import random

sum_cards = 0

cards = {
    '\u2663A':11, #if sum_cards<21 else 1,
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
    '\u2660A':11, #if sum_cards<21 else 1,
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
    '\u2666A':11, #if sum_cards<21 else 1,
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
    '\u2665A':11, #if sum_cards<21 else 1,
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
    '\u26652':2
    }

shuffled_deck = list(cards.keys())
random.shuffle(shuffled_deck)

# dealer_cards and player_cards pull from shuffled_deck
# pull the card and remove it from shuffled_deck
# then pull the value of the card from shuffled_deck that matches from the dictionary

# print(shuffled_deck) --> to test the shuffled deck

# print(cards['\u26652'])

# for i in cards:
#     print(i)

# for i in cards:
#     print(cards[i])

dsum_list = []
psum_list = []

def dealer_hand():
    for i in cards:
        dealer_cards = []
        i = 0
        
        # dc = {[key for key in cards.keys()][i]}
        dealer_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        dealer_cards.append(shuffled_deck[0])
        shuffled_deck.remove(shuffled_deck[0])
        # print(f"dealer's cards are: {dealer_cards}") to test the shuffle in the dealer's hand
        print("Dealer's Cards:")
        print(f'[ ] [{dealer_cards[1]}]')
        


            

    for k, v in cards.items():
        if k in dealer_cards:
            dsum_list.append(v)
    dsum = sum(dsum_list)
    # print(dsum) --> to test the for loop 

    if dsum == 21:
        print(f'[{[key for key in cards.keys()][i]}] [{[key for key in cards.keys()][i+1]}]')
        print(f"Dealer's hand = {dsum}! You LOSE!!!")
            
    
    # for k in range(dealer_cards):
    #     if k in cards:
    #         # dsum = cards.values(k)
    #         print(f'dealer has: {cards[k]}')
            
            
            
                
    #         dsum = sum(dealer_cards)
    #         if dsum == 21:
                
    #             print(f'[{[key for key in cards.keys()][i]}] [{[key for key in cards.keys()][i+1]}]')
    #             print(f"Dealer's hand = {dsum}! You LOSE!!!")
    #         # sum_dealer = sum(cards[i] for item in cards)
    #         # print(sum_dealer)
    #         # print(sum([value for value in cards.values()][i,i+1]))
    #         # else:
    #         # print(dealer_cards) --> this was a debugging test
    #         break


dealer_hand()



def player_hand():
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
            print("Your Cards:")
            print(f'[{player_cards[0]}] [{player_cards[1]}]')
            break

    for k, v in cards.items():
        if k in player_cards:
            psum_list.append(v)
    psum = sum(psum_list)
    print(f'Your Cards = {psum}')

    if psum == 21:
        print(f'[{[key for key in cards.keys()][i]}] [{[key for key in cards.keys()][i+1]}]')
        print(f"Dealer's hand = {psum}! You LOSE!!!")

player_hand()

# start_response Do you want to play? Y/N
    # if Y then start the fucking game, obviously...wtf you thinking?

def game():
    while True:
        start_response = input('Do you want to play a game? Y/N ')
        if start_response.lower() == 'y':
            continue
            
        elif start_response.lower() == 'n':
            break
        else:
            print("Invalid Response, it's literally just 1 letter, you can do this Buttercup")

# How many chips do you want? (int)
def chips():
    while True:
        chips = input("How many chips do you want? ")
        print(f'You have {chips} chips available to bet')
        if chips == int:
            continue
        else:
            print("Invalid Response, need a number from you Hot Shot!")
# bet_response how much do you want to bet? (int)
def bet():
    while True:
        bet = input("How many chips would you like to bet? ")
        print(f'Your bet is {bet}')
        if bet > chips:
            print("You don't have enough chips High Roller")
        elif bet == int:
            continue
        
        else:
            print("Invalid Response, need a number from you Big Money!")


# dealer hits if dsum < 17 | if dealer breaks (dsum > 21) then game over, player wins | if dealer hits Black Jack (dsum = 21) then game over, Dealer Wins
# hit_response would you like to Hit or Stay? if hit get another card. if stay, reveal the dealers cards and complete the round. 
# give chips, take chips or have mafia break legs
def hit(self):
    while True:
        print("Dealer's Cards:")
        print(f'[ ] [{self.dealer_cards[1]}]')
        print('\n')
        print("Your Cards:")
        print(f'[{self.player_cards[0]}] [{self.player_cards[1]}]')
        print(f'Your Cards = {self.psum}')
        hit = input("Would you like to HIT/STAY? ")
        if hit.lower() == 'stay':

            print(f'[{self.dealer_cards[0]}] [{self.dealer_cards[1]}]')
            print(f"Dealer's cards = {self.dsum}")
            print('\n')
            print(f'[{self.player_cards[0]}] [{self.player_cards[1]}]')
            print(f"Your cards = {self.psum}")
            if self.dsum < 17:
                self.dealer_cards.append(self.shuffled_deck[0])
                self.shuffled_deck.remove(self.shuffled_deck[0])
                print(self.dealer_cards)
                print(self.dsum)
            elif self.psum > self.dsum:
                print("YOU WIN!!!")
                self.chips += self.bet
            elif self.psum <= self.dsum:
                print("YOU LOSE!!!")
                self.chips -= self.bet
        elif hit.lower() == 'hit':
            self.player_cards.append(self.shuffled_deck[0])
            self.shuffled_deck.remove(self.shuffled_deck[0])
            print(self.player_cards)
            print(self.psum)
        else:
            print('Invalid Response')

def round():
    while True:
        round_over = input("WOuld you like to Cash out or place another bet? Cash/Bet ")
        if round_over.lower() == 'cash':
            print(f"You left the table with {chips} chips")
            break
        elif round_over.lower() == 'bet':
            self.bet()
        else:
            print("Invalid Response, please review your options and select appropriately")

def driver():
    game()
    while True:


        
    
    
    # print how many chips the player has during each round
    # if chips > 0 then start the fucking round
    
    # place the bet then shuffle and deal cards
    
    # round_response Round over, would you like to cash out or place another bet? Cash/Bet