import random
import time

class Player():
    def __init__(self, player_type="pc",cards=[], bet=0, name="", amount=0):

        self.name=name
        self.player_type=player_type
        self.cards=cards
        self._bet=bet
        self.amount=amount

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, amount):
        self._bet=self._bet+amount
        self.amount=self.amount-amount

    def place_initial_bet(self):
        while True:
            amount= input(f"Place initial bet amount. Your current amount is {self.amount}:")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n <= self.amount:
                    #self.amount = self.amount-n
                    #self.bet=n
                    return n

                print(f"Amount must range between 1 and {self.amount}")
                print("Try again")
            else:
                print(f"Kindly enter amount between 1 and {self.amount}")

    def call_fold_raise(self, player):
        choice=input("Press 1 to call \n Press 2 to fold \n Press 3 to raise")
        if choice =='1':
            return self.call(player)

        if choice == '2':
            return self.fold(player)

        if choice == '3':
            return self.raise_stake(player)
        print(f"Wrong choice {choice}. Choose 1,2 or 3")
        self.call_fold_raise(player)

    def call(self, player):
        print("Amount bet is", player.amount)
        diff=self.bet-player.bet

        if diff>0:
            return True
        diff=abs(diff)

        if self.amount > abs(diff):
            print("Cannot call! You do not have enough amount!")
            return "l"
        self.bet=diff
        print(f"Icall your bet. \n I bet {diff}")


    def fold(self, player):
        print("I fold!!")
        return "l"

    def raise_stake(self, player):
        raise_amount=input(f"Enter raise amount: Max amount you can raise is {self.amount}")
        raise_amount=int(raise_amount)
        if raise_amount>self.amount:
            print("You cannot raise more than your current amount")
            self.raise_stake(player)
            return
        print(f"I raise amount by {raise_amount}")
        self.bet = raise_amount
        #self.amount=self.amount=raise_amount
        return raise_amount



    def auto_match_or_raise(self,amount):
        print("PC calculating move...")
        time.sleep(3)
        to_do=random.randint(1,2)
        raise_amount=amount+random.randint(10,250)

        if raise_amount>self.amount:
            to_do=1

        if to_do ==1:
            if self.amount>amount:
                #self.amount-amount
                self.bet=amount
                print(f"Matching your action. Bet = {amount}")
                return amount
            else:
                return "l"

        #self.amount=self.amount-raise_amount
        self.bet=raise_amount
        print("FEELING LUCKY. I raise by", raise_amount)
        return raise_amount


    def update_amount_bet(self,amount):
        self.total_amount_bet=self.total_amount_bet+amount


    def reset_amount_bet(self):
        self.total_amount_bet=0