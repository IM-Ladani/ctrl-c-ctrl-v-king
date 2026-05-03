# Perfect Number Finder ✨

## What It Does

Checks if a given number is a perfect number (sum of proper divisors equals the number itself).

## Logic Used

- Loop through all numbers from 1 to n-1
- Check if each number divides n evenly (n % i == 0)
- Store all divisors in a list
- Sum all divisors
- Compare sum with original number

## Example

Input: `6` → Output: "Given number is Perfect number"

Input: `12` → Output: "Given number is not perfect number"

## What I Learned

- Finding divisors using modulo operator
- Building lists dynamically with `.append()`
- Using `sum()` to add all list elements
- Proper divisors exclude the number itself

## Challenges Faced

- Understanding that perfect numbers are rare (6, 28, 496, 8128...)
- Making sure the loop stops at n-1 (excluding n itself)
