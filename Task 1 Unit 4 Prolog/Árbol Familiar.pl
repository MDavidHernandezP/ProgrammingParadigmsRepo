% Mi familia porque no se me ocurrió otra.
hombre(raul).
hombre(mario).
hombre(david).

mujer(chabela).
mujer(yani).
mujer(kiara).

pariente(raul, mario).
pariente(raul, yani).
pariente(chabela, mario).
pariente(chabela, yani).

pariente(mario, david).

pariente(yani, kiara).

% Reglas.
padre(X, Y) :- hombre(X), pariente(X, Y).
madre(X, Y) :- mujer(X), pariente(X, Y).

hermano(X, Y) :- pariente(Z, X), pariente(Z, Y), X \= Y.

ancestro(X, Y) :- pariente(X, Y).
ancestro(X, Y) :- pariente(X, Z), ancestro(Z, Y).