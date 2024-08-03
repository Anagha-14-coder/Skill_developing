def print_pyramid_with_space(rows):
    # Outer loop to handle number of rows
    for i in range(0, rows):
        # Inner loop to handle spaces
        for j in range(0, rows-i-1):
            print(end=" ")

        # Inner loop to handle number of stars
        for j in range(0, i+1):
            # Printing stars with space
            print("* ", end="")
        
        # Moving to the next line after each row
        print()

# Example usage:
print_pyramid_with_space(5)
