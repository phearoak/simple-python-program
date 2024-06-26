#!/usr/bin/env python3

# Fonction qui vérifie si une chaîne de caractères est un palindrome
def is_palindrome(s):
    # Supprime les espaces et convertit la chaîne en minuscules
    s = s.replace(" ", "").lower()
    
    # Initialisation des index de début et de fin
    start = 0
    end = len(s) - 1
    
    # Compare les caractères tout en déplaçant les pointeurs vers le centre
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Test de la fonction is_palindrome
test_string1 = "A man a plan a canal Panama"
print(f"'{test_string1}' is a palindrome: {is_palindrome(test_string1)}")