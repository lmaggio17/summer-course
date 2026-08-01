########################################################################################################################

# <!-- -- - Write a function `pizzas_needed(people, slices_per_person, slices_per_pizza)` that calculates and returns how many whole pizzas to order (always round **up** — you never want to run short!).
# - Write another function `leftover_slices(people, slices_per_person, slices_per_pizza` that returns how many slices will be leftover.
# - Use input statements to ask how many guests, slices per person, and slices per pizza.
# - Using your user defined functions, print the PARTY SUMMARY shown below. --> 
# import math

# def pizzas_needed(people, slices_per_person, slices_per_pizza):
#     total_slices=people*slices_per_person
#     pizzas=total_slices/slices_per_pizza
#     pizzas=math.ceil(pizzas)
#     return pizzas

# def leftover_slices(people, slices_per_person, slices_per_pizza):
#     total_slices_needed=people*slices_per_person
#     pizzas=pizzas_needed(people, slices_per_person, slices_per_pizza)
#     total_slices_ordered=pizzas*slices_per_pizza
#     leftovers = total_slices_ordered - total_slices_needed
#     return leftovers

# people=int(input("How many people will be attending? "))
# slices_per_person=int(input("How many slices will be provided to each person? "))
# slices_per_pizza=int(input("How many slices are in a pie? "))
# pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza)
# leftovers = leftover_slices(people, slices_per_person, slices_per_pizza)

# print("PARTY SUMMARY")
# print(f"Guests: {people}")
# print(f"Slices per person: {slices_per_person}")
# print(f"Pizzas needed: {pizzas}")
# print(f"Leftover slices: {leftovers}")

########################################################################################################################

# - Write a function `o2_status(level)` that returns:
#   - `"CRITICAL"` if level < 15
#   - `"LOW"` if level is 15–18
#   - `"NORMAL"` if level is 19–23
#   - `"HIGH"` if level > 23
# - You are given the following hourly O2 readings (as a percentage):
 
def o2_status(level):
    if level <15:
        return "CRITICAL"
    elif level <=18:
        return "LOW"
    elif level <=23:
        return "NORMAL"
    else:
        return "HIGH"

readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21,26]

normal_count=0
low_count=0
critical_count=0
high_count=0
# - Use a `for` loop to process each reading, call your function, and print the hour and status.
for hour, reading in enumerate(readings, start=1):
    status=o2_status(reading)
    print(f"Hour{hour}: {reading}% - {status}")
    if status== "NORMAL":
        normal_count+=1
    elif status == "LOW":
        low_count+=1
    elif status== "HIGH":
        high_count+=1
    elif status == "CRITICAL":
        critical_count+=1
        print("*** ALERT: TAKE ACTION IMMEDIATELY ***")

print("\n*** Status Summary ***")
print(f"Normal: {normal_count} hours")
print(f"Low: {low_count} hours")
print(f"Critical: {critical_count} hours")
print(f"High: {high_count} hours")

########################################################################################################################

## Problem 3 — RPG Character Battle ⚔️
 
# *You're simulating a turn-based battle between a hero and a monster. Each turn, the hero attacks the monster and then the monster strikes back — until one of them runs out of HP.*
 
 
# - Write a function `attack(defender_hp, damage)` that subtracts damage from defender HP and returns the new HP (minimum 0).

def attack(defender_hp, damage):
       new_hp = defender_hp - damage
       if new_hp<0:
           new_hp=0
       return new_hp
# - Write a function `is_alive(hp)` that returns `True` if HP > 0.
def is_alive(hp):
    if hp>0:
        return True
    else:
        return False

hero_hp = 100
monster_hp = 90
round_number = 1
# - Use a `while` loop to simulate the battle. Each round:
while is_alive(hero_hp) and is_alive(monster_hp):
    monster_hp=attack(monster_hp, 18)
    if is_alive(monster_hp):
        hero_hp=attack(hero_hp, 12)
    print(f"Round {round_number}: Hero HP: {hero_hp} Monster HP: {monster_hp}")
    round_number += 1

if is_alive(hero_hp):
    print("Hero Wins! The monster has been defeated.")
else:
    print("Monster Wins! The hero has been defeated.")

########################################################################################################################

# # Define a function for each of the following checks — each should return `True` (cleared) or `False` (denied):

# def check_fitness(score):
#     if score >= 70:
#         return True
#     else:
#         return False
 
# def check_rank(rank):
# #     """Cleared if rank is 'Corporal', 'Sergeant', or 'Lieutenant'."""
#     if rank in ["Corporal", "Sergeant", "Lieutenant"]:
#         return True
#     else:
#         return False
 
# def check_service_years(years):
# #     """Cleared if years >= 2."""
#     if years >= 2:
#         return True
#     else:
#         return False
 
# # Then write a main program that:
# # - Collects the soldier's name, fitness score, rank, and years of service using `input()`.
# soldier_name = input("Please provide soldiers name. ")
# soldier_fitness = int(input("Please provide soldiers fitness score. "))
# soldier_rank = input("Please provide soldiers rank. ")
# soldier_tis = int(input("Please provide soldiers TIS. "))

# # - Uses a `for` loop to run all three checks and store each result.
# checks = [
#     check_fitness(soldier_fitness),
#     check_rank(soldier_rank),
#     check_service_years(soldier_tis)
# ]

# results =[]
# for check in checks:
#     results.append(check)
# # - Uses conditionals to determine overall clearance: the soldier is cleared only if **all three checks pass**.
# if all(results):
#     final_status = "CLEARED FOR MISSION"
# else:
#     final_status = "DENIED"
# # - Prints a full clearance report showing each individual check and the final decision.
 
# fitness_status = "PASS" if results[0] else "FAIL"
# rank_status = "PASS" if results[1] else "FAIL"
# service_status = "PASS" if results[2] else "FAIL"

# print("\n=== MISSION CLEARANCE REPORT ===")
# print(f"Soldier: {soldier_name}")
# print()
# print(f"Fitness check:  {fitness_status}")
# print(f"Rank check:     {rank_status}")
# print(f"Service check:  {service_status}")
# print()
# print(f"FINAL STATUS: {final_status}.")

########################################################################################################################
# *The season is over and it's time to crunch the numbers. Write a program that processes a list of athletes and generates a leaderboard.*
 
athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
 ]

# - Write a function `goals_per_game(goals, games)` that returns goals per game rounded to 2 decimal places. Return `0.0` if games played is 0.
def goals_per_game(goals, games):
    if games == 0:
        return 0.0
    gpg=round(goals/games, 2)
    return gpg

# - Write a function `mvp_candidate(gpg)` that returns `True` if the rate is 0.25 or higher.
def mvp_candidate(gpg):
    if gpg >= .25:
        return True
    else:
        return False
# - Use a `for` loop to process each athlete, call both functions, and print a formatted leaderboard. Use a conditional to mark MVP candidates with a `*`.
print("\n===SEASON LEADERBOARD===")
for name, games, goals in athletes:
    gpg=goals_per_game(goals, games)
    is_mvp=mvp_candidate(gpg)
    if is_mvp:
        marker = "*"
    else:
        marker = ""

    print("Athlete       Games        Goals        GPG         MVP")
    print(f"{name},     {games},     {goals},       {gpg},      {marker}")
    

# - After the loop, print the name of the top scorer (most total goals).
top_scorer = ""
most_goals = -1
if goals > most_goals:
    most_goals = goals
    top_scorer = name
    print(f"\nTop scorer: {top_scorer} ({most_goals} goals)")
# **Expected output:**
 
# ```
# === SEASON LEADERBOARD ===
#   Athlete       Games   Goals   GPG     MVP?
#   ------------------------------------------
#   Jordan        82      15      0.18
#   Patel         78      22      0.28    *
#   Okonkwo       90      18      0.20
#   Li            65      9       0.14
#   Reyes         88      31      0.35    *
#   Fischer       72      14      0.19
 
# Top scorer: Reyes (31 goals)