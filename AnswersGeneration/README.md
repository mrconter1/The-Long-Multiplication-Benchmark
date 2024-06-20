### Multiplication Steps Generator Script

This script helps you understand the traditional long multiplication method by providing a step-by-step breakdown of the multiplication process for two integers.

#### Functions Overview

1. **`sample_multiplication_steps(min_digits, max_digits, samples_per_size)`**

   The function `sample_multiplication_steps(min_digits, max_digits, samples_per_size)` generates sample multiplications for numbers with a range of digit lengths and computes the average length of the generated descriptions. This helps estimate the number of characters and tokens needed to multiply two same-sized numbers of size N.

   **Example Output:**

   | Length of digits | Average Characters Needed | Average Tokens Needed |
   |------------------|---------------------------|------------------------|
   | 1                | 441.60                    | 110.40                 |
   | 2                | 1042.44                   | 260.61                 |
   | 3                | 1923.52                   | 480.88                 |
   | 4                | 3282.24                   | 820.56                 |
   | 5                | 4895.08                   | 1223.77                |
   | 6                | 6947.12                   | 1736.78                |
   | 7                | 9316.00                   | 2329.00                |

2. **`generate_multiplication_steps(a, b)`**

   The function `generate_multiplication_steps(a, b)` takes two numbers and breaks down their multiplication into detailed steps, similar to how it's taught in schools. It shows the intermediate results and column-by-column additions leading to the final result.

   **Example Output for Multiplying 523 and 421:**
   ```
   Calculating:

       523
   x   421
   -------------

   Step 1: Multiply by the 1st digit from the right (1):

   1 * 523 = 523

   Intermediate result:
       523

   Step 2: Multiply by the 2nd digit from the right (2), shifted one position to the left:

   2 * 523 = 1046

   Intermediate result:
      10460

   Step 3: Multiply by the 3rd digit from the right (4), shifted two positions to the left:

   4 * 523 = 2092

   Intermediate result:
     209200

   Adding all the intermediate results:

       523
      10460
     209200
   -------------
     220183

   Final result: 220183
   ```

This example shows each step of multiplying 523 by 421, including the intermediate multiplications and the final addition.