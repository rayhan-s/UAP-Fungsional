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
print(f"Apakah '{string}' merupakan palindrom? {result}")

