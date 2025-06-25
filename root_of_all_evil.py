def sqrt(number):
    if number < 0:
        raise ValueError("Number cannot be negative")
    number = number ** 0.5
    return number

def main():
    print(sqrt(float(input("Enter a number: "))))

if __name__ == "__main__":
    main()