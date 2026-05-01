# Palindrome Checker

## Problem Statement

Determine whether a given string reads the same forwards and backwards. The check should be case-insensitive and ignore spaces, punctuation, and special characters.

## Logic Explanation

A palindrome is verified by comparing characters from both ends moving toward the center. The algorithm first cleans the input string by converting all characters to lowercase and removing non-alphanumeric characters (spaces, commas, periods, etc.). After cleaning, two pointers are used: one starting at the beginning (left) and one at the end (right). At each step, the characters at both pointers are compared. If they differ, the string is not a palindrome. If they match, the left pointer moves right and the right pointer moves left. This continues until the pointers cross each other. If all comparisons pass, the string is a palindrome.

## Algorithm Steps

1. Convert input string to lowercase
2. Remove all non-alphanumeric characters (keep only a-z and 0-9)
3. Initialize left pointer at index 0 and right pointer at last index
4. While left < right:
   - If characters at left and right are different → return False
   - Move left pointer forward by 1
   - Move right pointer backward by 1
5. Return True if loop completes without mismatches

## Complexity

Time complexity: O(n) where n is the length of the string
Space complexity: O(n) for the cleaned string (can be O(1) with two pointers on original string)

## Test Cases

- "racecar" → True
- "A man, a plan, a canal: panama" → True
- "hello" → False
- "12321" → True
