from database import get_questions_from_db
from unittest.mock import patch, MagicMock
from database import get_questions_from_db
from question import Question
import unittest

#  test:verifica la conectividad con la base datos y la obtencion de preguntas 
class TestGetQuestions(unittest.TestCase):
    @patch("database.psycopg2.connect")
    def test_with_valid_difficulty(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("¿Capital de Peru?", "Arquipa", "Lima", "Tacna", "Trujillo", 1, 1),
            ("¿2 + 2?", "1", "2", "3", "4", 3, 1),
        ]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        questions = get_questions_from_db(1)

        self.assertIsInstance(questions, list)
        self.assertEqual(len(questions), 2)
        self.assertTrue(all(isinstance(q, Question) for q in questions))
        self.assertEqual(questions[0].difficulty, 1)
        self.assertEqual(questions[0].description, "¿Capital de Peru?")


class TestDatabaseQuestions(unittest.TestCase):

    # test quee verifica la obtencion de preguntas con dificultad
    @patch("database.psycopg2.connect")
    def test_get_questions_with_valid_difficulty(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("¿Capital de Peru?", "Arquipa", "Lima", "Tacna", "Trujillo", 1, 1),
            ("¿2 + 2?", "1", "2", "3", "4", 3, 1),
        ]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        questions = get_questions_from_db(1)

        self.assertIsInstance(questions, list)
        self.assertEqual(len(questions), 2)
        self.assertTrue(all(isinstance(q, Question) for q in questions))
        self.assertEqual(questions[0].difficulty, 1)
        self.assertEqual(questions[0].description, "¿Capital de Peru?")

    # test quee verifica la obtencion de preguntas sin dificultad
    @patch("database.psycopg2.connect")
    def test_get_questions_without_difficulty(self, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            ("Pregunta prueba", "A", "B", "C", "D", 0, 2)
        ]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_connection

        questions = get_questions_from_db()

        self.assertEqual(len(questions), 1)
        self.assertIsInstance(questions[0], Question)
        self.assertEqual(questions[0].description, "Pregunta prueba")

    # test que verifica que no es posible obtener preguntas con una dificultad invalida
    def test_get_questions_with_invalid_difficulty(self):
        with self.assertRaises(ValueError):
            get_questions_from_db(5)

if __name__ == '__main__':
    unittest.main()
