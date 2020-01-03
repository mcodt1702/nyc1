#class tutorial

class Employee:

    raise_amount = 1.12


    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Marco', 'Coronado', 120000)
emp_2 = Employee('Sose', 'Canseco', 40000)
emp_3 = Employee('marcela', 'menchaca', 70000)
emp_4 = Employee('Hernan', 'Vela', 70000)


print(emp_1.fullname(), emp_1.pay)
emp_1.raise_amount = 1.30
emp_1.apply_rise()
print(emp_1.fullname())
print(f"Exito!!! {emp_1.fullname()}, ${emp_1.pay}")
print(f"Exito!!! {emp_2.fullname()}, ${emp_2.pay}")
print(f"Exito!!! {emp_4.fullname()}, ${emp_4.pay}")
