from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
import google.generativeai as genai
import logging
from functools import lru_cache
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

genai.configure(api_key="AIzaSyD1XJtiSMuln2ZdcJtVakXJUZNw0y_fkC4")  # Replace with your actual key

# ⚡️ Use LRU cache to store recent answers (max 100)
@lru_cache(maxsize=100)
def get_gk_answer(question):
    prompt = f"""
You are a fun and informative general knowledge (GK) quiz chatbot 🎓.
Always prioritize India-related topics when applicable 🇮🇳.

Instructions:
- Answer the question clearly and concisely in 2-4 sentences.
- Use emojis for fun and engagement 🎉🧠🌏📚.
- If the question is not GK-related, politely say: 
  "Sorry, I can only help with general knowledge questions! 🙏"

User question: {question}
"""

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text.strip()

app = Flask(__name__)
app.secret_key = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    score = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    question_text = db.Column(db.Text)
    option_a = db.Column(db.String(100))
    option_b = db.Column(db.String(100))
    option_c = db.Column(db.String(100))
    option_d = db.Column(db.String(100))
    correct_option = db.Column(db.String(1))

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"reply": "Please ask a general knowledge question! 📚"})

        answer = get_gk_answer(user_input)
        return jsonify({"reply": answer})
    except Exception as e:
        logging.error(f"Chatbot Error: {e}")
        return jsonify({"reply": "Oops! Something went wrong. Try again later. 😔"})


@app.route('/quiz', methods=['POST'])
def quiz():
    username = request.form['username']
    avatar = request.form['avatar']
    session['username'] = username
    session['avatar'] = avatar
    questions = Question.query.order_by(db.func.random()).limit(10).all()
    session['questions'] = [q.id for q in questions]
    return render_template('quiz.html', questions=questions, avatar=avatar)

@app.route('/submit', methods=['POST'])
def submit():
    question_ids = session.get('questions', [])
    score = 0
    for qid in question_ids:
        question = Question.query.get(qid)
        selected = request.form.get(str(qid))
        if selected == question.correct_option:
            score += 1
    user = User(username=session['username'], score=score)
    db.session.add(user)
    db.session.commit()
    session['score'] = score
    return redirect(url_for('result'))

@app.route('/result')
def result():
    score = session.get('score', 0)

    if score <= 4:
        performance = "😢 You failed the quiz"
    elif 5 <= score <= 6:
        performance = "😐 You passed, but it's average"
    elif 7 <= score <= 8:
        performance = "🙂 Good score!"
    elif score == 9:
        performance = "👏 Excellent work!"
    else:
        performance = "🌟 Outstanding!!"

    return render_template('result.html', score=score, performance=performance)


@app.route('/leaderboard')
def leaderboard():
    top_users = User.query.order_by(User.score.desc(), User.timestamp.asc()).limit(10).all()
    return render_template('leaderboard.html', users=top_users)

if __name__ == '__main__':
    app.run(debug=True)
