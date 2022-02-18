from typing import Dict
from flask_sqlalchemy import  SQLAlchemy
from flask import Flask
from klaszterezo_app_data.clustermodel import ClusterModel

class ClusterRepository():
    """
    Implements basic CRUD for ClusterModel
    """

    def __init__(self, db : SQLAlchemy) -> None:
        self.db = db
        #db.create_all()

    def Read(self, id : int) -> ClusterModel:
        result = ClusterModel.query.filter_by(id=id).first()
        return result

    def Create(self,input_groups: Dict ,output_groups : Dict):
        cm = ClusterModel(input_groups,output_groups)
        self.db.session.add(cm)
        self.db.session.commit()

    def Update(self,id : int ,ip_groups: Dict ,out_groups : Dict):
        model = ClusterModel.query.get(id)
        model.input_groups = ip_groups
        model.output_groups = out_groups
        self.db.session.commit()

    def Delete(self,id : int):
        model = ClusterModel.query.get(id)
        self.db.session.delete(model)
        self.db.session.commit()

