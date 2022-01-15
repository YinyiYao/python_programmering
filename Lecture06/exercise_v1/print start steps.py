def stars_step():
    rows = 10
    for i in range(0, rows):
        # nested loop for each column
        for j in range(0, i + 1):
            # print star
            print("*", end=' ')
        # new line after each row
        print("\r")

def main():
    return(stars_step())

if __name__ == "__main__":
    main()