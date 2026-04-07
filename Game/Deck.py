from Card import Card

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
        for card in deck:
            card.printCard()

    def shuffle():
        pass



    def remove_card():
        pass

    def add_to_end():
        pass


if __name__=="__main__":
    d1=Deck()

