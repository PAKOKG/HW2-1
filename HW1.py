class Employee:
    emp_count = 0
    work_rate = 2

    def init (self, name, salary):
        self.name = name
        self.salary = salary

    def display_count(self):
       pass

    def display_employee(self):
        print ('Name of a worker: {}. Salary: {}'. format(self.name, self.salary))

    def change_name(self, new_name):
        self.name = new_name
    def change_salary(self, new_salary):
        self.salary = new_salary

    def get_total_salary(self):
        return self.salary


p1 = Employee('Pako', 1200)
p1.display_employee()
p1.change_name('Jorge')
p1.change_salary(15000)
p1.display_employee()

print(Emp2.name, Emp2.salary)
print(Emp1.name, Emp1.salary)
