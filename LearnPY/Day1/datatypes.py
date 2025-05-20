# keywords --> predefined special words with certain meaning on program
# Identifiers --> what you can ann can not use as a variable

age = 65
print(age)
#age gets rewritten
age = 22
print(age)

# Formatting

user_input = int(input("Enter number: "))
print("Printing the Table", user_input)

print(f"{user_input}*1={user_input*1}")
print(f"{user_input}*2={user_input*2}")
print(f"{user_input}*5={user_input*5}")
print(f"{user_input}*10={user_input*10}")

# Variable
a, b, c = 6, 9, 69
print(a, b, c) 

#python is a dynamic type language

PI = 3.1415 #constant
print(PI)
# self identify data type
x = 20
y = x
y =11
z = y 
print(x)
print(y)
print(z)
# String
name = "Duck"
print(name, type(name))
print("Length:", len(name))
print(name[0])

#boolean
nepal_developed = False
usa_developed = True
print("Is Nepal developed: ", nepal_developed)
print("Is USA developed: ", usa_developed)

# Complex number
cn = 10+69j
# j = sqrt of -1
print("Complex Number:", cn)