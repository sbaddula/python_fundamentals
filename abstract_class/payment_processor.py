from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):

    def process_payment(self, amount):
        return f"Processing credit card payment for ${amount}"


processor = CreditCardProcessor()
print(processor.process_payment(200))