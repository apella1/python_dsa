# for loops
nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    if num % 3 == 0:
        print(num)

# for loops with range
for i in range(3, 9):
    print(i)

# nested for loops
teams = [["Elly", "Chris"], ["John", "Matt"],
         ["Scott", "Wes"], ["Huberman", "Lex"]]


for team in teams:
    for name in team:
        if name.startswith("J"):
            print(name)


for i in range(3):
    print(teams)

# while loop

number = 8

while number < 18:
    print("Nice!")
    number += 1
