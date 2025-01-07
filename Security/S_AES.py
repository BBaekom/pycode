"""REFERENCE"""
# https://github.com/mayank-02/simplified-aes
# https://sandilands.info/sgordon/teaching/reports/simplified-aes-example.pdf
# https://www.nku.edu/~christensen/simplified%20AES.pdf

sBox = [
    0x9, 0x4, 0xA, 0xB,
    0xD, 0x1, 0x8, 0x5,
    0x6, 0x2, 0x0, 0x3,
    0xC, 0xE, 0xF, 0x7
]

sBoxI = [
    0xA, 0x5, 0x9, 0xB,
    0x1, 0x7, 0x8, 0xF,
    0x6, 0x0, 0x2, 0x3,
    0xC, 0x4, 0xD, 0xE
]

def sub_word(word):
    return (sBox[(word >> 4)] << 4) + sBox[word & 0x0F]

def rot_word(word):
    return ((word & 0x0F) << 4) + ((word & 0xF0) >> 4)

def key_expansion(key):
    Rcon1 = 0x80
    Rcon2 = 0x30

    w = [None] * 6
    w[0] = (key & 0xFF00) >> 8
    w[1] = key & 0x00FF
    w[2] = w[0] ^ (sub_word(rot_word(w[1])) ^ Rcon1)
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ (sub_word(rot_word(w[3])) ^ Rcon2)
    w[5] = w[4] ^ w[3]

    return (
        int_to_state((w[0] << 8) + w[1]),
        int_to_state((w[2] << 8) + w[3]),
        int_to_state((w[4] << 8) + w[5]),
    )

def gf_mult(a, b):
    product = 0
    a = a & 0x0F
    b = b & 0x0F
    while a and b:
        if b & 1:
            product ^= a
        a = a << 1
        if a & (1 << 4):
            a = a ^ 0b10011
        b = b >> 1
    return product & 0xF

def int_to_state(n):
    return [n >> 12 & 0xF, (n >> 4) & 0xF, (n >> 8) & 0xF, n & 0xF]

def state_to_int(m):
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]

def add_round_key(s1, s2):
    return [i ^ j for i, j in zip(s1, s2)]

def sub_nibbles(sbox, state):
    return [sbox[nibble] for nibble in state]

def shift_rows(state):
    return [state[0], state[1], state[3], state[2]]

def mix_columns(state):
    return [
        state[0] ^ gf_mult(4, state[2]),
        state[1] ^ gf_mult(4, state[3]),
        state[2] ^ gf_mult(4, state[0]),
        state[3] ^ gf_mult(4, state[1]),
    ]

def inverse_mix_columns(state):
    return [
        gf_mult(9, state[0]) ^ gf_mult(2, state[2]),
        gf_mult(9, state[1]) ^ gf_mult(2, state[3]),
        gf_mult(9, state[2]) ^ gf_mult(2, state[0]),
        gf_mult(9, state[3]) ^ gf_mult(2, state[1]),
    ]

def encrypt(plaintext, pre_round_key, round1_key, round2_key):
    state = add_round_key(pre_round_key, int_to_state(plaintext))
    state = mix_columns(shift_rows(sub_nibbles(sBox, state)))
    state = add_round_key(round1_key, state)
    state = shift_rows(sub_nibbles(sBox, state))
    state = add_round_key(round2_key, state)
    return state_to_int(state)

def decrypt(ciphertext, pre_round_key, round1_key, round2_key):
    state = add_round_key(round2_key, int_to_state(ciphertext))
    state = sub_nibbles(sBoxI, shift_rows(state))
    state = inverse_mix_columns(add_round_key(round1_key, state))
    state = sub_nibbles(sBoxI, shift_rows(state))
    state = add_round_key(pre_round_key, state)
    return state_to_int(state)

key = 0b1010011100111011
plaintext = 0b0110111101101011
expected_ciphertext = 0b0000011100111000

pre_round_key, round1_key, round2_key = key_expansion(key)

ciphertext = encrypt(plaintext, pre_round_key, round1_key, round2_key)
print(f"Ciphertext: {format(ciphertext, '#018b')} (expected: {format(expected_ciphertext, '#018b')})")

decrypted_plaintext = decrypt(ciphertext, pre_round_key, round1_key, round2_key)
print(f"Decrypted Plaintext: {format(decrypted_plaintext, '#018b')} (original: {format(plaintext, '#018b')})")

assert ciphertext == expected_ciphertext, "암호화 결과가 예상 값과 다릅니다."
assert decrypted_plaintext == plaintext, "복호화 결과가 원래 평문과 다릅니다."


# def differential_attack(plaintext_pairs, ciphertext_pairs):
#     candidate_keys = []

#     for key_guess in range(2**16):
#         valid_key = True
#         for (p1, p2), (c1, c2) in zip(plaintext_pairs, ciphertext_pairs):
#             d1 = decrypt(c1, int_to_state(key_guess), int_to_state(key_guess), int_to_state(key_guess))
#             d2 = decrypt(c2, int_to_state(key_guess), int_to_state(key_guess), int_to_state(key_guess))

#             if (d1 ^ d2) != (p1 ^ p2):
#                 valid_key = False
#                 break

#         if valid_key:
#             candidate_keys.append(key_guess)

#     print("Candidate Keys:")
#     for key in candidate_keys:
#         print(format(key, '016b'))


# plaintext_pairs = [
#     (0b0110111101101011, 0b0110111101101000),
#     (0b1001100101010101, 0b1001100101010111),
# ]
# ciphertext_pairs = [
#     (encrypt(p1, pre_round_key, round1_key, round2_key), encrypt(p2, pre_round_key, round1_key, round2_key))
#     for p1, p2 in plaintext_pairs
# ]

# differential_attack(plaintext_pairs, ciphertext_pairs)
