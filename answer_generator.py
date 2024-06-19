def generate_multiplication_steps(a, b):
    print("Calculating: ", a, "*", b)
    
    a_str = str(a)
    b_str = str(b)
    
    # Take the first rightmost digit of b
    first_digit = int(b_str[-1])
    
    # Calculate the product of a and the first digit of b
    current_step = first_digit * a
    
    print()
    print(f"Step 1: Calculate for the 1st digit from the right ({first_digit}):")
    print()
    print(f"{first_digit} * {a} = ?")
    print()
    
    a_digits = list(map(int, reversed(a_str)))
    intermediate_results = []
    
    for i, digit in enumerate(a_digits):
        product = first_digit * digit
        shifted_product = product * (10 ** i)
        intermediate_results.append((product, shifted_product))
    
    # Print the detailed breakdown
    for i, (product, shifted_product) in enumerate(intermediate_results):
        shift_note = "(shift one left)" if i > 0 else ""
        print(f"{first_digit} * {a_digits[i]} = {shifted_product:06d} {shift_note}")

generate_multiplication_steps(64369, 95689)