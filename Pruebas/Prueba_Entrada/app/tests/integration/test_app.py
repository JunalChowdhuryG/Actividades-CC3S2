from dotenv import load_dotenv
import os
from app import app, save_quiz, restore_quiz
from quiz import Quiz
from question import Question
import unittest
from unittest.mock import patch

# cargamos las variables del archivo .env
load_dotenv()

class FlaskAppTestCase(unittest.TestCase):

    # Setup del entorno de prueba
    def setUp(self):
        app.config["TESTING"] = True
        app.secret_key = os.getenv("FLASK_SECRET_KEY_TEST","mi_clave_segura")
        self.client = app.test_client()

    # test para verificar que la aplicación se carga correctamente
    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Selecciona la dificultad", response.data)

    # test para verificar que los metodos save_quiz, restore_quiz funcionan correctamente
    def test_save_and_restore_quiz(self):
        quiz = Quiz()
        q1 = Question("¿Capital del Peru?", ["Lima", "Cusco", "Arquipa", "Trujillo"], 0, "Facil")
        quiz.add_question(q1)
        quiz.correct_answers = 1
        quiz.incorrect_answers = 0
        quiz.current_question_index = 1

        data = save_quiz(quiz)
        restored_quiz = restore_quiz(data)

        self.assertEqual(restored_quiz.correct_answers, 1)
        self.assertEqual(restored_quiz.questions[0].description, "¿Capital del Peru?")

    # test para verificar que la ruta /question se carga correctamente
    @patch('app.get_questions_from_db')
    def test_index_post_redirects_to_question(self, mock_get_questions):
        # Mock una lista de preguntas
        mock_get_questions.return_value = [
            Question("Pregunta 1", ["a", "b", "c","d"], 0, 1)
        ]

        response = self.client.post('/', data={'difficulty': '1'}, follow_redirects=False)

        # Debe redirigir a /question
        self.assertEqual(response.status_code, 302)
        self.assertIn('/question', response.location)


    # test para verificar que la ruta / se presente correctamente
    def test_index_get_renders_index_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Bienvenido al Juego de Trivia', response.data)

    # test para verificar que la ruta /result se cargue correctamente
    def test_result_without_session_redirects(self):
        response = self.client.get('/result', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/', response.location)

    # test para verificar que en la ruta /result se pueda volver a la pagina de inicio
    def test_result_redirects_without_session(self):
        response = self.client.get('/result', follow_redirects=True)
        self.assertIn(b'Selecciona la dificultad', response.data)

    # test para verificar que la ruta /result se cargue correctamente con una sesion activa y presente resultados
    def test_result_with_session(self):
        quiz = Quiz()
        question = Question("Pregunta?", ["a", "b"], 0, 1)
        quiz.add_question(question)
        quiz.correct_answers = 3
        quiz.incorrect_answers = 1

        with self.client.session_transaction() as session:
            session['quiz'] = save_quiz(quiz)

        response = self.client.get('/result')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Respuestas correctas: 3', response.data)
        self.assertIn(b'Respuestas incorrectas: 1', response.data)

    # test que verifica que la transicion de GET - POST - GET ..... al traer preguntas y enviar respuestas 
    def test_question_get_and_post(self):
        quiz = Quiz()
        question = Question("Pregunta?", ["a","b","c","d"], 0, 1)
        quiz.add_question(question)

        with self.client.session_transaction() as session:
            session['quiz'] = save_quiz(quiz)

        # Simula POST (responder la pregunta)
        response = self.client.post('/question', data={'answer': '0'}, follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pregunta', response.data)


if __name__ == '__main__':
    unittest.main()

