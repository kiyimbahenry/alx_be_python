# pattern_drawing.py
def main():
    size = int(input("Enter the size of the pattern: "))
    
    print(f"\nSquare pattern of size {size}:")
    row = 1
    while row <= size:
        for col in range(1, size + 1):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    main()
