from rich import print
from rich.text import Text

def simplify_strings(s):
    if not s:
        return ''
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    result = Text()
    for char in sorted(char_count.keys()):
        result.append(str(char_count[char]), style="blue")  # الرقم باللون الأزرق
        result.append(char, style="yellow")  # الحرف باللون الأصفر
        result.append(' ')  # إضافة مسافة
    return result


while True:
    try:
        s = input("Enter a string: ")
        if not s:
            break
    except EOFError:
        break
    result = simplify_strings(s)
    print("Simplified string:", result)
