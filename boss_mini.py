# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Security Audit: This variable and the cheat logic must be removed to close the backdoor vulnerability.
# SECRET_CODE = "ADMIN_ACCESS_2025"

# adding initial hit points to reference in overhealing prevention logic
p_hp_init = 50
b_hp_init = 50
p_hp = p_hp_init
b_hp = b_hp_init

# Attack Logic: this function was missing write new value to b_hp. subtracting 10 to match the output message
def attack():
  global b_hp
    b_hp -= 10
    if b_hp < 0: b_hp = 0
    print("You deal 10 damage!")

# Healing Guardrails: this function was missing boundaries preventing player from over-healing and healing while dead
def heal():
  global p_hp
  if p_hp <= 0:
    print ("You cannot heal when dead.")
    return
  p_hp += 20
  if p_hp > p_hp_init: p_hp = p_hp_init
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# Win Condition: modifying loop if statement to display victory message when appropriate
# I'm also adding a loss condition
while True:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    # TO DO: Implement more secure credential check.
    #if input("Code: ") == SECRET_CODE:
    if False:
      b_hp = 0
    else:
      print("You don't have access to cheats.")
    
  if b_hp <= 0:
    print("Victory!")
    break
  else:
    p_hp -= 10
    if p_hp <= 0:
      print("You Lose!")
      break

print("Game Over!")
