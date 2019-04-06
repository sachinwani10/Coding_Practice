def str_urlify(test_string, str_len):
    if not test_string:
        return "%20"
    i = 0
    new = ""
    while i < str_len:
        if test_string[i] != " ":
            new = new + test_string[i]
            i += 1
        else:
            new = new + "%20"
            i += 1
    return new


my_string = "Mr    John Smith         "
str_size = 16
print(str_urlify(my_string, str_size))
