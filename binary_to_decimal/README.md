# Binary to Decimal Converter 💻

## What It Does

Converts a binary number to decimal.

## Logic Used

- Validate input (only 0s and 1s)
- Convert each digit to integer and store in list
- Reverse the list to process from rightmost digit
- Multiply each digit by 2 raised to its position power
- Sum all values for final decimal

## Example

Input: `1010` → Output: `10`

Input: `110011` → Output: `51`

## What I Learned

- String validation with loops
- Using `[::-1]` to reverse a list
- Powers of 2 for binary conversion
- The importance of `return True` placement

## Challenges Faced

- Bug: `return True` was inside the loop (only checked first digit)
- Fix: Moved `return True` outside the loop
- Understanding that rightmost digit is position 0
