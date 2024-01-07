def kalimat_palindrome(func):
    def wrapper(s):
        result = func(s)
        if result:
            return f"'{s}' Tidak False"
        else:
            return f"'{s}' Tidak True"

    return wrapper

@kalimat_palindrome
def is_palindrome(s):
    def check_palindrome(start, end):
        if start >= end:
            return True
        if s[start] == s[end]:
            return check_palindrome(start + 1, end - 1)
        else:
            return False

    return check_palindrome(0, len(s) - 1)

string = "radar"
result = is_palindrome(string.lower())
print(result)
