from klaszterezo_app_data.clustermodel import ClusterModel
from klaszterezo_app_repository.clusterrepository import ClusterRepository
from flask_sqlalchemy import  SQLAlchemy
from flask import Flask
from typing import Dict
from klaszterezo_app_logic.jsonvalidator import JsonValidator

class Logic():
    
    def __init__(self, db : SQLAlchemy):
        self.db = db
        self.cluster_repo = ClusterRepository(self.db)
        self.validator = JsonValidator()

    def Write_Cluster_To_DB(self,input_groups: Dict ,output_groups : Dict):
        """
        writes old and new cluster groups to database
        """
        self.cluster_repo.Create(input_groups,output_groups)

    def Validate_JSON(self,input_json : str):
        """
        Validates JSON
        """
        self.validator.validate_json(input_json)

    def ReadFromDB(self,id: int) -> ClusterModel:
        """
        Reads element by ID
        """
        return self.cluster_repo.Read(id)
