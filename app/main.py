import os
import pymysql
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "dev")
DB_PASS = os.getenv("DB_PASS", "devpass")

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def run_sql(sql: str):
    conn = pymysql.connect(
        host=DB_HOST, port=DB_PORT,
        user=DB_USER, password=DB_PASS,
        database=DB_NAME, autocommit=False, charset="utf8mb4"
    )
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            if cur.description:
                cols = [d[0] for d in cur.description]
                rows = cur.fetchall()
                return cols, rows
            else:
                conn.commit()
                return [], []
    finally:
        conn.close()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    sample = "SELECT id, name, email, created_at FROM users ORDER BY id;"
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "sql": sample, "cols": None, "rows": None, "error": None}
    )

@app.post("/query", response_class=HTMLResponse)
def query(request: Request, sql: str = Form(...)):
    try:
        cols, rows = run_sql(sql)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "sql": sql, "cols": cols, "rows": rows, "error": None}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "sql": sql, "cols": None, "rows": None, "error": str(e)}
        )