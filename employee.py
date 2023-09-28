"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, wage, contract_hours=0):
        self.name = name
        self.wage = wage
        self.contract_hours = contract_hours

    def comission(self, comission_amount, contracts=0):
        self.comission_amount = comission_amount
        self.contracts = contracts

    def get_pay(self):
        wage = self.wage
        if self.contract_hours:
            wage *= self.contract_hours
        try:
            comission = self.comission_amount
            if self.contracts:
                comission *= self.contracts
        except:
            comission = 0
        return wage + comission

    def __str__(self):
        str = self.name + " "
        if self.contract_hours:
            str += f"works on a contract of {self.contract_hours} hours at {self.wage}/hour"
        else:
            str += f"works on a monthly salary of {self.wage}"
        try:
            if self.contracts:
                str += f" and receives a commission for {self.contracts} contract(s) at {self.comission_amount}/contract."
            else:
                str += f" and receives a bonus commission of {self.comission_amount}."
        except:
            str += "."
        str += f" Their total pay is {self.get_pay()}."
        return str


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000)
renee.comission(200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150)
jan.comission(220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000)
robbie.comission(1500)

# Ariel works on a contract of 120 hour at 30/hour and sreceives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120)
ariel.comission(600)
