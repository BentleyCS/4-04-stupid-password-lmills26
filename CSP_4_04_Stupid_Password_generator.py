"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""
import random
import string
from binascii import crc32


def stupidPassword(n: int, l: int):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    passwords = []

    for n1 in range(1,n):
        for n2 in range(1,n):
            for n3 in range(l):
                letter1 = letters[n3]
                for n4 in range(l):
                    letter2 = letters[n4]
                    for n5 in range(1,n+1):
                        if n5 > n1 and n5 > n2:
                            password = str(n1) + str(n2) + letter1 + letter2 + str(n5)
                            passwords.append(password)


    return passwords



