from flask import Flask, render_template, request, redirect, url_for, session
from database import get_questions_from_db
from question import Question
from quiz import Quiz
import os

from dotenv import load_dotenv


app = Flask(__name__)
secret_key = os.environ.get("FLASK_SECRET_KEY")
app.secret_key = secret_key

#  funcion para guardar el estado del Quiz
def save_quiz(quiz):
    # retorna el estado: preguntas, la pregunta en la que va , respuestas correctas, incorrectas
    return {
        'questions': [
            {
                'description': q.description,
                'options': q.options,
                'correct_index': q.correct_index,
                'difficulty': q.difficulty
            } for q in quiz.questions
        ],
        'current_question_index': quiz.current_question_index,
        'correct_answers': quiz.correct_answers,
        'incorrect_answers': quiz.incorrect_answers
    }

# funcion paraa restaurar el estado del Quiz
def restore_quiz(data):
    quiz = Quiz()
    # crea la quiz a partir de los datos serializados
    quiz.questions = [
        Question(q['description'], q['options'], q['correct_index'], q['difficulty'])
        for q in data['questions']
    ]
    # asigna los valores de la quiz, la pregunta en la que va , respuestas correctas, incorrectas 
    quiz.current_question_index = data['current_question_index']
    quiz.correct_answers = data['correct_answers']
    quiz.incorrect_answers = data['incorrect_answers']
    return quiz

#  Ruta principal 
@app.route('/', methods=['GET', 'POST'])
def index():
    # pagina proncipal, donde se elige la dificultad
    if request.method == 'POST':
        difficulty = int(request.form['difficulty'])
        # obtiene las preguntas en base ala dificultad que se elige
        questions = get_questions_from_db(difficulty)[:10]
        # crea el quiz con las preguntas obtenidas
        quiz = Quiz()
        # agrega las preguntas al quiz
        for q in questions:
            quiz.add_question(q)
        session['quiz'] = save_quiz(quiz)
        # redirige a la ruta de preguntas
        return redirect(url_for('question'))
    return render_template('index.html')

#  muestra pregunta 
@app.route('/question', methods=['GET', 'POST'])
def question():
    quiz = restore_quiz(session['quiz'])
    # verifica si hay un quiz en la sesion
    if request.method == 'POST':
        answer = int(request.form['answer'])
        current_question = quiz.questions[quiz.current_question_index - 1]
        quiz.answer_question(current_question, answer)
    next_question = quiz.get_next_question()
    # verifica si quedan preguntas
    if next_question is None:
        session['quiz'] = save_quiz(quiz)
        return redirect(url_for('result'))
    # si no hay preguntas, redirige a los resultados
    session['quiz'] = save_quiz(quiz)
    return render_template('question.html', question=next_question, index=quiz.current_question_index)

#  muestra resultados 
@app.route('/result')
def result():
    if 'quiz' not in session:
        return redirect(url_for('index'))
    # recupera el quiz de la sesion
    quiz = restore_quiz(session['quiz'])
    # retorna resultados, respuestas correctas e incorrectas
    return render_template('result.html', correct=quiz.correct_answers, incorrect=quiz.incorrect_answers)

load_dotenv()
#  inicia la app 
if __name__ == '__main__':

    app.run(host=os.getenv("FLASK_HOST"), port=os.getenv("FLASK_PORT"))