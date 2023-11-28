#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c

# Test case
if __name__ == "__main__":
    # You can add more test cases if needed
    result = magic_calculation(1, 2, 3)
    print(result)
