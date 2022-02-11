# +-----------------------+
# | lab3_2 - Isaiah Grace |
# +-----------------------+

# Task 2 - parsing bools

# 1: not (True and not False)
#
# Expected eval: False
print(not (True and not False))

# 2: A = True
#    B = False
#    C = True
#    (B or (not A)) and C
#
# Expected eval: False
A = True
B = False
C = True
print((B or (not A)) and C)

# 3: A = True
#    B = -1
#    bool(int(A) + B)
# 
# Expected eval: False
F = True
G = -1
print(bool(int(F) + G))

