% Colección de libros.
libro("Libro de Cocina", "David Hernández", "Cocina").
libro("Los Juegos del Hambre", "Suzane Collins", "Ciencia ficción").
libro("Breve Historia del Tiempo", "Stephen Hawking", "Cosmología").
libro("Cien Años de Soledad", "Gabriel García Márquez", "Realismo Mágico").

% Reglas y Consultas? No entendí bien esto.
autor_libro(Autor, Libros) :- findall(Libro, libro(Libro, Autor, _), Libros).

genero_libro(Genero, Libros) :- findall(Libro, libro(Libro, _, Genero), Libros).