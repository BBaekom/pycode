# Given parameters
p = 97  # Prime number for modulo operations
d_A = 3  # Private key
R = (80, 87)  # Ciphertext point R
C = 39  # Ciphertext value
a = 2  # Coefficient a in the elliptic curve equation

# Function for point addition
def point_add(P, Q, a, p):
    if P == Q:  # Point doubling
        lam = (3 * P[0]**2 + a) * pow(2 * P[1], -1, p) % p
    else:  # Point addition
        lam = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p) % p

    x_r = (lam**2 - P[0] - Q[0]) % p
    y_r = (lam * (P[0] - x_r) - P[1]) % p
    return (x_r, y_r)

# Function for scalar multiplication
def scalar_mult(k, P, a, p):
    R = None  # Start with the identity element
    Q = P

    while k:
        if k % 2:  # If k is odd
            R = Q if R is None else point_add(R, Q, a, p)
        Q = point_add(Q, Q, a, p)  # Double the point
        k //= 2

    return R

# Step 1: Calculate S = d_A * R
S = scalar_mult(d_A, R, a, p)

# Step 2: Calculate modular inverse of S_x
S_x_inverse = pow(S[0], -1, p)

# Step 3: Calculate M
M = (C * S_x_inverse) % p

print((S, M))