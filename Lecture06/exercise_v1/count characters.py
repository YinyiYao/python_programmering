def count_character():
    print("Enter the String:")
    text = input()
    print("Enter the Character:")
    char = input()
    textLen = len(text)
    sum = 0
    for i in range(textLen):
        if char==text[i]:
            sum = sum+1
    print("\nOccurrence of Given Character is:")
    print(sum)

def main():
    return(count_character())

if __name__ == "__main__":
    main()

'''https://codescracker.com/python/program/python-program-count-character-in-string.htm'''