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

    def reset_bet(self):
        self._bet=0

    def place_initial_bet(self):
        while True:
            amount= input(f"Place initial bet amount. Your current amount is {self.amount}:")

            if amount.isdigit():
                n=int(amount)
                if n>0 and n <= self.amount:
                    #self.amount = self.amount-n
                    #self.bet=n
                    return n

                print(f"Amount must range between 1 and {self.amount} :")
                print("Try again")
            else:
                print(f"Kindly enter amount between 1 and {self.amount} :")

    def call_fold_raise(self, player):
        choice=input("Press 1 to call \n Press 2 to fold \n Press 3 to raise :")
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

        if diff > self.amount:
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



    def auto_call_raise(self,player, k):
        print("PC calculating move...")
        time.sleep(3)
        to_do=random.randint(1,2)
        
        print(f"Human bet amount is ", player.bet)
        print(f"PC amount is ", self.bet)
        diff=player.bet-self.bet
        print("Difference is ", diff)

        if diff <=0:
            print("I call your bet.")
            return 

        if diff > self.amount:
            print("I fold. The bet too high!")
            return "l"

        raise_amount=random.randint(1, 50)
        raise_stake=diff+raise_amount
        if raise_stake>self.amount or k>=3:
            to_do=1

        if to_do ==1:
            self.bet= diff
            print(f"Matching your action. Bet = {amount}")
            return
            

        #self.amount=self.amount-raise_amount
        self.bet=raise_stake
        print("FEELING LUCKY. I raise by", raise_amount)
        

    def auto_match_or_raise(self, amount):
        print("PC calculating move...")
        time.sleep(3)
        to_do=random.randint(1,2)
        raise_amount=random.randint(1, 50)

        if raise_amount>self.amount:
            to_do=1

        if to_do ==1:
            if self.amount > amount:
                print(f"Matching your action. Bet = {amount}")
                return amount 
            else:
                return "l"   
        self.bet=raise_amount
        print("FEELING LUCKY. I raise by", raise_amount)
        return raise_amount
    
    #def update_amount_bet(self,amount):
        #self.total_amount_bet=self.total_amount_bet+amount


    #def reset_amount_bet(self):
        #self.total_amount_bet=0