# +-----------------------+
# | lab3_4 - Isaiah Grace |
# +-----------------------+

# Task 4 - fun with functions

def SayHello():
    print("Hello world")

SayHello()

def SayHelloTo(name):
    print(f"Hello {name}")

SayHelloTo("Zac")

def GetName():
    usr_name = input("What is your name? ")
    SayHelloTo(usr_name)
    return usr_name

print(GetName())

def SafeDivision(numA, numB):
    return None if numB == 0 else numA / numB

print(SafeDivision(3, 4))
