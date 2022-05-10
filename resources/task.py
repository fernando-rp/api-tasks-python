from flask_restful import Resource,reqparse

from models.task import TaskModel

class Task(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('name',
            type=str,
            required= True,
            help= "Este campo no puede estar vacío"

    )

    def get(self,name):        
        item= TaskModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return{'message':'La tarea no fue encontrada'},404
   
    def post(self,name):

        if TaskModel.find_by_name(name):
            return {'Error': "A task with name '{}' already exist".format(name)},400
        
        task=TaskModel(name)

        try:          
            task.save_to_db()
        except:
            return {'message': 'Ha ocurrido un error'},500
        
        return task.json(),201 
            
    def delete(self,name):
        item=TaskModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Tarea eliminada'}

    def put(self,name):

        data=Task.parser.parse_args()

        task=TaskModel.find_by_name(name)

        if task is None:
            task=TaskModel(name)
        else:
            task.name=data['name']
        
        task.save_to_db()
        
        return task.json()


class Tasks(Resource):
    def get(self):

        return {'tasks':[task.json() for task in TaskModel.query.all()]},200