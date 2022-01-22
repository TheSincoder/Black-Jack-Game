# Create a Black Jack game




print("Club -> \u2663")
print("Spades -> \u2660")
print("Diamond -> \u2666")
print("Heart -> \u2665")

import random
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Create a Dictionary of the cards in a deck
sum_cards = 0

cards = {
    '\u2663A':11 if sum_cards<21 else 1,
    '\u2663K':10,
    '\u2663Q':10,
    '\u2663J':10,
    '\u266310':10,
    '\u26639':9,
    '\u26638':8,
    '\u26637':7,
    '\u26636':6,
    '\u26635':5,
    '\u26634':4,
    '\u26633':3,
    '\u26632':2,
    '\u2660A':11 if sum_cards<21 else 1,
    '\u2660K':10,
    '\u2660Q':10,
    '\u2660J':10,
    '\u266010':10,
    '\u26609':9,
    '\u26608':8,
    '\u26607':7,
    '\u26606':6,
    '\u26605':5,
    '\u26604':4,
    '\u26603':3,
    '\u26602':2,
    '\u2666A':11 if sum_cards<21 else 1,
    '\u2666K':10,
    '\u2666Q':10,
    '\u2666J':10,
    '\u266610':10,
    '\u26669':9,
    '\u26668':8,
    '\u26667':7,
    '\u26666':6,
    '\u26665':5,
    '\u26664':4,
    '\u26663':3,
    '\u26662':2,
    '\u2665A':11 if sum_cards<21 else 1,
    '\u2665K':10,
    '\u2665Q':10,
    '\u2665J':10,
    '\u266510':10,
    '\u26659':9,
    '\u26658':8,
    '\u26657':7,
    '\u26656':6,
    '\u26655':5,
    '\u26654':4,
    '\u26653':3,
    '\u26652':2,
    }

# print(cards)

shuffled_deck = list(cards.keys())
random.shuffle(shuffled_deck)



# Create a class for the Dealer
# Dealer gets 1 face up card and face down card
# if Dealers cards = 21 round over (User Loses)
# face down card is revealed when user 'stays'

class Dealer():
    def __init__ (self):
        self.dsum = 0
        self.dcards = {}
        

# Create a class for the user
# both cards face up 
# options to 'hit'(get another card) or 'stay'(finish round)
# check and print sum as user gets the cards and after each hit

class Player():
    def __init__ (self,):
        self.psum = 0
        self.pcards = {}
        



# Create a class for the UI
# shuffle deck
# place a bet
# distribute 2 cards to dealer and 2 cards to user

class UI():

    dsum_list = []
    psum_list = []

    # def __init__ (self):
        
        # self.dealer = Dealer()
        # self.player = Player()
        


    # to show DEALERS hand, but moved to hit()
    # def dealer_hand(self):
    #     for i in cards:
    #         dealer_cards = []
    #         i = 0
    #         if len(dealer_cards) < 2:
    #             # dc = {[key for key in cards.keys()][i]}
    #             dealer_cards.append(shuffled_deck[0])
    #             shuffled_deck.remove(shuffled_deck[0])
    #             dealer_cards.append(shuffled_deck[0])
    #             shuffled_deck.remove(shuffled_deck[0])
    #             # print(f"dealer's cards are: {dealer_cards}") to test the shuffle in the dealer's hand
    #             print("Dealer's Cards:")
    #             print(f'[ ] [{dealer_cards[1]}]')
    #             break

    #     for k, v in cards.items():
    #         if k in dealer_cards:
    #             self.dsum_list.append(v)
    #     dsum = sum(self.dsum_list)
    #     # print(dsum) --> to test the for loop 

    #     if dsum == 21:
    #         print(f'[{[key for key in cards.keys()][i]}] [{[key for key in cards.keys()][i+1]}]')
    #         print(f"Dealer's hand = {dsum}! You LOSE!!!")


    # to show players hand, but moved to hit()
    # def player_hand(self):
    #     for i in cards:
    #         player_cards = []
    #         i = 0
    #         if len(player_cards) < 2:
    #             # dc = {[key for key in cards.keys()][i]}
    #             player_cards.append(shuffled_deck[0])
    #             shuffled_deck.remove(shuffled_deck[0])
    #             player_cards.append(shuffled_deck[0])
    #             shuffled_deck.remove(shuffled_deck[0])
    #             # print(f"dealer's cards are: {dealer_cards}") to test the shuffle in the dealer's hand
    #             print("Dealer's Cards:")
    #             print(f'[{player_cards[0]}] [{player_cards[1]}]')
    #             break

    #     for k, v in cards.items():
    #         if k in player_cards:
    #             self.psum_list.append(v)
    #     psum = sum(self.psum_list)
    #     print(f'Your Cards = {psum}')

    #     if psum == 21:
    #         print(f'[{[key for key in cards.keys()][i]}] [{[key for key in cards.keys()][i+1]}]')
    #         print(f"Dealer's hand = {psum}! You LOSE!!!")

    

    # How many chips do you want? (int)
    def chips(self):
        while True:
            chips = input("How many chips do you want? [0=quit] ")
            print(f'You have {chips} chips available to bet')
            if int(chips) == 0:
                break
            elif int(chips) >= 1:
                break
            else:
                print("Invalid Response, need a number from you Hot Shot!")
    # bet_response how much do you want to bet? (int)
    def bet(self):
        
        while True:
            bet = input("How many chips would you like to bet? [0=quit] ")
            print(f'Your bet is {bet}')
            if int(bet) == 0:
                break
            # elif int(bet) > int(x):
                
            #     print("You don't have enough chips High Roller")
            elif int(bet) >= 1:
                break
                           
            else:
                print("Invalid Response, need a number from you Big Money!")


    # dealer hits if dsum < 17 | if dealer breaks (dsum > 21) then game over, player wins | if dealer hits Black Jack (dsum = 21) then game over, Dealer Wins
    # hit_response would you like to Hit or Stay? if hit get another card. if stay, reveal the dealers cards and complete the round. 
    # give chips, take chips or have mafia break legs
    def hit(self):
        clear_screen()
        #Dealer 
        for i in cards:
            dealer_cards = []
            i = 0
            if len(dealer_cards) < 2:
                # dc = {[key for key in cards.keys()][i]}
                dealer_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                dealer_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                # print(f"dealer's cards are: {dealer_cards}") to test the shuffle in the dealer's hand
                
                break

        

        #Player
        for i in cards:
            player_cards = []
            i = 0
            if len(player_cards) < 2:
                # dc = {[key for key in cards.keys()][i]}
                player_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                player_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                # print(f"dealer's cards are: {dealer_cards}") to test the shuffle in the dealer's hand
               
                break

        
        # print(f'Your Cards = {psum}')

        

        while True:
            #Dealer
            for k, v in cards.items():
                if k in dealer_cards:
                    self.dsum_list.append(v)
            dsum = sum(self.dsum_list)


            #Player
            for k, v in cards.items():
                if k in player_cards:
                    self.psum_list.append(v)
            psum = sum(self.psum_list)
            print("Dealer's Cards:")
            print(f'[ ] [{dealer_cards[1]}]')
            print('\n')
            print("Your Cards:")
            print(player_cards)
            print(f'Your Cards = {psum}')
            hit = input("Would you like to HIT/STAY? ")
            if hit.lower() == 'stay':

                

                print(dealer_cards)
                print(f"Dealer's cards = {dsum}")
                print('\n')
                print(player_cards)
                print(f"Your cards = {psum}")

                if dsum < 17:
                    dealer_cards.append(shuffled_deck[0])
                    shuffled_deck.remove(shuffled_deck[0])
                    print(dealer_cards)
                    dsum = 0
                    dsum = sum(self.dsum_list)
                    print(dsum)

                elif dsum > 21:
                    print("YOU WIN!!!")
                    # self.chips += self.bet
                    break

                elif psum > 21:
                    print("YOU LOSE!!!")
                    # self.chips -= self.bet
                    break
                
                
                elif psum > dsum:
                    print("YOU WIN!!!")
                    # self.chips += self.bet
                    break
                elif psum <= dsum:
                    print("YOU LOSE!!!")
                    # self.chips -= self.bet
                    break
            elif hit.lower() == 'hit':
                clear_screen()
                player_cards.append(shuffled_deck[0])
                shuffled_deck.remove(shuffled_deck[0])
                print(player_cards)
                
                print(psum)

            else:
                print('Invalid Response')

    def round(self):
        while True:
            round_over = input("Would you like to Cash out or place a bet? Cash/Bet ")
            if round_over.lower() == 'cash':
                print(f"You left the table with {self.chips} chips")
                break
            elif round_over.lower() == 'bet':
                break
            else:
                print("Invalid Response, please review your options and select appropriately")


    def game(self):
        while True:
            start_response = input('Do you want to play a game? Y/N ')
            if start_response.lower() == 'y':
                # self.chips()
                # while True:
                #     self.round()
                #     while True:
                #         self.bet()
                while True:
                    self.hit()
                    # we want round to go to bet go to hit then back to bet
                
            elif start_response.lower() == 'n':
                break
            else:
                print("Invalid Response, it's literally just 1 letter, you can do this Buttercup")

run = UI()
run.game()
    










# if the sum of the dealers cards < 17 distribute more cards (recurrence)
# [0] [1] [2] [3]
#     i = 4 (deal out a card[i])
#     i += 1

# deal 2 cards to the dealer, reveal 1

# deal 2 cards to the player, reveal both
# hit = another card
# stay = complete the round by revealing the dealers other card and comparing the sums
# tie goes to the dealer
# display WIN or LOSE and calculate money


# if user wins double the bet, if user loses subtract bet from user total
      # self.roundOver = False
        # if self.dsum = 21:
        #     self.roundOver = True
        # elif self.dsum > self.psum



# place bet
# if you win gain bet dollars
# if you lose you lose bet dollars
# once dollars == 0 game over

# turn money into chips
# bet chips per round
# when chips = 0
# do you want to buy more chips?
# if no: Game over. If yes: input money

# after each round prompt:
# cash out or play another round? (cash/round)