def one_way(str1, str2):
    counter = 0
    if abs(len(str1) - len(str2)) != 1:
        return False
    else:
        list1 = [0] * 128
        list2 = [0] * 128
        for c in str1:
            list1[ord(c)] += 1
        for c in str2:
            list2[ord(c)] += 1
        if len(str1) > len(str2):
            for c in str1:
                if list1[ord(c)] != list2[ord(c)]:
                    counter += 1
        else:
            for c in str2:
                if list2[ord(c)] != list1[ord(c)]:
                    counter += 1
    if counter > 1:
        return True
    return False


tstr1 = "aaaaaa"
tstr2 = "aaaaaaa"
print(one_way(tstr1, tstr2))
