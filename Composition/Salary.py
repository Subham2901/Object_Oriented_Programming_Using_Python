class salary():
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def annual_salary(self):
        return (self.pay*12)+self.bonus