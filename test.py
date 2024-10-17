def amdahl_law(S, N):
    # S is the serial portion, N is the number of processing cores
    return 1 / (S + (1 - S) / N)

# Taking user inputs for S and N
S = float(input("Enter the serial portion (S) of the workload (e.g., 0.25 for 25%): "))
N = int(input("Enter the number of processing cores (N): "))

# Calculating speedup
speedup = amdahl_law(S, N)
print(f"Speedup with S={S} and N={N} cores is: {speedup}")