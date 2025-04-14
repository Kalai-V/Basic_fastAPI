import logging
db = [
    {"name": "Srinithi", "age": 20, "gender": "Female","email": "sri@gmail.com"},
    {"name": "Archana", "age": 20, "gender": "Female","email": "archana@gmail.com"}
]

def add_user(user: dict):
    logging.info(f"User added: {user}")
    db.append(user)

def get_all_users():
    return db