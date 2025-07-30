def main():
    text = input("Input: ")
    print("Output:", remove_vowels(text))

def remove_vowels(text):
    vowels = "AEIOUaeiou"
    return "".join([char for char in text if char not in vowels])

main()
