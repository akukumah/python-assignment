##i will attempt to model a simple tither payer's calculator 
       
#instance 



class Tithe:
    """Computes the tithe amount based on income and a discount percentage."""

    def __init__(self, income, discount=10):
        """Initialize the tithe calculator with income and discount percentage."""
        self.income = float(income)
        self.discount = discount

    def get_tithe(self):
        """Compute the tithe amount based on the income and discount."""
        result = self.income * self.discount / 100
        return int(result)


name = input("Please enter your name: ")
income = input("Enter your income (do not include currency): ")

# Create a Tithe instance
tithe_calculator = Tithe(income)

# Compute the tithe
tithe_amount = tithe_calculator.get_tithe()

print(f"Dear {name.title()}, you would pay {tithe_amount} cedis as your tithe")
