import random

def generate_multiplication_steps(a, b):
    result_string = []
    
    def print_to_result(*args):
        result_string.append(" ".join(map(str, args)))
    
    print_to_result("Calculating:\n")
    print_standing_form(a, b, print_to_result)
    
    a_str = str(a)
    b_str = str(b)
    
    intermediate_total_results = []
    step_results = []
    
    for idx, digit_char in enumerate(reversed(b_str)):
        digit = int(digit_char)
        
        print_step_intro(digit, a, idx, print_to_result)
        
        a_digits = list(map(int, reversed(a_str)))
        intermediate_results = calculate_intermediate_results(digit, a_digits, idx)
        
        print_intermediate_results(intermediate_results, digit, a_digits, idx, print_to_result)
        
        intermediate_total_results.append(intermediate_results)
        
        current_column_contributions, current_columns = generate_column_contributions(intermediate_total_results)
        
        current_breakdown = calculate_breakdown(current_columns, current_column_contributions, idx)
        
        print_to_result("\nIntermediate column summary after this step:\n")
        print_breakdown(current_breakdown, idx, print_to_result)
        
        step_result = calculate_final_result(intermediate_results)
        step_results.append(step_result)
        print_to_result(f"\nStep {idx + 1} result: {step_result}\n")
        
    print_to_result("\nSum up all steps from right-most column to left-most.\n")
    
    total_column_contributions, total_columns = generate_total_column_contributions(intermediate_total_results)
    
    total_breakdown = calculate_breakdown(total_columns, total_column_contributions)
    
    print_breakdown(total_breakdown, 0, print_to_result)
    
    final_result = calculate_final_result_from_columns(total_columns)
    
    print_to_result("\nSum everything up:\n")
    sum_everything_up(step_results, print_to_result)
    
    print_to_result(f"\nFinal result: {final_result}\n")
    
    return "\n".join(result_string)

def print_standing_form(a, b, print_fn):
    a_str = str(a)
    b_str = str(b)
    
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    print_fn(f"    {a_str}")
    print_fn(f"x   {b_str}")
    print_fn("-------------")

def print_step_intro(digit, a, idx, print_fn):
    print_fn()
    print_fn(f"Step {idx + 1}: Calculate for the {idx + 1}st digit from the right ({digit}):")
    print_fn()
    print_fn(f"{digit} * {a} = ?")
    print_fn()

def calculate_intermediate_results(digit, a_digits, idx):
    intermediate_results = []
    for i, a_digit in enumerate(a_digits):
        product = digit * a_digit
        shifted_product = product * (10 ** (i + idx))
        intermediate_results.append((product, shifted_product))
    return intermediate_results

def print_intermediate_results(intermediate_results, digit, a_digits, idx, print_fn):
    for i, (product, shifted_product) in enumerate(intermediate_results):
        shift_note = f"(shift whole number {idx + 1} step{'s' if idx > 0 else ''} left)"
        print_fn(f"{digit} * {a_digits[i]} = {shifted_product} {shift_note}")

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

def calculate_breakdown(columns, column_contributions, shift=0):
    carry = 0
    breakdown = []
    
    for i in range(len(columns)):
        total = columns[i] + carry
        carry, value = divmod(total, 10)
        breakdown.append((i + 1 + shift, [d for d in column_contributions[i] if d != 0], value, carry))
    
    return breakdown

def print_breakdown(breakdown, shift, print_fn):
    for i, (col, original, value, carry) in enumerate(breakdown):
        if original:
            additions = " + ".join(map(str, original))
        else:
            additions = "0"
        carry_note = f"({carry} is carried)" if carry else ""
        shift_note = f"(shifted {shift} step{'s' if shift != 1 else ''} left)" if shift > 0 else ""
        print_fn(f"Column {col}: {additions} = {value} {carry_note} {shift_note}")

def calculate_final_result(intermediate_results):
    return sum(shifted_product for _, shifted_product in intermediate_results)

def calculate_final_result_from_columns(columns):
    final_result = 0
    for i, column in enumerate(columns):
        final_result += column * (10 ** i)
    return final_result

def sum_everything_up(step_results, print_fn):
    max_length = len(str(max(step_results)))
    step_results_str = [str(result).zfill(max_length) for result in step_results]
    for result in step_results_str:
        print_fn(f"\t{result}")
    
    columns = list(map(list, zip(*[result[::-1] for result in step_results_str])))
    columns = [[int(digit) for digit in col] for col in columns]
    
    carry = 0
    breakdown = []
    
    for idx, col in enumerate(columns):
        total = sum(col) + carry
        carry, value = divmod(total, 10)
        breakdown.append((idx + 1, col, value, carry))
    
    print_fn("\nColumn by column addition:")
    for i, (col, original, value, carry) in enumerate(breakdown):
        if original:
            additions = " + ".join(map(str, original))
        else:
            additions = "0"
        carry_note = f"({carry} is carried)" if carry else ""
        print_fn(f"Column {i + 1}: {additions} = {value} {carry_note}")

def format_number(n):
    if n < 1000:
        return str(n)
    elif n < 1000000:
        return f"{n/1000:.1f}k"
    else:
        return f"{n/1000000:.1f}M"

def sample_multiplication_steps(digit_lengths, samples_per_size):
    import statistics
    import pandas as pd
    
    avg_result_lengths = []
    
    for digits in digit_lengths:
        results = []
        for _ in range(samples_per_size):
            a = random.randint(10**(digits-1), 10**digits - 1)
            b = random.randint(10**(digits-1), 10**digits - 1)
            result = generate_multiplication_steps(a, b)
            results.append(len(result))
        
        avg_length = statistics.mean(results)
        avg_tokens = avg_length / 4  # 1 token ~= 4 chars in English
        avg_result_lengths.append((digits, avg_length, avg_tokens))
    
    df = pd.DataFrame(avg_result_lengths, columns=["Length of digits", "Average Characters Needed", "Average Tokens Needed"])
    df["Average Characters Needed"] = df["Average Characters Needed"].apply(format_number)
    df["Average Tokens Needed"] = df["Average Tokens Needed"].apply(format_number)
    print(df.to_string(index=False))

# Example usage
digit_lengths_to_try = [1, 2, 3, 5, 7, 10, 15, 20, 50, 100]
sample_rate = 5
sample_multiplication_steps(digit_lengths_to_try, sample_rate)