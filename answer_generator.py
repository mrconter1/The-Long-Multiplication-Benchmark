def generate_multiplication_steps(a, b):
    print("Calculating: ", a, "*", b)
    
    a_str = str(a)
    b_str = str(b)
    
    results = []
    
    for i, digit in enumerate(reversed(b_str)):
        num_zeros = i
        current_step = int(digit) * a
        shifted_step = current_step * (10 ** num_zeros)
        results.append(shifted_step)
        print(f"Step {i+1}: Calculate for the {i+1}th digit from the right ({digit}):")
        print(f"{digit} * {a} = {current_step}")
        print(f"Shifted left by {num_zeros} places: {shifted_step}")
        print()
    
    print("Summing up all the shifted results:")
    total_sum = sum(results)
    for result in results:
        print(result)
    print("Final Result: ", total_sum)

generate_multiplication_steps(64369, 95689)