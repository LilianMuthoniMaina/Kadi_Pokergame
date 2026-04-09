from Deck import Deck
from Player import player

class Game():
    def __init__(self):
        self.main_pot=0
        self.current_pot=0
        deck=Deck()
        deck.shuffle()
        human_cards=[deck.give_card(), deck.give_card()]
        pc_cards=[deck.give_card(), deck.give_card()]
        self.human=player(type = "human", cards=human_cards, total_amount_bet=0, name="Booboo Kitty", amount=5000)
        self.pc= player(type="pc", cards=pc_cards, total_amount_bet=0, name="PC", amount=4500)

        self.deck =deck


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
