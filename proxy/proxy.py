from abc import ABCMeta, abstractmethod

class You:
    def __init__(self):
        print("You - let's buy the a T-shirt!")
        self.debitCard = DebitCard()
        self.isPurschased = None
    
    def make_payment(self):
        self.isPurschased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurschased:
            print("You - T-shirt is mine :)")
        else:
            print("You - I should earn more :(")

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def __getAccount(self):
        self.account = self.card # suponho o numero de cartão = numero conta

        return self.account
    def __hasFunds(self):
        print("Bank - checking whether or not account",self.__getAccount()," has funds")
        return True 

    def setCard(self,card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print("Bank - Paying your k-dam tshirt!")
            return True
        else:
            print("Bank - Sorry, you are poor and has not enough funds!")

class DebitCard(Payment):
    def __init__(self):
        self.bank=Bank()
    def do_pay(self):
        card = input("Proxy - Punch in card number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

you = You()
you.make_payment()