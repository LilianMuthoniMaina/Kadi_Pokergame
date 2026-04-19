from Game import Game

def play_game():
    game=Game()

    human=game.human
    pc=game.pc

    game.turn=human

    human_amount=human.place_initial_bet()
    #human.update_amount_bet(human_amount)
    human.bet=human_amount

    pc_amount=pc.auto_match_or_raise(human_amount)
    #pc.update_amount_bet(pc_amount)
    pc.bet=pc_amount

    if pc_amount == "l":
        print("Towel throw!! Human won")
        return

    game.turn=human
    #game.pot=pc_amount+human_amount

    k = 0

    print("INITIATING FIRST BETTING ROUND")
    print("-------------------------------")

    while True:
        print("-------------------------------")
        print("Round ", k)
        print("-------------------------------")
        if k >= 1 and pc.bet == human.bet:
            print("Both players have matched bets. End of betting round.")
            break
        k = k + 1
        human_choice = human.call_fold_raise(player=pc)
        if human_choice == "l":
            print("Towel throw!! PC won")
            return  
        print("--------------------------------")
        print("Human betamount ", human.bet)
        print("Human amount ", human.amount)
        

        pc_choice = pc.auto_call_raise(player=human,k=k)

        if pc_choice == "l":
            print("Towel throw!! Human won")
            return

        print("--------------------------------")
        print("PC bet amount ", pc.bet)
        print("PC amount ", pc.amount)
        print("--------------------------------")
        
    print("-----------------------------")
    print("Betting round complete")
    print("------------------------------")
    deck= game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.community_cards.append(deck.give_card())
    game.print_community_card()

    print("----------------------------------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()

    print("All the bet amount moved to the betting pot")
    print("POT AMOUNT ", game.pot)
    print("-----------------------------------------------")
    print("Initializing second betting round")

    k=0
    while True:
        if k>0 and pc.bet == human.bet:
            print("All bets are equal. End of betting round")
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice =="l":
            print("PC WON THE GAME")
            return

        print("----------------------------------")
        print("Human bet amount", human.bet)
        print("Human amount", human.amount)

        pc_choice=pc.auto_call_raise(player=human, k=k)

        if pc_choice=="l":
            print("Human won")
            return

        print("Pc bet amount", pc.bet)
        print("Pc amount", pc.amount)
        print("----------------------------------")

    print("Second betting round complete")
    print("----------------------------------")
    deck=game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("-----------------------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()
    print("All the bet amount moved to pot ")
    print("POT AMOUNT", game.pot)
    print("---------------------------------")
    print(" Starting final betting round")
    print("---------------------------------")


    k=0
    while True:
        if k>0 and pc.bet==human.bet:
            print("All bets are equal. Ending betting round")
            break
        k=k+1

        human_choice=human.call_fold_raise(player=pc)

        if human_choice=="l":
            print("Pc won game")
            return

        print("----------------------------")
        print("Human bet amount", human.bet)
        print("Human amount", human.amount)

        pc_choice=pc.auto_call_raise(player=human,k=k)

        if pc_choice=="l":
            print("Human Won")
            return

        print("pc bet amount", pc.bet)
        print("pc amount", pc.amount)
    print("---------------------------------")
    print("Third betting round complete")
    print("----------------------------------")
    deck=game.deck
    deck.burn_card()
    game.community_cards.append(deck.give_card())
    game.print_community_card()
    print("-----------------------------------")
    game.pot=human.bet+pc.bet
    human.reset_bet()
    pc.reset_bet()

    print("All bet money moved to betting pot")
    print("POT AMOUNT", game.pot)
    print("-----------------------------------")
    print("Initializing 3rd betting round")
    print("-----------------------------------")






play_game()