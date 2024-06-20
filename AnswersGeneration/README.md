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

   **Example Output for Multiplying 345 and 534:**
   ```
   Calculating:

       345
   x   534
   -------------

   Step 1: Calculate for the 1st digit from the right (4):

   4 * 345 = ?

   4 * 5 = 20 (shift whole number 1 step left)
   4 * 4 = 160 (shift whole number 1 step left)
   4 * 3 = 1200 (shift whole number 1 step left)

   Intermediate column summary after this step:

   Column 1: 0 = 0
   Column 2: 2 + 6 = 8
   Column 3: 1 + 2 = 3
   Column 4: 1 = 1

   Step 1 result: 1380


   Step 2: Calculate for the 2nd digit from the right (3):

   3 * 345 = ?

   3 * 5 = 150 (shift whole number 2 steps left)
   3 * 4 = 1200 (shift whole number 2 steps left)
   3 * 3 = 9000 (shift whole number 2 steps left)

   Intermediate column summary after this step:

   Column 2: 0 = 0 (shifted 1 step left)
   Column 3: 2 + 6 + 5 = 13 (1 is carried) (shifted 1 step left)
   Column 4: 1 + 2 + 1 + 2 = 7 (shifted 1 step left)
   Column 5: 1 + 1 + 9 = 11 (1 is carried) (shifted 1 step left)

   Step 2 result: 10350


   Step 3: Calculate for the 3rd digit from the right (5):

   5 * 345 = ?

   5 * 5 = 2500 (shift whole number 3 steps left)
   5 * 4 = 20000 (shift whole number 3 steps left)
   5 * 3 = 150000 (shift whole number 3 steps left)

   Intermediate column summary after this step:

   Column 3: 0 = 0 (shifted 2 steps left)
   Column 4: 2 + 6 + 5 = 13 (1 is carried) (shifted 2 steps left)
   Column 5: 1 + 2 + 1 + 2 + 5 = 11 (1 is carried) (shifted 2 steps left)
   Column 6: 1 + 1 + 9 + 2 = 13 (1 is carried) (shifted 2 steps left)
   Column 7: 2 + 5 = 7 (shifted 2 steps left)
   Column 8: 1 = 1 (shifted 2 steps left)

   Step 3 result: 172500


   Sum up all steps from right-most column to left-most.

   Column 1: 0 = 0
   Column 2: 0 = 0
   Column 3: 0 = 0
   Column 4: 0 + 8 + 0 = 8
   Column 5: 3 + 3 = 6
   Column 6: 1 + 7 = 8
   Column 7: 1 = 1

   Sum everything up:

           001380
           010350
           172500

   Column by column addition:
   Column 1: 0 + 0 + 0 = 0
   Column 2: 0 + 0 + 0 = 0
   Column 3: 0 + 0 + 0 = 0
   Column 4: 0 + 8 + 0 = 8
   Column 5: 3 + 3 = 6
   Column 6: 1 + 7 = 8
   Column 7: 1 = 1

   Final result: 184230
   ```

This example shows each step of multiplying 345 by 534, including the intermediate multiplications and the final addition.