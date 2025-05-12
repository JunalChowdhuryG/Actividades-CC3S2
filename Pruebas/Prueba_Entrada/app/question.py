# creacion clase Question
class Question:
    # constructor de la clase Question
    def __init__(self, description, options, correct_index, difficulty):
        self.description = description
        self.options = options
        self.correct_index = correct_index
        self.difficulty = difficulty

    # answer_index es el inddice de la respuesta seleccionada por el usuario
    # verifica si la respuesta dadad por el usuario es correcta
    def is_correct(self, answer_index):
        if not isinstance(answer_index, int):
            raise TypeError("answer_index debe ser un entero")
        return self.correct_index == answer_index