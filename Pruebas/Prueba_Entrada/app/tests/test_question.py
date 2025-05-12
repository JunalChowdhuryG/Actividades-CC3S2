from question import Question
import unittest

# test para la clase Question
class TestQuestion(unittest.TestCase):
    # test para la creacion de una pregunta
    def test_question_attributes(self):
        description = "¿Cual es 2 + 2?"
        options = ["1", "2", "3", "4"]
        correct_index = 3
        difficulty = 2
        question = Question(description, options, correct_index, difficulty)

        self.assertEqual(question.description, description)
        self.assertEqual(question.options, options)
        self.assertEqual(question.correct_index, correct_index)
        self.assertEqual(question.difficulty, difficulty)

    # test para el metodo is_correct con un respuesta correcto
    def test_question_correct_answer(self):
        question = Question("Capital de Lima", ["hUAROCHIRI", "Huacho", "Lima", "Huachipa"], 2, 1)
        self.assertTrue(question.is_correct(2))

    # test para el metodo is_correct con un respuesta incorrecto
    def test_question_incorrect_answer(self):
        question = Question("Capital de Lima", ["hUAROCHIRI", "Huacho", "Lima", "Huachipa"], 2, 1)
        self.assertFalse(question.is_correct(1))

    # test para el metodo is_correct con un respuesta fuera de rango
    def test_question_out_of_range_index(self):
        question = Question("Capital de Lima", ["hUAROCHIRI", "Huacho", "Lima", "Huachipa"], 2, 1)
        self.assertFalse(question.is_correct(4))  # indice fuera de rango

    # test para el metodo is_correct con un respuesta invaliaa
    def test_question_invalid_type(self):
        question = Question("2+2?", ["1", "2", "3", "4"], 3, 1)
        with self.assertRaises(TypeError):
            question.is_correct("tres")  # Tipo inválido

if __name__ == '__main__':
    unittest.main()