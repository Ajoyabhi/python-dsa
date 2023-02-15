def romantoint(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 50, 'D': 500, 'M': 1000}
    n = len(s)
    num = roman_map[s[n-1]]
    for i in range (n-2, -1, -1):
        if roman_map[s[i]] > roman_map[s[i+1]]:
            num = num + roman_map[s[i]]
        elif roman_map[s[i]] == roman_map[s[i+1]]:
            num = num + roman_map[s[i]]
        else:
            num = num - roman_map[s[i]]
    return num
s = input()
print("number is", romantoint(s))

