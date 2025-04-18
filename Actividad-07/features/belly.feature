# language: es

Característica: Comportamiento del Estómago

  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: Esperar con horas, minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos fraccionarios
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Manejar pepinos negativos
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa.

  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero two hours and thirty minutes
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Verificar predicción de gruñido
    Dado que he comido 12 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir

  Escenario: Saber cuántos pepinos puedo comer antes de gruñir
    Dado que he comido 8 pepinos
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que puedo comer 3 pepinos más

  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 15 pepinos
    Entonces debería haber comido 15 pepinos

  Escenario: Verificar que el estómago no gruñe por poco tiempo
    Dado que he comido 20 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir

  Escenario: Verificar que el estómago gruñe si se cumple todo
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir
