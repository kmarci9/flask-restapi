from flask_sqlalchemy import  SQLAlchemy,Model
from typing import Dict
from sqlalchemy.types import TypeDecorator
from sqlalchemy import Column, Integer
from imports import db
import json
import sqlalchemy


class PickleType(db.TypeDecorator):

    impl = sqlalchemy.Text(1024)

    def process_bind_param(self, value, dialect):
        """
        json.dumps() function converts a Python object into a json string.
        """
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        """
        json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.
        """
        if value is not None:
            value = json.loads(value)
        return value


class ClusterModel(db.Model):
    __tablename__ = "cluster"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False)
    input_groups = db.Column(db.PickleType(), nullable=False)
    output_groups = db.Column(db.PickleType(), nullable=False)

    def __init__(self,input_groups : Dict,output_groups : Dict ) -> None:
        self.input_groups = input_groups
        self.output_groups = output_groups
        super(ClusterModel,self).__init__()

    def __repr__(self) -> str:
        return f"repr: ID: {self.id} input_groups = {self.input_groups} output groups= {self.output_groups}"



