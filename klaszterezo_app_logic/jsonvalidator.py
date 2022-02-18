import json
from jsonschema import validate, ValidationError, SchemaError
from typing import Dict

schema = {
    "type" : "object",
    "patternProperties" : {
        "^group_[1-9]+$" : {
            "type" : "array",
            "items" : {
                "type" : "array",
                "items" : {
                    "type" : "number",
                },
                "minItems" : 1
            },
            "minItems" : 1
        },
    },
    "additionalProperties": False
}

class JsonValidator():

    def _check_group_naming(self,ip_json : Dict):
        """
        checks if group naming is continuous, if not throws InvalidJsonException
        """
        keys_list = list(ip_json)
        for i,(key_value) in enumerate(ip_json):
            recent_num = int(keys_list[i][6:])
            if i > 0:
                prev_num = int((keys_list[i-1][6:])) 
                if prev_num != recent_num- 1:
                    raise InvalidJsonException("Invalid group numbering, group numbers should be continuous starting from 1")

    def _check_array_len(self,ip_json: Dict):
        """
        checks if every input array has the same size
        throws InvalidJsonException if not
        """
        arr_len = len(ip_json.get('group_1')[0])
        for key, value in ip_json.items():
            for items in value:
                if len(items) != arr_len:
                    raise InvalidJsonException("Invalid length of input arrays, every array must have the same size")

    def validate_json(self,input_json: str) -> str:
        """
        input json: string

        Validates input json, checks continous naming,if every array has the same size, proper group naming
        """
        my_json = json.loads(input_json)
        validate(my_json, schema)
        self._check_array_len(my_json)
        self._check_group_naming(my_json)
        


class InvalidJsonException(Exception):
    pass
