from attr import NOTHING


def main():
   ...


def convert(time):
    time = time.split(':')
    hour = float(time[0])
    minute = float(time[1])/60
    return float(hour + minute)



if __name__ == "__main__":
    main()

    ask = input("Enter time: ")

    x= convert(ask)


    if 7 <= x <= 8:
        print("breakfast time")
    elif 12<=x<=13:
        print("lunch time")
    elif 18 <=x<= 19:
        print("dinner time")
    else:
         NOTHING