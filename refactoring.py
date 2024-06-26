#!/usr/bin/env python3

import sys

# Programme pour calculer des statistiques simples sur une liste de nombres

# Calcule la somme des nombres dans une liste donnée
def sum(numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    return sum_numbers

# Calcule la longueur d'une liste donnée
def length(numbers):
    count = 0
    for number in numbers:
        count += 1
    return count

# Calcule la moyenne des nombres dans une liste donnée
def average(numbers):
    return sum(numbers) / length(numbers) if length(numbers) > 0 else 0

# Calcule le nombre minimum dans une liste donnée
def min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number

# Calcule le nombre maximum dans une liste donnée
def max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# Calcule les statistiques sur une liste de nombres donnée
def calculate_statistique(numbers):
    # Vérifie si la liste est vide
    if (len(numbers) == 0):
        return
    
    print("Sum: ", sum(numbers))
    print("Average: ", average(numbers))
    print("Max: ", max(numbers))
    print("Min: ", min(numbers))

# Vérifie si la liste des arguments contient uniquement des nombres
def check_input(data):
    for i in data:
        if not i.isnumeric():
            print("Please enter only numbers")
            sys.exit(1)

def main():
    data = sys.argv[1:]
    check_input(data)
    calculate_statistique(data)

if __name__ == '__main__':
    main()

