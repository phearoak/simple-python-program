#!/usr/bin/env python3

# This program calculates the sum of two numbers, finds the maximum number in a list, and checks if a number is prime

# Function to calculate the sum of two numbers
def calculate_sum(a, b):
    return a + b

# Function to find the maximum number in a list
def find_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num_list = [1, 2, 3, 4, 5]
print("Sum of 4 and 5:", calculate_sum(4, 5))
print("Maximum number in the list:", find_max(num_list))
print("Is 7 prime?", is_prime(7))
