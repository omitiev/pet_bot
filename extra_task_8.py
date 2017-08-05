# A pangram is a sentence that contains all the letters of the English alphabet at least once,
# for example: “The quick brown fox jumps over the lazy dog”.
# Your task here is to write a function to check a sentence to see if it is a pangram or not.


import default


default.start(8)


def is_pangram(usr_str):
    counter = 0
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    for i in alphabet:
        if i in list(usr_str):
            counter += 1
    return counter == len(alphabet)


str4check = str(input("Please enter your string for checking: "))
print("Your string is pangram? ", is_pangram(str4check))


default.end()
