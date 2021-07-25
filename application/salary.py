from application.db.workers_wage import workers_wages


class Salary:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        for k, v in workers_wages.items():
            print(f'{k} {v}')
