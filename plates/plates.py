def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: Starts with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3: No periods, spaces, or punctuation
    if not s.isalnum():
        return False

    # Rule 4: Numbers, if present, must be at the end
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not number_started:
                if s[i] == '0':
                    return False  # Rule 5: First number cannot be 0
                number_started = True
        elif number_started:
            return False  # Letters after numbers not allowed

    return True


main()
