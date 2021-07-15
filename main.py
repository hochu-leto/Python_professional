import datetime

from application.db.people import get_employees
from application.salary import calculate_salary


def main():
    calculate_salary()
    get_employees()
    print(f'Сегодня {datetime.date.today()}')  #


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

