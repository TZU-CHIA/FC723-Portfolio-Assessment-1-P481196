def find_gcd(A,B):
    if A < B:
        A, B = B, A
    if A == 0:
        return B
    if B == 0:
        return A
    R = A % B
    GCD = find_gcd(B, R)
    return GCD

def check_relative_prime(A, B):
    GCD = find_gcd(A, B)
    print(f"The GCD of {A} and {B} is {GCD}.")
    if GCD == 1:
        print(f"{A} and {B} are relative prime.")
    else:
        print(f"{A} and {B} are not relative prime numbers.")

# Call the function
check_relative_prime(88, 99)