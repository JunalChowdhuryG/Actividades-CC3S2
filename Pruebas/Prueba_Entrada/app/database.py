import psycopg2
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from question import Question
load_dotenv('.env')
# refactorizamos el metodo get_questions_from_db para que reciba un parameto opcional difficulty
def get_questions_from_db(difficulty=None):
    # validadmos que la dificulatad este entre 1 y 3
    if difficulty is not None and difficulty not in [1, 2, 3]:
        raise ValueError("La dificultad debe ser 1, 2 o 3")
    
    # connexion a la bd "trivia_db"  de postgres
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')


    # connexion a la bd "trivia_db"  de postgres
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = connection.cursor()

    # hacemos la consulta 
    if difficulty is not None:
        # hacemos la consulta si no se pasa la dificultad
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions
            WHERE difficulty = %s;
        """, (difficulty,))
    else:
        # hacemos la consulta si  se pasa la dificultad
        cursor.execute("""
            SELECT description, option_1, option_2, option_3, option_4, correct_option_index, difficulty
            FROM questions;
        """)

    rows = cursor.fetchall()
    connection.close()

    # creamos lista de "question" con los datos traidos de la bd
    questions = [
        Question(row[0], row[1:5], row[5], row[6])
        for row in rows
    ]
    # mezclamos las preguntas
    return questions
