from mpmath import mp

def calculate_pi(precision):
    # Set precision for mpmath
    mp.dps = precision  # Set the number of decimal places

    pi_value = mp.pi  # Calculate the value of π
    return pi_value

if __name__ == "__main__":
    try:
        precision = int(input("Enter the number of decimal places to calculate π: "))
        if precision < 1:
            print("The number of decimal places must be greater than 1.")
        else:
            pi_value = calculate_pi(precision)
            print(f"The value of π: {pi_value}")
    except ValueError:
        print("Please enter a valid integer.")
