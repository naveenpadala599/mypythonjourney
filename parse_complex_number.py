def parse_complex(s):
    """
    Converts a string like '3+4j' or '5 - 2j' into a complex number.
    Strips spaces and validates the format.
    """
    try:
        # Remove spaces and convert to complex
        s_clean = s.replace(" ", "")
        return complex(s_clean)
    except ValueError:
        raise ValueError("Invalid complex number format. Use format like '3+4j' or '5-2j'.")

# Take input from user
user_input = input("Enter a complex number (e.g., 3+4j or 5-2j): ")

try:
    cnum = parse_complex(user_input)
    print(f"Parsed complex number: {cnum}")
    print(f"Real part: {cnum.real}")
    print(f"Imaginary part: {cnum.imag}")
    print(f"Modulus: {abs(cnum)}")
except ValueError as ve:
    print("Error:", ve)
