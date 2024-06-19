def generate_multiplication_steps(a, b):
    print("Calculating:\n")
    print_standing_form(a, b)
    
    a_str = str(a)
    b_str = str(b)
    
    # Take the first rightmost digit of b
    first_digit = int(b_str[-1])
    
    # Calculate the product of a and the first digit of b
    print_step_intro(first_digit, a)
    
    a_digits = list(map(int, reversed(a_str)))
    intermediate_results = calculate_intermediate_results(first_digit, a_digits)
    
    print_intermediate_results(intermediate_results, first_digit, a_digits)
    
    print("\nMove from right-most column to left-most.\n")
    
    column_contributions, columns = generate_column_contributions(intermediate_results, len(a_digits))
    
    breakdown = calculate_breakdown(columns, column_contributions)
    
    print_breakdown(breakdown)
    
    final_result = calculate_final_result(intermediate_results)
    
    print(f"\n{first_digit} * {a} = {final_result}\n")
    print(f"Step result: {final_result}")

def print_standing_form(a, b):
    a_str = str(a)
    b_str = str(b)
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    print(f"    {a_str}")
    print(f"x   {b_str}")
    print("-------------")

def print_step_intro(first_digit, a):
    print()
    print(f"Step 1: Calculate for the 1st digit from the right ({first_digit}):")
    print()
    print(f"{first_digit} * {a} = ?")
    print()

def calculate_intermediate_results(first_digit, a_digits):
    intermediate_results = []
    for i, digit in enumerate(a_digits):
        product = first_digit * digit
        shifted_product = product * (10 ** i)
        intermediate_results.append((product, shifted_product))
    return intermediate_results

def print_intermediate_results(intermediate_results, first_digit, a_digits):
    for i, (product, shifted_product) in enumerate(intermediate_results):
        shift_note = "(shift one left)" if i > 0 else ""
        print(f"{first_digit} * {a_digits[i]} = {shifted_product} {shift_note}")

def generate_column_contributions(intermediate_results, num_digits):
    # Find the length of the longest shifted product
    max_length = max(len(str(shifted_product)) for _, shifted_product in intermediate_results)
    columns = [0] * max_length
    column_contributions = [[] for _ in range(max_length)]
    
    for i, (product, shifted_product) in enumerate(intermediate_results):
        shifted_str = str(shifted_product).zfill(max_length)[::-1]  # reverse for column-wise addition
        for j, digit in enumerate(shifted_str):
            columns[j] += int(digit)
            column_contributions[j].append(int(digit))
    
    return column_contributions, columns

def calculate_breakdown(columns, column_contributions):
    carry = 0
    breakdown = []
    
    for i in range(len(columns)):
        total = columns[i] + carry
        carry, value = divmod(total, 10)
        breakdown.append((i + 1, [d for d in column_contributions[i] if d != 0], value, carry))
    
    return breakdown

def print_breakdown(breakdown):
    for i, (col, original, value, carry) in enumerate(breakdown):
        if original:
            additions = " + ".join(map(str, original))
        else:
            additions = "0"
        carry_note = f"({carry} is carried)" if carry else ""
        print(f"Column {col}: {additions} = {value} {carry_note}")

def calculate_final_result(intermediate_results):
    return sum(shifted_product for _, shifted_product in intermediate_results)

# Example usage
generate_multiplication_steps(643213213369, 953213213689)