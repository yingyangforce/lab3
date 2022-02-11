# +-----------------------+
# | lab3_5 - Isaiah Grace |
# +-----------------------+

# Task 5 - parsing if blocks

# Block A:
cash = 1.5
if int(cash) * 2.0 != int(cash * 2.0):
    print("The devil is in the details.")
# Won't print, int cast will cut off .5
# resulting in different calculations

# Block B:
temp = 40
if temp < 40:
    print("It is cold.")
elif temp < 80:
    print("It is mild.")
elif temp < 100:
    print("It is hot.")
else:
    print("It is unbearable.")
# Should print "It is mild"

# Block C:
def MyFunction(A, B):
    if A - B > 0:
        return A
    elif B - A > 0:
        return B

a = "defensive prompt"
b = 42
C = MyFunction(a, b) + 1
# Should crash due to type mixing
