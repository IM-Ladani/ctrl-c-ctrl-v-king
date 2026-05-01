# FizzBuzz

## Problem Statement

Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

## Logic Explanation

The solution uses the modulo operator (%) to check divisibility. When a number is divided by 3 and the remainder is 0, it is a multiple of 3. The same applies for 5. The program first checks if a number is divisible by both 3 and 5 using the AND operator. If true, it prints "FizzBuzz". If false, it checks divisibility by 3 alone, then by 5 alone. If none of these conditions are met, it prints the original number. This order matters because checking "FizzBuzz" first prevents it from being incorrectly caught by the individual Fizz or Buzz conditions.

## Algorithm Steps

1. Loop from 1 to 100
2. If number divisible by 3 AND 5 → print "FizzBuzz"
3. Else if number divisible by 3 → print "Fizz"
4. Else if number divisible by 5 → print "Buzz"
5. Else → print the number

## Complexity

Time complexity: O(n) where n is the range of numbers
Space complexity: O(1)

## Sample Output

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...
