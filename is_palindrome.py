def is_palindrome(x: int) -> int:
    return False if x < 0 else x == int(str(x)[::-1])


print(is_palindrome(121))
print(is_palindrome(123))
