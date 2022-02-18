import subprocess
import json
import re
import os
import platform
from typing import Dict



class Clustering():

    @staticmethod
    def run_clustering(input_json : str) -> Dict:
        """
        runs re-clustering with the binary provided
        input : raw json string
        returns Dictionary which contains the re-clustered groups
        """
        threshold = "1.0"
        parent_root = os.path.abspath(os.curdir)
        dir_path = os.path.join(parent_root,"klaszterezo_algoritmus_bin")

        if platform.system() == "Linux":
            command = [os.path.join(dir_path,"lexunit-exercise-linux-amd64",), input_json, threshold]
        elif platform.system() == "Windows":
            command = [os.path.join(dir_path,"lexunit-exercise-windows-amd64.exe",), input_json, threshold]
        res = subprocess.run(command,cwd=dir_path , check= True, capture_output=True, text= True)
        output = res.stdout
        p = re.compile(r'(\{.*\})')
        try:
            res = next(p.finditer(output))
            return json.loads(res.group())
        except StopIteration:
            raise Exception("No result found")


        

