def sqrt(number):
    if type(number) != float:
        raise TypeError("The input is not an integer")
    number = number ** 0.5
    return number

def main():
  print(sqrt(float(input("Enter a number: "))))

if __name__ == "__main__":
    main()