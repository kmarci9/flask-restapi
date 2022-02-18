from flask import Flask, request, jsonify, abort, Response
from flask_sqlalchemy import SQLAlchemy
import json
from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
from klaszterezo_app_logic.clustering import Clustering
from klaszterezo_app_logic.logic import Logic
#from imports import  *

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///klaszterezo_app_data/database.db"
db = SQLAlchemy(application)
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

logic = Logic(db)

@application.route("/groups",  methods = ['POST'])
def process_groups():
    """
    Endpoint for clustering vector groups
    returns: clustered json
    """
    try:
        ip_json = request.get_json()
        error = logic.Validate_JSON(ip_json)
        output_dict = Clustering.run_clustering(ip_json)
        logic.Write_Cluster_To_DB(json.loads(ip_json),output_dict)
        return jsonify(output_dict), 201
    except Exception as err:
        msg = str(err)
        return {
                'status': 400,
                'Error': msg,
            }, 400
        #abort(Response(msg))
    


@application.route("/read",  methods = ['POST'])
def read_db():
    """
    Reads first element for testing
    """
    asd = logic.ReadFromDB(1)
    print(repr(asd))
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    
if __name__ == "__main__":
    application.run(debug=True)