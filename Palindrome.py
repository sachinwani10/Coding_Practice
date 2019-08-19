from math import floor

def palindrome(s):
    n = len(s)
    center = floor(n/2)
    
    s1 = s[ : center]
    if n % 2 == 0:
        s2 = s[center : ]
    else:
        s2 = s[center + 1: ]
    
    return s1 == s2[::-1]
    
print(palindrome("redder"))

==========================================

def palindrome(s):
    n = len(s)
    i, j = 0, n-1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
    
print(palindrome("raxxr"))
