# Anagram of String
""" An Anagram is a condition where one string or number is rearranged in that manner
each character of the rearranged string or number must be a part of another string or number."""


def anagramStr(str1, str2):
    if sorted(str1) == sorted(str2):
        print("strings are anagram")
    else:
        print("Strings are not anagram")


str1 = input("Enter a string1")
str2 = input("Enter a string2")
anagramStr(str1, str2)