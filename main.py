from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# koneksi DB
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="spam_api"
)

cursor = db.cursor()

@app.get("/")
def home():
    return {"message": "API + MySQL jalan 🚀"}


@app.post("/message")
def save_message(data: dict):
    text = data.get("text")

    query = "INSERT INTO messages (text, prediction) VALUES (%s, %s)"
    values = (text, "unknown")

    cursor.execute(query, values)
    db.commit()

    return {"message": "data berhasil disimpan"}


@app.get("/messages")
def get_messages():
    cursor.execute("SELECT * FROM messages")
    result = cursor.fetchall()

    return {"data": result}