
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

name = lower_case_name1 + lower_case_name2

T_count = name.count("t")
R_count = name.count("r")
U_count = name.count("u")
E_count = name.count("e")

L_count = name.count("l")
O_count = name.count("o")
V_count = name.count("v")
E_count = name.count("e")

print(f"T occurs {T_count} times")
print(f"R occurs {R_count} times")
print(f"U occurs {U_count} times")
print(f"E occurs {E_count} times")

true_count = T_count + R_count + U_count + E_count
print(f"Total = {true_count}")

print(f"L occurs {L_count} times")
print(f"O occurs {O_count} times")
print(f"V occurs {V_count} times")
print(f"E occurs {E_count} times")

love_count = L_count + O_count + V_count + E_count
print(f"Total = {love_count}")

Love_Score = str(true_count) + str(love_count)
print(f"Love Score = {Love_Score}")

if 10 > int(Love_Score) > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos")
elif 40 >= int(Love_Score) <= 50:
    print(f"Your score is {Love_Score}, you are alright together")
else:
    print(f"Your score is {Love_Score}")



