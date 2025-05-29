# Importing the random module to let the AI randomly choose a move
import random
# Importing sys to allow graceful program exit
import sys

# Define the RPS class
class RPS:
    # Constructor that runs when an object is created
    def __init__(self):
        print("Welcome to RPS 9000!")
        # Dictionary mapping user-readable move names to emojis
        self.moves: dict = {'rock': '🪨', 'paper': '📰', 'scissors': '✂'}
        # Creating a list of valid moves from the dictionary keys
        self.valid_moves: list[str] = list(self.moves.keys())

    # Method to play one round of the game
    def play_game(self):
        # Ask the user for input
        user_move: str = input('rock, paper or scissors? >> ').lower()

        # If the user wants to exit
        if user_move == 'exit':
            print("Thanks for playing!")
            sys.exit()

        # Check for invalid inputs
        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()

        # Randomly select a move for the AI
        ai_move: str = random.choice(self.valid_moves)

        # Show both moves using emojis
        self.display_moves(user_move, ai_move)
        # Decide the winner
        self.check_moves(user_move, ai_move)

    # Method to display both user's and AI's moves
    def display_moves(self, user_move: str, ai_move: str):
        print('---')
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print('---')

    # Method to determine the winner
    def check_moves(self, user_move: str, ai_move: str):
        # It's a tie if both moves are the same
        if user_move == ai_move:
            print("It's a tie!")
        # All winning conditions for the user
        elif (user_move == 'rock' and ai_move == 'scissors') or \
             (user_move == 'scissors' and ai_move == 'paper') or \
             (user_move == 'paper' and ai_move == 'rock'):
            print("You win!")
        # All other cases: AI wins
        else:
            print("AI wins...")

# Main execution starts here
if __name__ == '__main__':
    # Create a game instance
    rps = RPS()
    # Loop to keep playing until user exits
    while True:
        rps.play_game()
