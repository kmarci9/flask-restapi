import requests

BASE = "http://flaskrestapi-env.eba-9a5pem3p.us-east-1.elasticbeanstalk.com/"

json_groups = """{
     "group_1": [[0.1, -0.2, 0.3], [0.4, -0.5, 0.6]],
	 "group_2": [[0.33, 0.42, -0.1]],
	 "group_3": [[-0.7564, 0.9845, 0.66], [-0.55,-0.55, -0.55], [0.3, 0.33, 0.333]]
 }
"""

response = requests.post(BASE + "groups", json = json_groups)

print (json_groups)

print (response.json())

#requests.post(BASE + "read", json = json_groups)

