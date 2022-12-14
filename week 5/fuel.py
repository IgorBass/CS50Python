def main():
    fraction = input("Number: ")
    y = convert(fraction)
    print(gauge(y))


def convert(fraction):
    while True:
        try:
            nums = fraction.split('/')
            first_number = int(nums[0])
            second_number = int(nums[1])

            fract = int(round((first_number/second_number) * 100))

            if first_number > second_number:
                raise ValueError

            return fract

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError



def gauge(percentage):
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
