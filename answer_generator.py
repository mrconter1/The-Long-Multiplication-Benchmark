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
    
    print("\nMove from right-most column to left-most.\n")
    
    # Generate the dynamic addition breakdown
    columns = [0] * (len(a_digits) + 1)  # +1 to handle the carry at the last step
    
    # Store intermediate digit contributions for each column
    column_contributions = [[] for _ in range(len(columns))]
    
    for i, (product, shifted_product) in enumerate(intermediate_results):
        for j, digit in enumerate(str(shifted_product).zfill(6)[::-1]):  # reverse for column-wise addition
            columns[j] += int(digit)
            column_contributions[j].append(int(digit))
    
    carry = 0
    breakdown = []
    
    for i in range(len(columns)):
        total = columns[i] + carry
        carry, value = divmod(total, 10)
        breakdown.append((i + 1, column_contributions[i], value, carry))
    
    for i, (col, original, value, carry) in enumerate(breakdown):
        additions = " + ".join(map(str, original))
        carry_note = f"({carry} is carried)" if carry else ""
        print(f"Column {col}: {additions} = {value} {carry_note}")
    
    # Print the final result of this multiplication step
    final_result = sum(shifted_product for _, shifted_product in intermediate_results)
    print(f"\n{first_digit} * {a} = {final_result}\n")
    print(f"Step result: {final_result}")

generate_multiplication_steps(64369, 95689)