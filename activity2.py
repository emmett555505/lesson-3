#assigning different variables
name = "Emmett"
age = 15
is_student = True
weight = 120.5

#printing different variables and their data type
print("name :", name)
print("data type of name i", type(name))

print("age :", age)
print("data ype of age is", type(age))

print("is_student :", is_student)
print("data type of is_student is", type(is_student))

print("weight :", weight)
print("data type of weight", type(weight))

#type casting to convert the datatype of variables
print("\n after type casting....")
age = str(age)
print(age)
print("data type of age is", type(age))
weight = int(weight)
print(weight)
print("data type of weight is", type(weight))