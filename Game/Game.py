from Deck import Deck
from Player import Player

class Game():
    def __init__(self):
        self.pot=0
        deck=Deck()
        deck.shuffle()
        human_cards=[deck.give_card(), deck.give_card()]
        pc_cards=[deck.give_card(), deck.give_card()]
        self.human=Player(player_type = "human", cards=human_cards, bet=0, name="Booboo Kitty", amount=5000)
        self.pc= Player(player_type="pc", cards=pc_cards, bet=0, name="PC", amount=4500)

        self._turn=self.human
        self.deck =deck
        self.community_cards=[]

    @property
    def turn (self):
        return self._turn

    @turn.setter
    def turn(self, player):
        if isinstance(player,Player):
            self._turn=player
        else:
            raise ValueError("The turn must be assigned to player object")
    

    def print_community_card(self, rank=None):
        print("Community cards")
        for card in self.community_cards:
            if card.rank == rank:
                return card

            if rank is None:
                card.printCard()

        return None

    def check_royal_flush(self, cards):
        royal=["A", "K", "Q", "J", "10"]
        checked_cards=[]

        for rank in royal:
            card=self.check_rank_card(cards=cards, rank=rank)
            if card:
                checked_cards.append(card)
            else:
                return None

        return
        for i, rank in enumerate(royal):
            found=False
            for j, card in enumerate(cards):
                if card.rank==rank:
                    found=True
                    checked_cards.append(card)
                    break
            if found==True:
                continue
            return None

        suite=checked_cards[0].suite
        for card in checked_cards:
            if suite != card.suite:
                return None

        return True

    def check_straight_flush(self):
        pc_cards=self.community_cards+self.pc.cards
        human_cards=self.community_cards+self.human.cards



if __name__=="__main__":
        game =Game()
        game.deck.print_deck()
        print("This is thee deck")
        print("PC cards")
        game.pc.cards[0].printCard()
        game.pc.cards[1].printCard()
        print("This is thee deck")
        print("Human cards")
        game.human.cards[0].printCard()
        game.human.cards[1].printCard()
