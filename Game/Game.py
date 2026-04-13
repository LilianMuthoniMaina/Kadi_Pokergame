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

    @property
    def turn (self):
        return self._turn

    @turn.setter
    def turn(self, player):
        if isinstance(player,Player):
            self._turn=player
        else:
            raise ValueError("The turn must be assigned to player object")


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
