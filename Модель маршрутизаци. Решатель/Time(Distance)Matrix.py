import json

a = 25          
matrix = [0] * a 
for i in range(a): 
    matrix[i] = [0] * a
#------------------
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 0-9 to 10-19.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 0-9 to 20-24.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 0-9 to 0-10.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 10-19 to 0-9.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 10-19 to 10-19.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 10-19 to 20-24.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 20-24 to 0-9.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 20-24 to 10-19.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
with open("C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\from 20-24 to 20-24.json", "r") as my_file:
    routing_json = my_file.read()

routing = json.loads(routing_json)
routing = routing["routes"]
for rout in routing:
  matrix[rout["source_id"]][rout["target_id"]]=rout["duration"]
# ------------------|
print(max(matrix))

file = open('C:\\Users\\Kortald\\Desktop\\Ответы сервера 2Гис\\routematrix.txt', 'r+')
for column in matrix:
    file.write(str(column))