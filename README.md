# Piepy
This program is made for calculate π

# Install
- install mathod (recommend)
``` python
      pip install mpmath
```

# Quick Start
- All code can be found in the example
- Download piepy.exe and start it
- Enter numbers of demical places to calculate π (recommend not over 1000000)
- Result is save at pi_value.txt


Source Code
``` python
      from mpmath import mp

def calculate_pi(precision):
    # Set precision for mpmath
    mp.dps = precision  # Set the number of decimal places

    pi_value = mp.pi  # Calculate the value of π
    return pi_value

def save_to_file(pi_value, precision):
    # Save the value of π to a text file
    with open('pi_value.txt', 'w') as file:
        file.write(f"The value of π calculated to {precision} decimal places is:\n")
        file.write(str(pi_value))

if __name__ == "__main__":
    try:
        precision = int(input("Enter the number of decimal places to calculate π: "))
        if precision < 1:
            print("The number of decimal places must be greater than 1.")
        else:
            pi_value = calculate_pi(precision)
            print(f"The value of π: {pi_value}")
            save_to_file(pi_value, precision)
            print("The value of π has been saved to 'pi_value.txt'.")
    except ValueError:
        print("Please enter a valid integer.")
```
