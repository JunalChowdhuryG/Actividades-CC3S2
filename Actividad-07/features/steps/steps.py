from behave import given, when, then
from src.belly import Belly
import re
import random

# Diccionarios de palabras numericas en espanol ingles
# dicionario espanol
NUMEROS_ES = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60,
    "setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5
}
# diccionario ingles
NUMEROS_EN = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,
    "half": 0.5
}

# funcion para convertir palabras a numeros en espanol e ingles
def convertir_palabra_a_numero(palabra):
    if not palabra:
        return 0
    palabra = palabra.strip().lower()

    # Manejar casos especiales
    # en espanol
    if palabra in NUMEROS_ES:
        return NUMEROS_ES[palabra]
    # en ingles
    if palabra in NUMEROS_EN:
        return NUMEROS_EN[palabra]
    # para los casos decimales
    try:
        return float(palabra)
    except ValueError:
        return 0

# caso  cuando ah comido pepinos
@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        context.belly.comer(float(cukes))
    except Exception as e:
        context.exception = e

# extraer el tiempo de espera
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    desc = time_description.strip('"').lower()

    # Caso aleatorio
    if "aleatorio" in desc:
        match = re.search(r'entre (\d+(?:\.\d+)?) y (\d+(?:\.\d+)?) horas', desc)
        if match:
            min_h = float(match.group(1))
            max_h = float(match.group(2))
            random.seed(42)
            tiempo = round(random.uniform(min_h, max_h), 2)
            context.belly.esperar(tiempo)
            return

    # caso especial: media hora
    if desc == 'media hora':
        context.belly.esperar(0.5)
        return

    # para casos 1.5 horas
    if re.fullmatch(r'\d+(\.\d+)? horas?', desc):
        horas = float(desc.split()[0])
        context.belly.esperar(horas)
        return
    
    # Parsing con palabras en espanol 
    #pattern = re.compile(r'(?:(\w+)\s*horas?)?[ ,y]*(?:(\w+)\s*minutos?)?[ ,y]*(?:(\w+)\s*segundos?)?')

    # refactorizamoss el patron para manejar casos espanol ingles
    pattern = re.compile(
        r'(?:(\w+)\s*(?:hora|horas|hour|hours))?[ ,y]*(?:(\w+)\s*(?:minuto|minutos|minute|minutes))?[ ,y]*(?:(\w+)\s*(?:segundo|segundos|second|seconds))?'
    )
    # encontramos coincidencia con el patron
    match = pattern.match(desc)
    if match:
        # extraemos las palabras horas, minutos y segundos 
        h_word = match.group(1)
        m_word = match.group(2)
        s_word = match.group(3)

        # convertimos las palabras a numeros con la funcion convertir_palabra_a_numero
        h = convertir_palabra_a_numero(h_word) if h_word else 0
        m = convertir_palabra_a_numero(m_word) if m_word else 0
        s = convertir_palabra_a_numero(s_word) if s_word else 0

        # calculamos el tiempo total
        total = h + (m / 60) + (s / 3600)

        context.belly.esperar(total)
        return
    # lanzamos error si se interpreta mal
    raise ValueError(f"no se puede interpretar: {desc}")

# caso cuantos pepinos mas puedo comer
@when('pregunto cuántos pepinos más puedo comer')
def step_when_ask_remaining_cucumbers(context):
    context.restantes = context.belly.pepinos_para_gruñir()

# caso cuando el estomago gruñe
@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruniendo(), "Se esperaba que gruñera, pero no lo hizo"

# caso cuando el estomago no gruñe
@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruniendo()

# caso cuando el estomago no gruñ
@then('debería ocurrir un error de cantidad negativa.')
def step_then_should_raise_error(context):
    assert context.exception is not None
    assert isinstance(context.exception, ValueError)

# caso cuantos pepinos mas puedo comer
@then('debería decirme que puedo comer {cantidad:g} pepinos más')
def step_then_pepinos_restantes(context, cantidad):
    assert context.restantes == cantidad

# caso cuantos pepinos deberiaa habeer comido
@then('debería haber comido {esperado:g} pepinos')
def step_then_total_pepinos(context, esperado):
    assert context.belly.pepinos_comidos == esperado

# caso predecir gruñir
@then('el sistema debería predecir que va a gruñir en {horas:g} horas')
def step_then_prediccion(context, horas):
    assert context.belly.predecir_gruñido(context.belly.pepinos_comidos, horas)