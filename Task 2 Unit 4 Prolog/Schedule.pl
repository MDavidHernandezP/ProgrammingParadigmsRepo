% Horarios.
franja_horaria(1, '9:00-10:00').
franja_horaria(2, '10:00-11:00').
franja_horaria(3, '11:00-12:00').
franja_horaria(4, '1:00-2:00').
franja_horaria(5, '2:00-3:00').

% Recursos disponibles.
recurso(sala_a).
recurso(sala_b).
recurso(sala_c).

% Ejemplos de tareas con duraciones y dependencias.
tarea(tarea1, 'Tarea 1', 2, []).
tarea(tarea2, 'Tarea 2', 1, [tarea1]).
tarea(tarea3, 'Tarea 3', 2, []).
tarea(tarea4, 'Tarea 4', 1, [tarea2, tarea3]).

% Restricciones
% Una tarea no puede ser programada en franjas horarias que se superponen.
tareas_concurrentes(Tarea1, Tarea2) :-
    tarea(Tarea1, _, Duracion1, _),
    tarea(Tarea2, _, Duracion2, _),
    franja_horaria(Franja1, _),
    franja_horaria(Franja2, _),
    Tarea1 \= Tarea2,
    Franja1 + Duracion1 > Franja2,
    Franja1 < Franja2 + Duracion2.

% Una tarea requiere un recurso.
requiere_recurso(Tarea, Recurso) :-
    tarea(Tarea, _, _, _),
    recurso(Recurso).

% Una tarea no puede ser programada si sus dependencias no están completadas.
depende_de_tareas_completadas(Tarea, TareasCompletadas) :-
    tarea(Tarea, _, _, Dependencias),
    subtract(Dependencias, TareasCompletadas, []).

% Predicado para encontrar una programación válida.
programacion(Programacion) :-
    encontrar_programacion([], Programacion).

encontrar_programacion(TareasCompletadas, Programacion) :-
    tarea(Tarea, _, _, _),
    \+ member(Tarea, TareasCompletadas),
    depende_de_tareas_completadas(Tarea, TareasCompletadas),
    requiere_recurso(Tarea, Recurso),
    franja_horaria(FranjaHoraria, _),
    \+ tareas_concurrentes(Tarea, _),
    append(TareasCompletadas, [Tarea], TareasCompletadasActualizadas),
    encontrar_programacion(TareasCompletadasActualizadas, RestoProgramacion),
    Programacion = [(Tarea, Recurso, FranjaHoraria) | RestoProgramacion].

encontrar_programacion(_, []). % Caso base

% Ejemplo de uso.
% programacion(Programacion).
