def revert(s):
    if s:
        s = s[-1] + revert(s[:-1])
    return s

def revert2(string):
    return string[::-1]

str1 = "안녕 세상!"
str2 = revert(str1)
str3 = revert2(str1)

print(str1)
print(str2)
print(str3)