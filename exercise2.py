import copy

empleados =[
["Pedro",["Python","SQL"]],
["Manolo",["Java","C++","JavaScript"]],
["Alejandro",["HTML","CSS","JavaScript"]]
]

deepCopy = copy.deepcopy(empleados)
shallowCopy = empleados.copy()
empleados[0][1].append("Docker")

deepCopy[2][1].append("Java")
newEmployee = ["Juan", ["Node.js", "redis"]]
print(newEmployee)
deepCopy.append(newEmployee)

print("Shallow: " + str(shallowCopy))
print("Deep: " + str(deepCopy))