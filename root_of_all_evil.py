def sqrt(number):
    """
    this function gets a number and return the square root of the number
    :param number: number
    :return: the square root of the number
    """
    if number < 0:
        raise ValueError("Number cannot be negative")
    number = number ** 0.5
    return number

def main():
    print(sqrt(float(input("Enter a number: "))))

if __name__ == "__main__":
    main()