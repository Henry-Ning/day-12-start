################### Scope ####################

enemies = 1
player_health = 10

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# If statement does not create local scope. Def does. Variables created under if statements are global variables. 