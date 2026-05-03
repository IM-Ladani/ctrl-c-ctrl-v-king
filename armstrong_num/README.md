# Armstrong Number Checker 🔢

## What It Does

Checks if a given number is an Armstrong number (also called Narcissistic number).

## Logic Used

- Convert number to string to find its length
- Extract each digit and convert back to integer
- Raise each digit to the power of total number of digits
- Sum all the results
- Compare sum with original number

## Example

Input: `153` → Output: "given number is armstrong number."

## What I Learned

- Converting between string and integer
- Using exponentiation (`**`) for powers
- Working with lists to store intermediate values
- The importance of total length for digit powers

## Challenges Faced

- Understanding that the power changes based on number of digits
- Converting string digits back to integers for math operations
