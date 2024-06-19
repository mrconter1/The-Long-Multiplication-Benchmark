def generate_multiplication_steps(a, b):
    print("Calculating:\n")
    print_standing_form(a, b)
    
    a_str = str(a)
    b_str = str(b)
    
    intermediate_total_results = []
    overall_columns = []
    
    for idx, digit_char in enumerate(reversed(b_str)):
        digit = int(digit_char)
        
        # Calculate the product of a and the current digit of b
        print_step_intro(digit, a, idx)
        
        a_digits = list(map(int, reversed(a_str)))
        intermediate_results = calculate_intermediate_results(digit, a_digits, idx)
        
        print_intermediate_results(intermediate_results, digit, a_digits, idx)
        
        # Summarize after each step
        intermediate_total_results.append(intermediate_results)
        
        # Generate column contributions and breakdown for the current step
        current_column_contributions, current_columns = generate_column_contributions(intermediate_total_results)
        
        current_breakdown = calculate_breakdown(current_columns, current_column_contributions)
        
        print("\nIntermediate column summary after this step:\n")
        print_breakdown(current_breakdown)
        
        step_result = calculate_final_result(intermediate_results)
        print(f"\nStep {idx + 1} result: {step_result}\n")
        
    print("\nSum up all steps from right-most column to left-most.\n")
    
    total_column_contributions, total_columns = generate_total_column_contributions(intermediate_total_results)
    
    total_breakdown = calculate_breakdown(total_columns, total_column_contributions)
    
    print_breakdown(total_breakdown)
    
    final_result = calculate_final_result_from_columns(total_columns)
    
    print(f"\nFinal result: {final_result}\n")

def print_standing_form(a, b):
    a_str = str(a)
    b_str = str(b)
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    print(f"    {a_str}")
    print(f"x   {b_str}")
    print("-------------")

def print_step_intro(digit, a, idx):
    print()
    print(f"Step {idx + 1}: Calculate for the {idx + 1}st digit from the right ({digit}):")
    print()
    print(f"{digit} * {a} = ?")
    print()

def calculate_intermediate_results(digit, a_digits, idx):
    intermediate_results = []
    for i, a_digit in enumerate(a_digits):
        product = digit * a_digit
        shifted_product = product * (10 ** (i + idx))
        intermediate_results.append((product, shifted_product))
    return intermediate_results

def print_intermediate_results(intermediate_results, digit, a_digits, idx):
    for i, (product, shifted_product) in enumerate(intermediate_results):
        shift_note = f"(shift whole number {idx + 1} step{'s' if idx > 0 else ''} left)"
        print(f"{digit} * {a_digits[i]} = {shifted_product} {shift_note}")

def generate_column_contributions(intermediate_total_results):
    max_length = max(len(str(shifted_product)) for results in intermediate_total_results for _, shifted_product in results)
    columns = [0] * max_length
    column_contributions = [[] for _ in range(max_length)]
    
    for results in intermediate_total_results:
        for i, (product, shifted_product) in enumerate(results):
            shifted_str = str(shifted_product).zfill(max_length)[::-1]
            for j, digit in enumerate(shifted_str):
                columns[j] += int(digit)
                column_contributions[j].append(int(digit))
    
    return column_contributions, columns

def generate_total_column_contributions(intermediate_total_results):
    max_length = max(len(str(shifted_product)) for results in intermediate_total_results for _, shifted_product in results)
    total_columns = [0] * max_length
    total_column_contributions = [[] for _ in range(max_length)]
    
    for results in intermediate_total_results:
        for i, (product, shifted_product) in enumerate(results):
            shifted_str = str(shifted_product).zfill(max_length)[::-1]
            for j, digit in enumerate(shifted_str):
                total_columns[j] += int(digit)
                total_column_contributions[j].append(int(digit))
    
    return total_column_contributions, total_columns

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

def calculate_final_result_from_columns(columns):
    final_result = 0
    for i, column in enumerate(columns):
        final_result += column * (10 ** i)
    return final_result

# Example usage
generate_multiplication_steps(423, 314)