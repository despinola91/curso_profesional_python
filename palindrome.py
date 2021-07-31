def is_palindrome(string: str) -> bool:
    string = string.replace(" ","").lower()
    return string == string[::-1]

def run():
    print(is_palindrome("Ana"))
    print(is_palindrome("Facundo"))
    print(is_palindrome(1000))

if __name__ == "__main__":
    run()