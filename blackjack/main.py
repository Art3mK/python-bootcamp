from deck import Deck
from card import Card
from player import Player

def main():
    deck = Deck()
    player_name = input("How do I call you?: ")

    human_player = Player(player_name, deck.pull_card(), deck.pull_card(), 200)
    computer = Player("Computer", deck.pull_card(), deck.pull_card(), 1000000,True)

    first_game = True

    while True:
        if not first_game:
            if play_next():
                reset_game(deck, human_player, computer)
            else: game_over()
        first_game = False
        bet = get_bet(human_player)
        computer.print_cards()
        serve_player(human_player,deck)
        if human_player.is_busted():
            print(f"{computer.name} won your {bet}!")
            human_player.lose_bet(bet)
            if human_player.bank < 1:
                print("Нету ручки - нет конфетки!")
                exit(0)
            continue
        else:
            computer.cards[0].secret = False
            computer.print_cards()
            # If player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet
            if human_player.has_21() and not computer.cards[1].rank in ["jack",10,"queen","king","ace"]:
                print(f"{human_player.name} won {bet*1.5}$ with blackjack!")
                human_player.win_bet(bet*1.5)
                continue
            while(computer.get_cards_value() < 17):
                computer.add_card(deck.pull_card())
                computer.print_cards()
            print("=========")
            computer.print_cards()
            print("=========")
            human_player.print_cards()
            if computer.is_busted() or human_player.get_cards_value() > computer.get_cards_value():
                print(f"Player wins {bet*1.5}€")
                human_player.win_bet(bet*1.5)
            elif human_player.get_cards_value() == computer.get_cards_value():
                print("tie!")
            else:
                print(f"Computer wins your {bet}!")
                human_player.lose_bet(bet)
                if human_player.bank < 1:
                    print("Нету ручки - нет конфетки!")
                    exit(0)


def get_bet(player):
    while True:
        try:
            bet = float(input(f"{player.name}, please place your bet (you have {player.bank}$): "))
            if player.can_place_bet(bet): return bet
        except ValueError:
            continue

def serve_player(player,deck):
    answer = ''
    while answer != 'n':
        player.print_cards()
        if player.is_busted() or player.has_21(): return
        answer = input(f"{player.name}, wanna hit? (y|n): ")
        if answer == 'y':
            player.add_card(deck.pull_card())

def play_next():
    answer = ''
    while answer not in ['y','n']:
        answer = input("Play again (y/n)?: ")
    return True if answer == 'y' else False

def reset_game(deck, player, computer):
    deck.reset()
    player.reset_cards(deck.pull_card(),deck.pull_card())
    computer.reset_cards(deck.pull_card(),deck.pull_card())
    computer.cards[0].secret = True

def game_over():
    print("Good luck!")
    exit(0)

if __name__ == "__main__":
    main()
