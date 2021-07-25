from application.salary import Salary
from application.people import People


def main():
    accountant = Salary('accountant')
    employees = People('workers')
    while True:
        command = input('Введите команду: ')
        if command == 'c':
            accountant.calculate_salary()
        if command == 'g':
            employees.get_employees()
        if command == 'e':
            break


if __name__ == '__main__' :
    main()