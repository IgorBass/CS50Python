monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    print(valid_date())

def valid_date():
    user_input = input('Date: ')
    while True:
        try:
            if '/' in user_input:
                n = user_input.split('/')
                day = int(n[1])
                month = int(n[0])
                year = int(n[-1])
                if day > 31 or month>12:
                    user_input = input('Date: ')
                formatted = f'{year}-{month:02}-{day:02}'
                return formatted
            elif ',' in user_input:
                n = user_input.replace(',', '').split(' ')
                month = monthes.index(n[0]) + 1
                day = int(n[1])
                year = int(n[-1])
                if month>12 or day>31:
                    user_input = input('Date: ')
                formatted = f'{year}-{month:02}-{day:02}'
                return formatted
        except ValueError:
               user_input = input('Date: ')





main()