import random

class Blackjack:
    def __init__(self):
        self.deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
        self.userHand = []
        self.dealerHand = []

    # Initial Card Dealing
    def deal(self):
        """Deal two cards to the user and dealer."""
        # Dealing Two cards to user and dealer
        self.userHand.append(self.hit())
        self.dealerHand.append(self.hit())
        
        self.userHand.append(self.hit()) 
        self.dealerHand.append(self.hit())
        
    # Hit Method
    def hit(self):
        """Draw a card from the deck."""
        if not self.deck:
            return None
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
    
    def calculate_hand(self, hand):
        """Calculate the total value of a hand. Assuming standing on soft 17."""
        total = sum(hand)
        
        usable_aces = hand.count(0)
        
        # Adjust for Aces
        while usable_aces > 0 and total <= 10:
            total += 11
            usable_aces -= 1
            
        total += usable_aces
            
        return total
        
    # Determine Winner
    def determine_winner(self):
        """Determine the winner based on the hands."""
        user_score = self.calculate_hand(self.userHand)
        dealer_score = self.calculate_hand(self.dealerHand)
        
        print(f"Your score: {user_score}, Dealer's score: {dealer_score}")
        
        if user_score > 21:
            print("You busted! Dealer wins.")
        elif dealer_score > 21 or user_score > dealer_score:
            print("You win!")
        elif user_score < dealer_score:
            print("Dealer wins!")
        else:
            print("It's a tie!")
        
    def play(self):
        """Start the game."""
        self.deal()
        print(f"Your hand: {self.userHand}, Dealer's hand: {self.dealerHand[0]} and a hidden card.")
        
        while True:
            action = input("Do you want to hit or stand? (h/s): ").strip().lower()
            
            # Hit Action
            if action == 'h':
                card = self.hit()
                if self.userHand == 21:
                    break
                if card is None:
                    print("No more cards in the deck!")
                    break
                self.userHand.append(card)
                
                if self.calculate_hand(self.userHand) > 21:
                    print(f"Your hand: {self.userHand} - You busted! Dealer wins.")
                    return
                
                print(f"Your hand: {self.userHand}")
                
            # Stand Action
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' to hit or 's' to stand.")
        
        # Dealer stands soft on 17 or higher
        while self.calculate_hand(self.dealerHand) < 17:
            self.dealerHand.append(self.hit())
        
        print(f"Dealer's hand: {self.dealerHand}")
        self.determine_winner()
        
if __name__ == "__main__":
    game = Blackjack()
    game.play()