import unittest
from quiz import Quiz
from question import Question

# test para comprobar metodo add_question de la clase Quiz
class TestQuiz(unittest.TestCase):

    # test para comprobar que la clase Quiz se inicializa correctamente
    def test_add_question(self):
        quiz = Quiz()
        q = Question("¿Cual fue la capital del Imperio Inca?", ['Lima', 'Cusco', 'Arequipa', 'Trujillo'], 1, 1)
        quiz.add_question(q)
        self.assertEqual(len(quiz.questions), 1)
        self.assertEqual(quiz.questions[0].description, "¿Cual fue la capital del Imperio Inca?")

    # test para comprobar si se agregan  preguntas
    def test_get_next_question_returns_correctly(self):
        quiz = Quiz()
        q1 = Question("pregunta prueba 1", ["A", "B", "C", "D"], 0, 1)
        q2 = Question("pregunta prueba 2", ["A", "B", "C", "D"], 1, 2)
        quiz.add_question(q1)
        quiz.add_question(q2)
        self.assertEqual(quiz.get_next_question(), q1)
        self.assertEqual(quiz.get_next_question(), q2)

    # test para comprobar que se devuelve None si no hay preguntas
    def test_get_next_question_returns_none_when_empty(self):
        quiz = Quiz()
        self.assertIsNone(quiz.get_next_question())

    # test para comprobar que se devuelve None si no hay preguntas
    def test_get_next_question_returns_none_after_all_questions(self):
        quiz = Quiz()
        q1 = Question("pregunta prueba", ["A", "B", "C", "D"], 1, 3)
        quiz.add_question(q1)
        quiz.get_next_question()  # consume la pregunta
        self.assertIsNone(quiz.get_next_question())

    # test para comprobar si comprueba la respuesta correcta, y los contadores de respuestas correctas e incorrectas
    def test_quiz_scoring(self):
        quiz = Quiz()
        question = Question("pregunta prueba", ["A", "B", "C", "D"], 3, 1)
        quiz.add_question(question)
        self.assertTrue(quiz.answer_question(question, 3))
        self.assertEqual(quiz.correct_answers, 1)
        self.assertEqual(quiz.incorrect_answers, 0)

    # test para comprobar si comprueba la respuesta incorrecta, y los contadores de respuestas correctas e incorrectas
    def test_quiz_incorrect_answer(self):
        quiz = Quiz()
        question = Question("pregunta prueba", ["A", "B", "C", "D"], 2, 1)
        quiz.add_question(question)
        self.assertFalse(quiz.answer_question(question, 1))
        self.assertEqual(quiz.correct_answers, 0)
        self.assertEqual(quiz.incorrect_answers, 1)

if __name__ == '__main__':
    unittest.main()