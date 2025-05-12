from question import Question
from quiz import Quiz
from database import get_questions_from_db

# funcion para seleccionar la dificultad del quiz
def seleccionar_dificultad():
    print("Bienvenido al Quiz de Historia del Peru")
    # solicita el nivel de dificultad
    print("Elige la dificultad del Quiz")
    print("1. Facil")
    print("2. Intermedio")
    print("3. Dificil")
    print("4. Mixto")

    # verifica la entrada del usuario
    while True:
        try:
            # validad la entrada de la dificultad
            nivel = int(input("respuesta >>> "))
            if 1 <= nivel <= 4:
                nivel -= 1
                break
            else:
                print("Opcion no disponible, vuelve a intentar")
        except ValueError:
            print("entrada invalida - vuelvea intentar")
    return nivel

# muestra las preguntas en pantalla
def mostrar_pregunta(quiz, question):
    print(f"Pregunta {quiz.current_question_index}: {question.description}")
    for idx, opt in enumerate(question.options):
        print(f"{idx + 1}. {opt}")

# solicita la respuesta del usuario
def obtener_respuesta_valida(num_opciones):
    while True:
        # valida la respuesta
        try:
            answer = int(input("respuesta >>> "))
            if 1 <= answer <= num_opciones:
                answer -= 1  # restamos 1 para que coincida con los índices (0-3)
                break
            else:
                print("clave no permitida, vuelve a intentar")
        except ValueError:
            print("entrada invalida - vuelvea intentar")
    return answer



def mostrar_resultados(quiz):
    # muestra el resultado final
    print("\n============ Juego terminado ============\n")
    print(f"respuestas Correctas: {quiz.correct_answers}")
    print(f"respuestas Incorrectas: {quiz.incorrect_answers}")
    


def run_quiz():
    # inicia el objeto Quiz
    quiz = Quiz()
    
    # selecciona la dificultad
    nivel=seleccionar_dificultad()
    
    # obtiene las preguntas de la base de datos en base al nivel elegido
    questions = get_questions_from_db()[:10] if nivel == 4 else get_questions_from_db(nivel)[:10]
    for question in questions:
        quiz.add_question(question)

    # inicia el juego
    while True:
        question = quiz.get_next_question()
        if not question:
            break

        mostrar_pregunta(quiz, question)
        
        respuesta =  obtener_respuesta_valida(len(question.options))
        
        # verifica si la respuesta es correcta
        if quiz.answer_question(question, respuesta):
            print("======== Correcto =======")
        else:
            print("======== Incorrecto =======")

    # termina el juego
    mostrar_resultados(quiz)

# funcion principal
# inicia el programa
def main():
    print("\nDia 7 - Gestión de configuración, seguridad y pruebas de rendimiento\n ")
    run_quiz()

if __name__ == "__main__":
    main()