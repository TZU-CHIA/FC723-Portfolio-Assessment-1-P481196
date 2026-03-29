
class EuclideanAlgorithm:

    def __init__(self):
        """
        Initialization function
        """
        pass

    def find_gcd(self, A, B):
        """
        Function to compute GCD using recursion
        GCD: Greatest Common Divisor
        """
        # Ensure A is greater than B
        if A < B:
            A, B = B, A

        # Base case: when remainder is 0
        if A == 0:
            return B
        if B == 0:
            return A

        # Compute reminder and use recursion compute GCD
        R = A % B
        GCD = self.find_gcd(B, R)
        return GCD

    def check_relative_prime(self):
        """
        Function to check relative prime numbers
        """
        # Get the two numbers that user want to check if they are relative prime
        A = int(input("Please enter first number: "))
        B = int(input("Please enter second number: "))

        # Get and show GCD
        GCD = self.find_gcd(A, B)
        print(f"The GCD of {A} and {B} is {GCD}.")

        # If GCD is 1, they are relative prime
        if GCD == 1:
            print(f"{A} and {B} are relative prime.")
        # If GCD is not 1, they are not relative prime
        else:
            print(f"{A} and {B} are not relative prime numbers.")


# Instantiate the class
system = EuclideanAlgorithm()
# Call the function
system.check_relative_prime()