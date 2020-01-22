# Ques 1

lis = "aneesh kumar"
print(len(lis))

"""-------------------------------------------------------------------------------------------"""

# Ques 2

i = input("Enter words with space:")
l = i.split()

m = 0
for n in range(len(l)):
    if len(l[n]) > m:
        m = len(l[n])
print(m)

"""--------------------------------------------------------------------------------------------------------------"""

# Ques 3

lis2 = ["barbarian", "pubg", "akm", "groza", "awm"]

for i in range(0,len(lis2), 2):
    lis2[i] = "#"

print(lis2)

"""--------------------------------------------------------------------------------------------------------------"""

# Ques 4

lis3 = []
lis4 = ["coc", "freefire"]

def empty(u):
    if len(u) == 0:
        print("List is empty")
    else:
        print("List is not empty")

empty(lis3)
empty(lis4)

"""---------------------------------------------------------------------------------------------------------------"""

# Ques 5

lis5 = ["nobita", "doraemon"]

lis6 = lis5[:]

print(lis6)
