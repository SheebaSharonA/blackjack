

from random import shuffle
Values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
Suits=["Hearts","Spades","Clubs","Diamonds"]
Ranks=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=Values[rank]
        #print(self.value)
        
    def __str__(self):
        return self.rank+" of "+self.suit

class Deck():
   
    def __init__(self):
        self.card_deck=[]
        i=0
        for s in Suits:
            for r in Ranks:
                created_card=Card(s,r)
                i+=1
                self.card_deck.append(created_card)
        #print(i)
   
    def shuffle(self):
        return shuffle(self.card_deck)
        
    def draw_one(self):
        return self.card_deck.pop()
        
    def __str__(self):
        deck_comp=" "
        for card in self.card_deck:
            deck_comp+="\n" + card.__str__()
        return "this deck contains:"+deck_comp
        
        
class Hand:
    def __init__(self):
        self.card=[]
        self.value=0
        self.aces=0
        
    def add_card(self,card):
        self.card.append(card)
        self.value+= card.value
        
        if card.rank== "Ace":
            self.aces+=1
    
    def adjust_aces(self):
        if self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
            
class Chips:
    def __init__(self):
        self.total=100
        self.bet=0
        
    def win_bet(self):
        self.total+=self.bet
        
    def lost_bet(self):
        self.total-=self.bet

#fucntions:
def take_bet(chips):
    on=True
    while on:
        try:
            x= int(input("Enter the bet"))
        except:
            print("Enter the valid number")
        else:
            if x>chips.total:
                print("The bet is higher than the total")
            else:
                chips.bet=x
                on=False
            

def hit(deck,hand):
    hand.add_card(deck.draw_one())
    hand.adjust_aces()
    
def hit_or_stand(deck,hand):
    global playing
    x= input("enter 'h' to hit or 's' to stand")
    if x.lower() =='h':
        hit(deck,hand)
        return True
            
    elif x.lower() =='s':
        print("Player has decided to stand")
        return False
        
    else:
        print("enter valid input")
        
        
def show_some(player,dealer):
    print("Player's cards:", *player.card, sep = '\n')
    print("Dealer's first card is hidden")
    print(f"Dealer's second cards: {dealer.card[1]}")
    
def show_all(player,dealer):
    print("Player's cards:", *player.card, sep = '\n')
    print("Player's Hand =",player.value)
    print("Dealer's cards:", *dealer.card, sep = '\n')
    print("Dealer's Hand =",dealer.value)
    
def player_busts(player,dealer,chips):
    print("Player busts so Dealer wins")
    chips.lost_bet()
    
def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("Dealer busts so Player wins")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.lost_bet()
    
def push(player,dealer,chips):
    print("Dealer and Player tie")
    
game_on=True  
while True:
    print("Welcome to Blackjack")
    deck = Deck()
    deck.shuffle()
    
    player_hand= Hand()
    player_hand.add_card(deck.draw_one())
    player_hand.add_card(deck.draw_one())
    
    dealer_hand= Hand()
    dealer_hand.add_card(deck.draw_one())
    dealer_hand.add_card(deck.draw_one())
     
    player_chips= Chips()
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    playing= True
    while playing:
        playing = hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            playing=False
            game_on=False
            
    if player_hand.value <= 21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
    
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
            
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)
        
        print("\nPlayer's winnings stand at",player_chips.total)
        cont = int(input("DO u wanna continue 1 for yes 0 for no"))
        if cont ==1 :
            game_on=True
        else:
            game_on= False
