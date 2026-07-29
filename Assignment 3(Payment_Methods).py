class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self,report):
        pass
      
#Concrete Strategies
class CreditCard(PaymentMethod):

    def make_payment(self,amount):
        print(f"\nPayment of ${amount} completed through Credit Card.")

class DebitCard(PaymentMethod):

     def make_payment(self,amount):
         print(f"\nPayment of ${amount} completed through Debit Card")

class UPI(PaymentMethod):

    def make_payment(self, amount):
        print(f"\nPayment of ${amount} completed through UPI.")


class NetBanking(PaymentMethod):

    def make_payment(self, amount):
        print(f"\nPayment of ${amount} completed through Net Banking.")
      
# Context Class
class PaymentSystem:

    def __init__(self):
        self.payment_mode = None

    def choose_method(self, method):
        self.payment_mode = method

    def pay_amount(self, amount):
        if self.payment_mode:
            self.payment_mode.make_payment(amount)
        else:
            print("No payment method selected.")
          
# Driver Program
system = PaymentSystem()

methods = {
    1: CreditCard(),
    2: DebitCard(),
    3: UPI(),
    4: NetBanking()
}
while True:
    print("\n Payment Processing System ")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    try:
        option = int(input("Enter your choice: "))

        if option == 5:
            print("Thank you for using the Payment Processing System!")
            break

        if option not in methods:
            print("Invalid choice! Please try again.")
            continue

        amount = float(input("Enter payment amount: "))

        system.choose_method(methods[option])
        system.pay_amount(amount)

    except ValueError:
        print("Please enter valid numeric values.")
         
