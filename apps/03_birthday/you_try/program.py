import datetime


def print_header():
    print('--------------------')
    print('Birthday')
    print('--------------------')
    print()


def date_diff(date1, date2):
    diff = date1 - date2
    return diff.days


def days_from_now(date):
    return date_diff(
        datetime.date(datetime.date.today().year, date.month, date.day),
        datetime.date.today())


def get_input():
    year = int(input('What year were you born? '))
    month = int(input('What month were you born? '))
    day = int(input('What day were you born? '))

    return datetime.date(year, month, day)


def print_user_info(date):
    print('Your birthday is {}'.format(date))
    diff = days_from_now(date)

    if(diff < 0):
        diff = date_diff(
            datetime.date(datetime.date.today().year + 1, date.month, date.day),
            datetime.date.today())

    print('Its {} days to your next birthday'.format(diff))


def main():
    print_header()
    bday = get_input()
    print_user_info(bday)


if __name__ == "__main__":
    main()
