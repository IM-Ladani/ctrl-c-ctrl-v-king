# Anagram Checker 🔤

## What It Does

Checks if two strings are anagrams (contain the same letters in different order).

## Logic Used

- Remove spaces from both strings
- Convert both strings to lowercase
- Convert each string into a list of characters
- Sort both lists alphabetically
- Compare the sorted lists

## Example

Input: `"listen"` and `"silent"` → Output: "given strings are anagrams"

## What I Learned

- Removing spaces with `.replace()`
- Converting strings to lists
- Sorting lists with `.sort()`
- Comparing sorted lists for equality

## Challenges Faced

- Understanding that `.sort()` returns `None` and sorts in place
- Handling spaces and case sensitivity
- Converting the problem into sorted list comparison

## Note

Strings with same letters but different case or spaces will still match because we normalize them first.
