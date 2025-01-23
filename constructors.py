class Employee:
    company='google'
    location='bengaluru'
    ceo='sundar pichai'
    def __init__(self,name,emp_id,salary):
      print('employe object created')
      self.name=name
      self.emp_id=emp_id
      self.salary=salary
    def emp_info(self):
        print(f'employee of {Employee.company}')
        print(f'employee name={self.name}')
        print(f'empolyee id={self.emp_id}')
        print(f'empolyee salary={self.salary}')
      # first commit on git
john=Employee('john cena',420,50000)
print(john.__dict__)
john.emp_info()




