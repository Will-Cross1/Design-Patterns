# Factory Method interface
class PaymentFactory:
    """
    Factory Method base class.
    
    Defines the method that the factory creation subclasses must use
    This allows object creation in subclasses reducing coupling between client and payment classes
    """
    def create_payment(self):
        pass


# The payment method classes used by the factory. As shown, they do not inherit anything.
# While they can all inherit a pay class, this is not necessary for the factory method to work in this example.
class CardPayment:
    """
    What will be created by the factory.
    Contains the payment processing logic.
    """
    def pay(self, amount):
        print("Processing card details...")
        print(f"Card payment: £{amount}")


class PayPalPayment:
    """
    What will be created by the factory.
    Contains the payment processing logic.
    """
    def pay(self, amount):
        print("Connecting to PayPal servers...")
        print(f"PayPal payment: £{amount}")


class CryptoPayment:
    """
    What will be created by the factory.
    Contains the payment processing logic.
    """
    def pay(self, amount):
        print("Initialising blockchain...")
        print("Routing through dark web...")
        print(f"Crypto payment: £{amount}")


# Factory classes for each payment type. This can be done in a single factory class with a parameter,
# but this is easier to extend and understand for demonstration purposes
class CardPaymentFactory(PaymentFactory):
    """
    Creates CardPayment object.
    """
    def create_payment(self):
        return CardPayment()


class PayPalPaymentFactory(PaymentFactory):
    """
    Creates PayPalPayment object.
    """
    def create_payment(self):
        return PayPalPayment()


class CryptoPaymentFactory(PaymentFactory):
    """
    Creates CryptoPayment object.
    """
    def create_payment(self):
        return CryptoPayment()


# Client class
class Basket:
    """
    The client using the Factory Method.

    The Basket does not need to know the exact payment class being created.
    It only interacts with the factory interface.
    """
    def __init__(self, amount):
        self.amount = amount
        self.payment = None # No selected method yet

    def select_payment_factory(self, factory):
        # The factory creates the payment object.
        # This is done per switch in payment method
        self.payment = factory.create_payment()

    def checkout(self):
        if not self.payment:
            print("Please select a payment method first!")
            raise ValueError("No payment method selected")

        self.payment.pay(self.amount)


def factory_examples():
    # The factory creates the selected payment object.
    # The Basket does not depend on the original payment classes.
    print(" Card payment example:")
    basket = Basket(92.50)
    basket.select_payment_factory(CardPaymentFactory())
    basket.checkout()
    print("")

    # The payment type can be changed by creating a different object,
    # but this requires creating a new payment object through another factory.
    # This is why the Strategy pattern is more flexible, as it allows changing the strategy without creating a new object.
    print(" PayPal payment example, with switching:")
    basket = Basket(31.03)
    basket.select_payment_factory(CryptoPaymentFactory())
    basket.select_payment_factory(PayPalPaymentFactory())
    basket.checkout()


if __name__ == "__main__":
    factory_examples()