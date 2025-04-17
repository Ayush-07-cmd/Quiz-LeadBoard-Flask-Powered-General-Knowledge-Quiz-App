from app import db, app

with app.app_context():
    db.drop_all()          # ❌ Drop all existing tables and data
    db.create_all()        # ✅ Recreate empty tables
    print("Database cleaned and initialized successfully!")
