from Card import Card
import random

class Deck():
    def __init__(self):

        ranks=Card.RANKS
        suites=Card.SUITES
        deck=[]

        for rank in ranks:
            for suite in suites:
                card=Card(suite=suite,rank=rank)
                deck.append(card)
                #print("rank", rank)
                #print("suite", suite)


        self.deck=deck
        #for card in deck:
            #card.printCard()

    def shuffle(self):
        newDeck=[]
        deck=self.deck

        while True:
            if len(deck)==1:
                card=deck[0]
                newDeck.append(card)
                break

            n=random.randint(0,len(deck)-1)

            card=deck[n]
            deck.pop(n)
            newDeck.append(card)

        print("new Deck Length", len(newDeck))
        print("old Deck Length", len(deck))

        for card in newDeck:
            card.printCard()
        self.deck=newDeck

        

    def print_deck(self):
        deck=self.deck

        for card in deck:
            card.printCard()

    def burn_card(self): #top card put below of deck
        print("before burn card")
        self.print_deck()
        print("after burn card")
        top_card=self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()

        

    def give_card(self): # take top card from deck, 
        top_card=self.deck[0]
        self.deck.pop(0)
        return top_card


if __name__=="__main__":
    d1=Deck()
    d1.shuffle()
    d1.burn_card()
    card=d1.give_card()
    print("given card is")
    d1.print_deck()

