% Este program no soluciona como tal el sudoku.
% Más bien valida si el sudoku (respondido) es correcto.
sudoku(Puzzle) :-
    Puzzle = [
        Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9
    ],
    
    % En ninguna fila, columna y cuadricula se deben repetir valores.
    valid(Row1), valid(Row2), valid(Row3),
    valid(Row4), valid(Row5), valid(Row6),
    valid(Row7), valid(Row8), valid(Row9),
	% Validación de columnas.
    transpose(Puzzle, [Col1, Col2, Col3, Col4, Col5, Col6, Col7, Col8, Col9]),
    valid(Col1), valid(Col2), valid(Col3),
    valid(Col4), valid(Col5), valid(Col6),
    valid(Col7), valid(Col8), valid(Col9),
	% Validación de cuadriculas.
    subgrid(Row1, Row2, Row3),
    subgrid(Row4, Row5, Row6),
    subgrid(Row7, Row8, Row9).

% Validación de listas, deben tener valores distintos del 1 al 9.
valid([]).
valid([Head|Tail]) :-
    number(Head),
    Head > 0,
    Head =< 9,
    \+ member(Head, Tail),
    valid(Tail).

% Intercambiando filas y columnas para la validarlas.
transpose([], []).
transpose([[]|_], []).
transpose(Matrix, [Row|Rows]) :-
    transpose_row(Matrix, Row, RestMatrix),
    transpose(RestMatrix, Rows).

transpose_row([], [], []).
transpose_row([[H|T]|Rows], [H|Hs], [T|Ts]) :-
    transpose_row(Rows, Hs, Ts).

% Validación de cuadriculas si las filas son válidas.
subgrid([], [], []).
subgrid([A, B, C|Rest1], [D, E, F|Rest2], [G, H, I|Rest3]) :-
    valid([A, B, C, D, E, F, G, H, I]),
    subgrid(Rest1, Rest2, Rest3).

% Ejemplo de uso.
% sudoku([
%     [5, 3, _, _, 7, _, _, _, _],
%     [6, _, _, 1, 9, 5, _, _, _],
%     [_, 9, 8, _, _, _, _, 6, _],
%     [8, _, _, _, 6, _, _, _, 3],
%     [4, _, _, 8, _, 3, _, _, 1],
%     [7, _, _, _, 2, _, _, _, 6],
%     [_, 6, _, _, _, _, 2, 8, _],
%     [_, _, _, 4, 1, 9, _, _, 5],
%     [_, _, _, _, 8, _, _, 7, 9]
% ]). 
% Incompleto = false

% sudoku([
%     [5, 3, 4, 6, 7, 8, 9, 1, 2],
%     [6, 7, 2, 1, 9, 5, 3, 4, 8],
%     [1, 9, 8, 3, 4, 2, 5, 6, 7],
%     [8, 5, 9, 7, 6, 1, 4, 2, 3],
%     [4, 2, 6, 8, 5, 3, 7, 9, 1],
%     [7, 1, 3, 9, 2, 4, 8, 5, 6],
%     [9, 6, 1, 5, 3, 7, 2, 8, 4],
%     [2, 8, 7, 4, 1, 9, 6, 3, 5],
%     [3, 4, 5, 2, 8, 6, 1, 7, 9]
% ]).
% Completado y correcto = true