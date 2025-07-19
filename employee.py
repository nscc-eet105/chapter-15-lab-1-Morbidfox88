#Chad Collard
#Employee lab
#7/19/2025

class Employee:
    def __init__(self, name, worked, rate):
        self.__name = name
        self.__worked = worked
        self.__rate = rate

    def set_name(self, name):
        self.__name = name

    def set_worked(self, worked):
        self.__worked = worked

    def set_rate(self ,rate):
        self.__rate = rate

    def get_name(self):
        return self.__name

    def get_worked(self):
        return self.__worked

    def get_rate(self):
        return self.__rate

    def calc_pay(self):
        hours_worked = self.__worked
        hourly_rate = self.__rate
        total_pay = hours_worked * hourly_rate
        return total_pay

class Salesperson(Employee):
    def __init__(self, name, worked, rate, sales, commission):
            super().__init__(name, worked, rate)
            self.__sales = sales
            self.__commission = commission

    def set_sales(self, sales):
            self.__sales = sales

    def set_commission(self, commission):
            self.__commission = commission

    def get_sales(self):
        return self.__sales

    def get_commission(self):
        return self.__commission

    def calc_pay(self):
        base_pay = super().calc_pay()
        commission_earned = self.__sales * self.__commission
        total_pay = base_pay + commission_earned
        return total_pay

    

    
