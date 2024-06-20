```
Calculating:

    523
x   421
-------------

Step 1: Calculate for the 1st digit from the right (1):

1 * 523 = ?

1 * 3 = 3 (shift whole number 1 step left)
1 * 2 = 20 (shift whole number 1 step left)
1 * 5 = 500 (shift whole number 1 step left)

Intermediate column summary after this step:

Column 1: 3 = 3
Column 2: 2 = 2
Column 3: 5 = 5

Step 1 result: 523


Step 2: Calculate for the 2st digit from the right (2):

2 * 523 = ?

2 * 3 = 60 (shift whole number 2 steps left)
2 * 2 = 400 (shift whole number 2 steps left)
2 * 5 = 10000 (shift whole number 2 steps left)

Intermediate column summary after this step:

Column 2: 3 = 3  (shifted 1 step left)
Column 3: 2 + 6 = 8  (shifted 1 step left)
Column 4: 5 + 4 = 9  (shifted 1 step left)
Column 5: 0 = 0  (shifted 1 step left)
Column 6: 1 = 1  (shifted 1 step left)

Step 2 result: 10460


Step 3: Calculate for the 3st digit from the right (4):

4 * 523 = ?

4 * 3 = 1200 (shift whole number 3 steps left)
4 * 2 = 8000 (shift whole number 3 steps left)
4 * 5 = 200000 (shift whole number 3 steps left)

Intermediate column summary after this step:

Column 3: 3 = 3  (shifted 2 steps left)
Column 4: 2 + 6 = 8  (shifted 2 steps left)
Column 5: 5 + 4 + 2 = 1 (1 is carried) (shifted 2 steps left)
Column 6: 1 + 8 = 0 (1 is carried) (shifted 2 steps left)
Column 7: 1 = 2  (shifted 2 steps left)
Column 8: 2 = 2  (shifted 2 steps left)

Step 3 result: 209200


Sum up all steps from right-most column to left-most.

Column 1: 3 = 3
Column 2: 2 + 6 = 8
Column 3: 5 + 4 + 2 = 1 (1 is carried)
Column 4: 1 + 8 = 0 (1 is carried)
Column 5: 1 = 2
Column 6: 2 = 2

Sum everything up:

        000523
        010460
        209200

Column by column addition:
Column 1: 3 + 0 + 0 = 3
Column 2: 2 + 6 + 0 = 8
Column 3: 5 + 4 + 2 = 1 (1 is carried)
Column 4: 0 + 0 + 9 = 0 (1 is carried)
Column 5: 0 + 1 + 0 = 2
Column 6: 0 + 0 + 2 = 2

Final result: 220183
´´´