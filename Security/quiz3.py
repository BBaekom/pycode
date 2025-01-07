from sympy import mod_inverse

# Given values
p = 137
d_A = 3
G = (21, 6)
a = 4

# Function to perform elliptic curve point addition
def point_addition(P, Q, a, p):
    x1, y1 = P
    x2, y2 = Q
    
    if P == Q:  # Point doubling case
        m = (3 * x1**2 + a) * mod_inverse(2 * y1, p) % p
    else:  # General point addition case
        m = (y2 - y1) * mod_inverse(x2 - x1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

# Step 1: Calculate 2G
G2 = point_addition(G, G, a, p)

# Step 2: Calculate 3G = 2G + G
Q_A = point_addition(G2, G, a, p)

# Extracting the coordinates of Q_A
print(Q_A)