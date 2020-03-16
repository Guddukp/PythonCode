import json
filename='num.json'
with open(filename)as file:
    my_list=json.load(file)
print(my_list)
