from question import Question

# clase para el flujo de preguntas
class Quiz:
    def __init__(self): 
        self.questions = [] # lista de pregunta
        self.current_question_index = 0 # indice que indicca la pregunta actual
        self.correct_answers = 0  # Contador de respuestas correctas
        self.incorrect_answers = 0  # Contador de respuestas incorrectas

    # metodo para argrgar pregunta a la lista de pregunta
    def add_question(self, question):
        self.questions.append(question)

    # metodo para obtener la siguiente pregunta de la lista
    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None # hasta que no haya preguntas en la lista
    
    # metodo para los contadores de respuestas correctas e incorrectas
    def answer_question(self, question, answer_index):
        if question.is_correct(answer_index):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False