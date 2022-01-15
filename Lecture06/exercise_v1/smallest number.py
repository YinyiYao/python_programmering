def smallest_number():
    NumList=[]
    for i in range(1,4):
        value = int(input("Please enter the Value of %d Element : " %i))
        NumList.append(value)

    print("The Smallest Element in this List is : ", min(NumList))

def main():
    return(smallest_number())

if __name__ == "__main__":
    main()