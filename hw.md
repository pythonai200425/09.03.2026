# Homework – Recursive Calls in Python

Solve the following exercises using **recursion only** (do not use loops unless explicitly stated).

The exercises gradually increase in difficulty.

# Exercise 1 – Print Numbers Down

Write a recursive function:

print_down(n)

The function prints all numbers from **n down to 1**.

Example:

print_down(5)

Output:

5 4 3 2 1

Requirements:

* Use recursion
* Base case when n == 0

# Exercise 2 – Sum of Odd Numbers

Write a recursive function:

sum_odd(n)

The function returns the **sum of all odd numbers from 1 to n**.

Example:

sum_odd(7)

Result:

1 + 3 + 5 + 7 = 16

Expected output:

16

Notes:

* If n is even, skip it
* Only odd numbers should be added

# Exercise 3 – Power Function

Write a recursive function:

power(base, exponent)

The function calculates:

base ^ exponent

Example:

power(2, 4)

Output:

16

Explanation:

2^4 = 2 * 2^3
2^3 = 2 * 2^2
2^2 = 2 * 2^1
2^1 = 2

Base case:

exponent == 0 → return 1

# Exercise 4 – Maximum in a List

Write a recursive function:

max_in_list(lst)

The function returns the **largest number inside the list**.

Example:

max_in_list([3, 8, 2, 15, 6])

Output:

15

Hints:

* Compare the first element with the maximum of the rest of the list

Concept idea:

max([3,8,2,15,6])
= max(3, max([8,2,15,6]))

Base case:

list with one element

# Exercise 5 – Count Even Numbers in a List

Write a recursive function:

count_even(lst)

The function returns how many **even numbers** exist in the list.

Example:

count_even([2,5,8,7,6,3,10])

Output:

4

Explanation:

Even numbers are:

2, 8, 6, 10

Hints:

* Check the first element
* Add 1 if it is even
* Continue recursion with the rest of the list

Base case:

empty list → return 0

# Bonus Challenge (Optional)

Write a recursive function:

sum_digits(n)

The function returns the **sum of digits of a number**.

Example:

sum_digits(583)

Output:

5 + 8 + 3 = 16

Hint:

last digit → n % 10
remove digit → n // 10

Base case:

n == 0

Good luck 🚀

Submit email: **[pythonai200425+recursive@gmail.com](mailto:pythonai200425+recursive@gmail.com)**
