# Strategy interface
class PaymentStrategy:
    """
    The strategy interface
    Has the method that all strategies must implement
    """
    def pay(self, amount):
        pass

# The strategies for this design pattern. One for each payment method
class CardPayment(PaymentStrategy):
    """
    The Card payment strategy.
    This would have Card processing logic, but for this example, it just uses prints.
    """
    def pay(self, amount):
        print("Processing card details...")
        print(f"Card payment: £{amount}")

class PayPalPayment(PaymentStrategy):
    """
    The PayPal payment strategy.
    This would have PayPal processing logic, but for this example, it just uses prints.
    """
    def pay(self, amount):
        print("Connecting to PayPal servers...")
        print(f"PayPal payment: £{amount}")

class CryptoPayment(PaymentStrategy):
    """
    The Crypto payment strategy.
    This would have Crypto processing logic, but for this example, it just uses prints.
    """
    def pay(self, amount):
        print("initialising blockchain...")
        print("Routing through dark web...")
        print(f"Crypto payment: £{amount}")


# The context class that holds the current strategy and delegates checkout to it.
class Basket:
    """
    Context class.
    Holds the current payment strategy and delegates checkout to it.
    This is what the user interacts with.
    """
    def __init__(self, amount):
        self.amount = amount
        self.payment_strategy = None  # No strategy selected yet

    def set_payment_method(self, strategy):
        # Used to select Basket's payment strategy
        self.payment_strategy = strategy

    def checkout(self):
        # Executes the strategy's payment method
        if not self.payment_strategy:
            print("Please select a payment method first!")
            raise ValueError("No payment method selected")
        self.payment_strategy.pay(self.amount)


# Each time the user changes payment method, set_payment_method is called to change strategy.
# Below (in user_examples()) are examples only, in a real application, each function call would come from the UI directly and would not be hardcoded
def user_examples():
    # The user selects card payment, but forgot their card, so switches to PayPal.
    print(" Card to PayPal test:")
    basket = Basket(92.50)
    basket.set_payment_method(CardPayment())
    basket.set_payment_method(PayPalPayment())
    basket.checkout()
    print("")
    
    # The user goes a bit mad experimenting with the UI and switches payment methods a few times before settling on crypto
    print(" Random switching test:")
    basket = Basket(0.94)
    basket.set_payment_method(CardPayment())
    basket.set_payment_method(CryptoPayment())
    basket.set_payment_method(PayPalPayment())
    basket.set_payment_method(CryptoPayment())
    basket.set_payment_method(PayPalPayment())
    basket.set_payment_method(CardPayment())
    basket.set_payment_method(CryptoPayment())
    basket.checkout()
    print("")
    
    # The user just pays with their card and doesn't switch at all
    print(" Normal card test:")
    basket = Basket(975.70)
    basket.set_payment_method(CardPayment())
    basket.checkout()
    print("")
    
    # The user somehow manages to checkout without selecting a payment method.
    # this is caught and an error message is displayed
    print(" No payment method test:")
    basket = Basket(12.32)
    try:
        basket.checkout()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    # user has added some items to their basket, and has clicked finish and pay
    # This total is put into the basket object as the user is given the option to select payment method
    print(" PayPal test:")
    basket = Basket(5)
    basket.set_payment_method(PayPalPayment())
    basket.checkout()
    print("")
    
    # The user would normally select the method and pay, but we will mock some examples in the user_examples function to show the strategy pattern
    user_examples()
