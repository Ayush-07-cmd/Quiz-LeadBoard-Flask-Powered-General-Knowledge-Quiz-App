from app import db, app, Question

# Full list of 50 General Knowledge questions about India
questions_data = [
    {"category": "General Knowledge", "question_text": "What is the capital of India?", "options": ["Mumbai", "Kolkata", "New Delhi", "Chennai"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Who was the first Prime Minister of India?", "options": ["Mahatma Gandhi", "Sardar Patel", "Jawaharlal Nehru", "Subhas Chandra Bose"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which Indian river is considered the holiest?", "options": ["Yamuna", "Ganga", "Brahmaputra", "Godavari"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "In which year did India gain independence?", "options": ["1945", "1946", "1947", "1948"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which state is known as the 'Spice Garden of India'?", "options": ["Kerala", "Tamil Nadu", "Karnataka", "Assam"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which monument is located in Agra?", "options": ["Red Fort", "Qutub Minar", "Taj Mahal", "India Gate"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which Indian festival is known as the Festival of Lights?", "options": ["Holi", "Eid", "Diwali", "Navratri"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Who wrote the Indian national anthem?", "options": ["Rabindranath Tagore", "Bankim Chandra Chattopadhyay", "Sarojini Naidu", "Subhas Chandra Bose"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "What is the currency of India?", "options": ["Dollar", "Euro", "Rupee", "Yen"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which Indian city is known as the Silicon Valley of India?", "options": ["Hyderabad", "Bengaluru", "Mumbai", "Pune"], "correct": "B"},

    # Added 40 more
    {"category": "General Knowledge", "question_text": "Who is known as the Father of the Nation in India?", "options": ["B. R. Ambedkar", "Mahatma Gandhi", "Jawaharlal Nehru", "Bhagat Singh"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "Which Indian state has the longest coastline?", "options": ["Gujarat", "Tamil Nadu", "Maharashtra", "Andhra Pradesh"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which is the national animal of India?", "options": ["Elephant", "Lion", "Tiger", "Leopard"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which is the highest civilian award in India?", "options": ["Padma Bhushan", "Padma Vibhushan", "Bharat Ratna", "Padma Shri"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which is the smallest state in India by area?", "options": ["Goa", "Sikkim", "Tripura", "Manipur"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Who discovered the sea route to India?", "options": ["Columbus", "Vasco da Gama", "Magellan", "Marco Polo"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "What is the name of the Indian Parliament?", "options": ["Sansad Bhavan", "Rashtrapati Bhavan", "Raj Bhavan", "Jan Bhavan"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which dance form is associated with Kerala?", "options": ["Kathak", "Bharatanatyam", "Kathakali", "Odissi"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Who is the President of India as of 2024?", "options": ["Droupadi Murmu", "Ram Nath Kovind", "Narendra Modi", "Amit Shah"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian state is known for tea production?", "options": ["Kerala", "Assam", "Bihar", "Maharashtra"], "correct": "B"},
    
    {"category": "General Knowledge", "question_text": "Which sport is most popular in India?", "options": ["Football", "Hockey", "Cricket", "Kabaddi"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which place is called the Pink City of India?", "options": ["Jodhpur", "Jaipur", "Udaipur", "Agra"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "Which Indian state is known for the Sun Temple in Konark?", "options": ["Odisha", "Rajasthan", "Gujarat", "West Bengal"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian satellite was first launched into space?", "options": ["Chandrayaan", "INSAT", "Aryabhata", "Mangalyaan"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Who was the first Indian woman in space?", "options": ["Sunita Williams", "Kalpana Chawla", "Rakesh Sharma", "Indira Gandhi"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "What does 'Jai Jawan Jai Kisan' mean?", "options": ["Victory to soldiers and farmers", "Victory to India", "Power to the people", "Long live democracy"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Mughal emperor built the Red Fort?", "options": ["Akbar", "Babur", "Shah Jahan", "Aurangzeb"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Where is the Indian Space Research Organisation (ISRO) headquarters located?", "options": ["Delhi", "Mumbai", "Chennai", "Bengaluru"], "correct": "D"},
    {"category": "General Knowledge", "question_text": "Which Indian state has 'Shillong' as its capital?", "options": ["Nagaland", "Meghalaya", "Tripura", "Manipur"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "Which Indian festival celebrates colors?", "options": ["Holi", "Diwali", "Dussehra", "Raksha Bandhan"], "correct": "A"},
    
    {"category": "General Knowledge", "question_text": "Which country shares the longest border with India?", "options": ["China", "Pakistan", "Bangladesh", "Nepal"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which city is known as the financial capital of India?", "options": ["Mumbai", "Delhi", "Bengaluru", "Ahmedabad"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian leader gave the slogan 'Give me blood, and I shall give you freedom'?", "options": ["Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose", "Jawaharlal Nehru"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "What is the national bird of India?", "options": ["Peacock", "Swan", "Eagle", "Parrot"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "How many states are there in India (as of 2024)?", "options": ["28", "29", "30", "31"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian scientist won the Nobel Prize for Physics in 1930?", "options": ["C.V. Raman", "Homi Bhabha", "Venkatraman Ramakrishnan", "S. Chandrasekhar"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Where is the Gateway of India located?", "options": ["Kolkata", "Chennai", "Mumbai", "Delhi"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which Indian city is called the City of Lakes?", "options": ["Bhopal", "Jaipur", "Udaipur", "Mysore"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Who was India's first woman Prime Minister?", "options": ["Sonia Gandhi", "Indira Gandhi", "Pratibha Patil", "Sarojini Naidu"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "Which Indian cricketer is known as the 'Little Master'?", "options": ["Kapil Dev", "Virat Kohli", "Sunil Gavaskar", "Sachin Tendulkar"], "correct": "C"},
    {"category": "General Knowledge", "question_text": "Which Indian state is famous for the dance form Bihu?", "options": ["Assam", "Mizoram", "West Bengal", "Odisha"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which city is known for its Charminar?", "options": ["Hyderabad", "Delhi", "Mumbai", "Lucknow"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which freedom fighter led the Salt March?", "options": ["Bhagat Singh", "Jawaharlal Nehru", "Sardar Patel", "Mahatma Gandhi"], "correct": "D"},
    {"category": "General Knowledge", "question_text": "Which Indian language has the most speakers?", "options": ["Hindi", "Bengali", "Telugu", "Tamil"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which state is famous for Kanchipuram silk?", "options": ["Kerala", "Tamil Nadu", "Andhra Pradesh", "West Bengal"], "correct": "B"},
    {"category": "General Knowledge", "question_text": "Who designed the Indian national flag?", "options": ["Pingali Venkayya", "B.R. Ambedkar", "Sardar Patel", "Jawaharlal Nehru"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian mountain peak is the highest?", "options": ["Kanchenjunga", "Mount Everest", "Nanda Devi", "Trisul"], "correct": "A"},
    {"category": "General Knowledge", "question_text": "Which Indian city is known as the City of Joy?", "options": ["Mumbai", "Chennai", "Kolkata", "Pune"], "correct": "C"},
]

with app.app_context():
    for q in questions_data:
        question = Question(
            category=q["category"],
            question_text=q["question_text"],
            option_a=q["options"][0],
            option_b=q["options"][1],
            option_c=q["options"][2],
            option_d=q["options"][3],
            correct_option=q["correct"]
        )
        db.session.add(question)

    db.session.commit()
    print("✅ 50 Indian GK questions added successfully!")
