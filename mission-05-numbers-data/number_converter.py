# number_converter.py
# A simple decimal to binary and hexadecimal converter

def main():
    print("=== Decimal Number Converter ===")
    user_input = input("Enter a positive decimal integer: ")
    decimal_number = int(user_input)
    
    binary_value = bin(decimal_number)
    hex_value = hex(decimal_number)
    
    print(f"Decimal:     {decimal_number}")
    print(f"Binary:      {binary_value}")
    print(f"Hexadecimal: {hex_value}")

if __name__ == "__main__":
    main()
