# Quera Python Practice: Problem Solutions

## Introduction

This repository contains my solutions to Python problems from Quera. I made it to practice Python and improve my problem-solving skills. Each problem has its own Python file, so it is easy to find and check the solutions.

Introduction
This repository contains my solutions to Python problems from Quera. I created it to practice Python, improve my problem-solving skills, and learn more by solving different problems.
Each problem has its own Python file. The files are named based on the problem, so it is easier to find each solution. I tried to solve the problems using the Python concepts I have learned so far.
Some problems are about numbers and mathematical rules, while others use strings, loops, and conditions. Working on these problems helps me understand how to use Python in different situations.
I will add more solutions to this repository as I solve new problems on Quera. This repository is also a place where I can keep my code and check my progress as I learn Python.
### 1. Pythagorean Theorem

**Problem**

Write a program that gets 3 positive numbers from the user. The program must check if we can make a right triangle with these numbers. If we can, print `YES`. If not, print `NO`.

**Description**

The program gets 3 numbers from the user. I put them in a list and use `sorted()` to sort them. The smallest number comes first and the biggest one comes last.

After this, I check the square of the first two numbers and add them together. Then I check the square of the last number. If the results are the same, the program prints `YES`, and if they are not the same, it prints `NO`.

I used `sorted()` because the numbers can come in any order. This way I can check the biggest number with the other two numbers.

**File**: [`pythagorean_theorem.py`](pythagorean_theorem.py)

**Problem Link:** [View on Quera](https://quera.org/problemset/280?tab=description)

### 2. Triangle Angles

**Problem**

Write a program that gets 3 angles from the user. We need to check if we can make a triangle with these angles or not. If we can, the program prints `Yes`, and if not, it prints `No`.

**Description**

The program gets 3 numbers in one line. I use `split()` to separate them and change them to integers. Then I put them in a list called `angles`.

I use `sum()` to check the total of the angles. The sum must be 180. I also use `all()` to check that none of the angles is zero.

If both conditions are true, the program prints `Yes`. If one of them is not true, it prints `No`.

**File:** [`triangle_angles.py`](triangle_angles.py)

**Problem Link:** [View on Quera](https://quera.org/problemset/10230?tab=description)

### 3. Chessboard Difference
### 3. Chessboard Difference

**Problem**

Write a program that gets the number of each chess piece from the user. The program must tell how many pieces we need to add or remove to have the correct number of each piece.

**Description**

In this question, Puyan has a chess set, but the number of some pieces is not correct. Some pieces are more than needed and some are less.

A chess set needs 1 king, 1 queen, 2 rooks, 2 bishops, 2 knights and 8 pawns. The program gets the number of these pieces from the user in one line.

I use different variables for each piece. Then I subtract the number we have from the number we need. For example, for the king I use `1 - king`, and for the pawns I use `8 - pawns`.

At the end, the program prints the results in one line. A positive number means we need to add some pieces, and a negative number means we have to remove some pieces.

**File:** [`chessboard_difference.py`](chessboard_difference.py)

**Problem Link:** [View on Quera](https://quera.org/problemset/2636?tab=description)

### 4. Digit Pattern

**Problem**

Write a program that gets an integer from the user. The number can have different number of digits. The program must print each digit as many times as the digit number.

**Description**

The program gets the number as a string. I used a string because I need to get each digit one by one.

The first loop goes through all digits. It prints the digit with `:` after it. Then the second loop prints the same digit again. How many times it prints depends on the digit value.

For example, if the digit is `3`, the output is `3:333`. If the digit is `5`, the output is `5:55555`. When the digit is `0`, nothing is printed after the colon. After each digit, the program goes to the next line.

I used two `for` loops for this. The first loop finds each digit, and the second loop prints it as many times as needed.

**File:** [`digit_pattern.py`](digit_pattern.py)

**Problem Link:** [View on Quera](https://quera.org/problemset/9774?tab=description)

### 5. Digital Root

**Problem**

Write a program that gets a number from the user. If the number has more than one digit, we must add its digits together and get a new number. We do this again with the new number until only one digit is left.

**Description**

The program gets an integer from the user. I use two `while` loops to do this.

The first loop checks if the number is 10 or bigger. If it is, the program starts adding its digits. I set `digit_sum` to zero at the start of each round.

The second loop gets the last digit using `% 10` and adds it to `digit_sum`. Then `// 10` removes the last digit from the number. This continues until there are no digits left in the number.

After that, I put the sum in `number`. If the new number still has more than one digit, the program does the same thing again. When only one digit is left, it prints the result.

**File:** [`digital_root.py`](digital_root.py)

**Problem Link:** [View on Quera](https://quera.org/problemset/3539?tab=description)