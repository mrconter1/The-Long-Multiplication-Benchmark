### Multiplication Context Size Estimation

The `estimator.py` script enables estimation of the context window size needed to manually perform schoolbook long multiplication. It provides a step-by-step breakdown of the multiplication process for two integers. The conclusion drawn from the analysis is that an **around 2500 token** context window should be enough to manually calculate the multiplication of two **seven-digit** numbers using the schoolbook long multiplication method.

#### Functions Overview

1. **sample_multiplication_steps**

   The purpose of `sample_multiplication_steps` is to estimate how many characters and tokens a typical person would need to solve a multiplication of two same-sized whole numbers using the schoolbook long multiplication method. This function generates sample multiplications for numbers with a range of digit lengths and computes the average length of the generated descriptions.

   **Output with sample rate of five:**

| Length of digits | Average Characters Needed | Average Tokens Needed |
|------------------|---------------------------|------------------------|
| 1                | 430.2                     | 107.5                  |
| 2                | 1.0k                      | 250.2                  |
| 3                | 1.9k                      | 478.7                  |
| 5                | 4.7k                      | 1.2k                   |
| 7                | 9.4k                      | 2.4k                   |
| 10               | 18.8k                     | 4.7k                   |
| 15               | 46.7k                     | 11.7k                  |
| 20               | 85.7k                     | 21.4k                  |
| 25               | 144.5k                    | 36.1k                  |
| 30               | 228.6k                    | 57.1k                  |
| 40               | 447.1k                    | 111.8k                 |
| 50               | 789.8k                    | 197.5k                 |
| 75               | 2.2M                      | 561.2k                 |
| 100              | 4.9M                      | 1.2M                   |
| 150              | 15.1M                     | 3.8M                   |

2. **generate_multiplication_steps**

   `generate_multiplication_steps` is used by `sample_multiplication_steps` and generates a detailed output of all the steps involved in solving a multiplication of two same-sized whole numbers, including all intermediate steps. This function breaks down the multiplication into detailed steps, similar to how it's taught in schools, showing intermediate results and column-by-column additions leading to the final result.

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