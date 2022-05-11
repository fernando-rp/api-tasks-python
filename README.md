# API-Tasks-fwd

Api-tasks-fwd es una api para agregar, modificar, agregar y eliminar tareas.

## Installation

Usa el paquete [pip](https://pip.pypa.io/en/stable/), para posteriormente crear el ambiente virtual como "pipenv" y finalmente hacer correr la aplicación.

```bash
pip install 
```

```bash
pipenv shell 
```
```bash
python3 app.py 
```


## Usage


Para obtener todas las tareas:
```bash
GET/tasks 
```
Para obtener una tarea en específico:
```bash
GET/task/<name>
```
Para agregar una nueva tarea:
```bash
POST/task/<name>
```
Para eliminar una tarea:
```bash
DELETE/task/<name>
```
Para actualizar una tarea existente o agregar una nueva:
```bash
PUT/task/<name>

{ "name": "nombre-tarea"}
```

## Contributing
Son bienvenidos los pull request. Para cambios mayores por favor primero abre una discusión para revisar lo que te gustaría modificar.


## Hecho por:
FWD
