# multiplication_table.py
# Generates multiplication table using for loop

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate and print multiplication table using for loop
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

# Run the program
if __name__ == "__main__":
    main()
