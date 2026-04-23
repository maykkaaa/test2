from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from database import create_table, get_connection

app = FastAPI()

create_table()

class UserCreate(BaseModel):
    username: str
    email: str

@app.get("/users")
def get_user():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return [{"id":u[0],"username":u[1], "email":u[2]} for u in users]
@app.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"id":user[0],"username":user[1], "email":user[2]}
    raise HTTPException(status_code=404, detail="User not found")
@app.post("/create_user")
def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (user.username, user.email))
    conn.commit()
    conn.close()
    return {"message":"User created successfully"}
