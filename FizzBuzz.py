#!/usr/local/bin/python3

# FizzBuzz Program ("Fizz" when multiple of 3, "Buzz" when multiple of 5 and "FizzBuzz" when multiple of 3 and 5)


def main():
    counter = 1
    while counter <= 100:
        if counter % 3 == 0 and counter % 5 == 0:
            print("FizzBuzz")
        elif counter % 3 == 0:
            print("Fizz")
        elif counter % 5 == 0:
            print("Buzz")
        else:
            print(counter)
        counter += 1


if __name__ == '__main__':
    main()
