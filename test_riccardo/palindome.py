"""Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
 "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
  "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization,
  and spacing are usually ignored.
"""
import re


def sanitize(s):
    str_sanitized = re.sub(ur"([^\w\d\s]+)", '', s).replace(" ", "").lower()
    return str_sanitized


def is_palindrome(str):
    sanitized = sanitize(str)
    if sanitized == sanitized[::-1]:
        return True
    else:
        return False