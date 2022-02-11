# +-----------------------+
# | lab3_3 - Isaiah Grace |
# +-----------------------+

# Task 3 - to if or not to if

x = 3
x = 1 if x > 1 else x

#---

x = 19
print("Yes" if 20 > x > 10 else "No")

#---

x = 12
y = 12
z = 21

print("Correct" if y==z else "Incorrect" if y==x else "Inconclusive")

#--- 

x = 1
y = 2
z = 3
#                    XOR(x, y, z)
print("True" if (x!=y and x!=z and y!=z) else "False")

