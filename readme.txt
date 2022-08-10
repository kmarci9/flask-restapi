JOB Interview sample task

The whole task, with a backend and frontend running in the cloud
web application that is capable of running on the initial
vector sets (image embeddings), save them, re-cluster them
(grouping) and display the new clusters (groups).

Create an application that can use REST API to
receive properly formatted vector sets (POST request) and
to perform the re-clustering.
The results of the last re-clustering, i.e. the final
final vector sets (POST response).
In addition, it is necessary to store in a database the initial and final
and initial vector sets.
Test data
Also, part of the task is to validate the incoming data, e.g.
whether the group names are correct, or whether there is an empty set, etc.
In the case where the construction of the clustering algorithm is not part of the
tasks to be performed, we provide a ready-made solution, binary
which you will be able to use. The ready-made solution is Go
language.
Example of a properly formatted vector set:
{"group_1": [[R0,R1,R2,R3], [R4,R5,R6,R7]], "group_2": [[R8,R9,R10,R11]],
"group_3": [[R12,R13,R14,R15], [R16,R17,R18,R19]]}
where the number of vector sets is 3, the length of the vectors is 4 and each Ri is
is a real number.
The lengths of each vector must be equal, but any
lengths, and the naming of the groups ("group_N") is given in the example
should be followed as in the example.

This repo only contains the backend part.

step1: Project requires PYTHON 3.7.4+
step2: pip3 install -r requirements.txt
step3: run restapi -> python3 application.py

for testing try:
 klaszterezo_app_test/test.py
