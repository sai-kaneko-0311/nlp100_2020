import re
def cipher(str):
    result = ''
    for char in str:
        if re.search(r'[a-z]', char):
            result += chr(219-ord(char))
        else:
            result += char
    return result
print(cipher('Hello, mom!'))
print(cipher('Hvool, nln!'))