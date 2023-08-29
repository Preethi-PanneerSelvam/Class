class emp:
    def __init__(self,ID,Name,Salary):
        self.id=ID
        self.name=Name
        self.salary=Salary
    def show(self):#poly
        print("Hi my id is",self.id,"name is",self.name,"salary is ",self.salary)
    def update(aaa,new_name):
        aaa.name=new_name

class tcs(emp):
    def show(self):
        print("Hi my id is",self.id,"\tName is",self.name,"\tsalary is ",self.salary)
    def salary_hike(self):
        self.salary=self.salary + (0.05*self.salary)

class tcs_sales(tcs):
    def show(self):
        print("Hi my id is",self.id,"\tName is",self.name,"\tsalary is ",self.salary)
    def salary_inc(self):
        self.salary=self.salary +(0.1*self.salary)
e1=tcs(23,"sandeep",34000)
e2=tcs_sales(55,"kuldeep",67000)
e1.show()
e1.salary_hike()
e1.show()
e2.salary_hike()
e2.show()
e2.salary_inc()
e2.show()