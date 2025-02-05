from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Usage
def make_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

credit = CreditCardProcessor()
paypal = PayPalProcessor()

make_payment(credit, 100)   # Output: Processing credit card payment of $100
make_payment(paypal, 200)   # Output: Processing PayPal payment of $200