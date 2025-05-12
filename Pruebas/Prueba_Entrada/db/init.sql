-- creacion de la tabla
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    option_4 TEXT NOT NULL,
    correct_option_index INT NOT NULL CHECK (correct_option_index BETWEEN 0 AND 3),
    difficulty INT NOT NULL CHECK (difficulty BETWEEN 1 AND 3)
);

--  preguntas de prueba
-- preguntas nivel 1
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('¿En qué año se proclamó la Independencia del Perú?', '1810', '1821', '1835', '1840', 1, 1),
('¿Quién fue el primer presidente del Perú?', 'Simón Bolívar', 'José de San Martín', 'José de la Riva-Agüero', 'Ramón Castilla', 2, 1),
('¿Qué civilización antigua construyó Machu Picchu?', 'Chavín', 'Moche', 'Inca', 'Nazca', 2, 1),
('¿Cuál fue la capital del Imperio Inca?', 'Lima', 'Cusco', 'Arequipa', 'Trujillo', 1, 1),
('¿Qué conquistador lideró la caída del Imperio Inca?', 'Hernán Cortés', 'Francisco Pizarro', 'Diego de Almagro', 'Pedro de Valdivia', 1, 1),
('¿Qué batalla selló la independencia del Perú?', 'Ayacucho', 'Junín', 'Tarapacá', 'Angamos', 0, 1),
('¿Qué presidente peruano abolió la esclavitud?', 'Ramón Castilla', 'Andrés Avelino Cáceres', 'Nicolás de Piérola', 'Augusto B. Leguía', 0, 1),
('¿Qué recurso fue clave en la economía del Virreinato del Perú?', 'Oro', 'Plata', 'Petróleo', 'Cobre', 1, 1),
('¿Qué país invadió las Islas Chincha en 1864?', 'Chile', 'España', 'Ecuador', 'Gran Bretaña', 1, 1),
('¿Qué tratado puso fin a la Guerra del Pacífico?', 'Tratado de Ancón', 'Tratado de Lima', 'Tratado de Paz con Chile', 'Tratado de Guayaquil', 0, 1);

-- preguntas nivel 2
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('¿Qué rebelión indígena fue liderada por Túpac Amaru II?', 'Rebelión de Huánuco', 'Gran Rebelión de 1780', 'Revolución de Tacna', 'Sublevación de Huaraz', 1, 2),
('¿Qué presidente implementó el "Oncenio" en el Perú?', 'Óscar R. Benavides', 'Augusto B. Leguía', 'Manuel Prado', 'Fernando Belaúnde', 1, 2),
('¿Qué conflicto armado enfrentó a Perú y Ecuador en 1941?', 'Guerra del Cenepa', 'Guerra del Pacífico', 'Guerra de Zarumilla', 'Guerra del 41', 3, 2),
('¿Qué héroe naval peruano murió en el Combate de Angamos?', 'Miguel Grau', 'Francisco Bolognesi', 'Alfonso Ugarte', 'Andrés Avelino Cáceres', 0, 2),
('¿Qué cultura preinca construyó las Líneas de Nazca?', 'Paracas', 'Nazca', 'Moche', 'Chimú', 1, 2),
('¿Qué virrey del Perú fue el más destacado?', 'Virrey Toledo', 'Virrey Pezuela', 'Virrey La Serna', 'Virrey Abascal', 0, 2),
('¿En qué año se dio el "Baguazo"?', '2007', '2009', '2011', '2013', 1, 2),
('¿Qué grupo terrorista fue liderado por Abimael Guzmán?', 'MRTA', 'Sendero Luminoso', 'Movimiento Revolucionario', 'Vanguardia Revolucionaria', 1, 2),
('¿Qué batalla fue clave en la Guerra del Pacífico?', 'Batalla de Arica', 'Batalla de Huamachuco', 'Batalla de Miraflores', 'Batalla de Tarapacá', 2, 2),
('¿Qué presidente peruano fue derrocado por Fujimori en 1992?', 'Alan García', 'Valentín Paniagua', 'Alberto Fujimori', 'Fernando Belaúnde', 0, 2);

-- preguntas nivel 3
INSERT INTO questions (description, option_1, option_2, option_3, option_4, correct_option_index, difficulty)
VALUES
('¿Qué líder indígena resistió en la "Breña" durante la Guerra del Pacífico?', 'Miguel Iglesias', 'Lizardo Montero', 'Andrés A. Cáceres', 'Francisco García Calderón', 2, 3),
('¿Qué tratado cedió Tarapacá a Chile después de la Guerra del Pacífico?', 'Tratado de Lima', 'Tratado de Ancón', 'Tratado de Valparaíso', 'Tratado de Paz y Amistad', 1, 3),
('¿Qué presidente peruano nacionalizó el petróleo en 1968?', 'Fernando Belaúnde', 'Juan Velasco Alvarado', 'Francisco Morales Bermúdez', 'Manuel Prado', 1, 3),
('¿Qué cultura preinca es conocida por sus "huacos retratos"?', 'Chavín', 'Moche', 'Chimú', 'Paracas', 1, 3),
('¿Qué batalla marcó el fin de la Confederación Perú-Boliviana?', 'Yungay', 'Ingavi', 'Ayacucho', 'Junín', 0, 3),
('¿Qué líder del MRTA murió en la toma de la residencia del embajador de Japón?', 'Néstor Cerpa Cartolini', 'Víctor Polay Campos', 'Oscar Ramírez Durand', 'Abimael Guzmán', 0, 3),
('¿Qué virrey intentó sofocar la Rebelión de Túpac Amaru II?', 'Virrey Amat', 'Virrey Jáuregui', 'Virrey Abascal', 'Virrey Pezuela', 1, 3),
('¿Qué héroe civil peruano murió defendiendo el Morro de Arica?', 'Alfonso Ugarte', 'Francisco Bolognesi', 'Miguel Grau', 'Andrés A. Cáceres', 1, 3),
('¿En qué gobierno se creó el Sol (nuevo sol) como moneda oficial?', 'Alan García (1985)', 'Alberto Fujimori (1991)', 'Alejandro Toledo (2001)', 'Fernando Belaúnde (1980)', 1, 3),
('¿Qué arqueólogo descubrió la ciudadela de Caral?', 'Julio C. Tello', 'Ruth Shady', 'Walter Alva', 'Luis Lumbreras', 1, 3);