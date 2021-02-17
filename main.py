################### Scope ####################

enemies = 1
player_health = 10

def increase_enemies():
  enemies = 2 #This line does not change the global variable
  print(f"enemies inside function: {enemies}")

def add_enemies():
  global enemies #This is how to change global variable
  enemies +=1
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

add_enemies()

print(f"enemies outside function: {enemies}")

# If statement does not create local scope. Def does. Variables created under if statements are global variables. 

#Global Contestants 

PI = 3.14159
URL = "https://www.google.com"

#all capitalized for constants 


# What you knowThese are questions you got right on the first try.
# What will be printed in the console when the following code is run?DO NOT run the code, just pretend to be a computer. def a_function(a_parameter): a_variable = 15 return a_parameter a_function(10) print(a_variable)
# What will be printed in the console when the code is run?DO NOT run the code, just pretend to be a computer.i = 50 def foo(): i = 100 return i foo() print(i)
# What will be printed in the console when the following code is run?DO NOT run the code, just pretend to be 