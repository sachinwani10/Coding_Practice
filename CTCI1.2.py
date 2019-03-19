def is_permutation(str1, str2):
    if len(str1) == len(str2):
        a = sorted(str1)
        b = sorted(str2)
        if a == b:
            return True
        else:
            return False
    return False


str_a = "sekjfjh"
str_b = "sekjfjh"
print(is_permutation(str_a, str_b))
