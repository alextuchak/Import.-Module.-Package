from application.db.staff import staff


class People:
    def __init__(self, name):
        self.name = name

    def get_employees(self):
        for k, v in staff.items():
            print(f'{k} {v}')