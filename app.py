from flask import Flask
from flask_restful import Api

from resources.task import Task, Tasks

from db import db

app= Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api= Api(app)
 

api.add_resource(Task, '/task/<string:name>')
api.add_resource(Tasks, '/tasks')

if __name__=="__main__":
    db.init_app(app)
    app.run(port=5000,debug=True)