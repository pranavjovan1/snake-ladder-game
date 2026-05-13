"""
Snake and Ladder Game
A Python implementation of the classic Snake and Ladder board game
"""

import random
from typing import Dict, List, Tuple


class SnakeLadderGame:
    """A class to represent the Snake and Ladder game"""
    
    BOARD_SIZE = 100
    
    def __init__(self, num_players: int = 2):
        """
        Initialize the game with specified number of players
        
        Args:
            num_players (int): Number of players (default: 2)
        """
        self.num_players = num_players
        self.players = {i + 1: 0 for i in range(num_players)}
        self.snakes = self._setup_snakes()
        self.ladders = self._setup_ladders()
        self.current_player = 1
        self.game_over = False
        self.winner = None
        
    def _setup_snakes(self) -> Dict[int, int]:
        """
        Setup snake positions on the board
        Snakes go from higher position to lower position
        
        Returns:
            Dict mapping snake head position to tail position
        """
        snakes = {
            17: 4,
            54: 31,
            62: 19,
            87: 24,
            93: 73,
            95: 75,
            98: 79
        }
        return snakes
    
    def _setup_ladders(self) -> Dict[int, int]:
        """
        Setup ladder positions on the board
        Ladders go from lower position to higher position
        
        Returns:
            Dict mapping ladder start position to end position
        """
        ladders = {
            3: 22,
            5: 14,
            9: 31,
            20: 38,
            32: 61,
            42: 84,
            51: 67,
            57: 72,
            71: 91
        }
        return ladders
    
    def roll_dice(self) -> int:
        """
        Simulate rolling a six-sided dice
        
        Returns:
            int: Random number between 1 and 6
        """
        return random.randint(1, 6)
    
    def move_player(self, player_id: int, dice_value: int) -> Tuple[int, int, str]:
        """
        Move a player based on dice value
        
        Args:
            player_id (int): The player ID
            dice_value (int): The value rolled on dice
            
        Returns:
            Tuple containing:
            - new position
            - final position (after snake/ladder)
            - message describing the move
        """
        current_position = self.players[player_id]
        new_position = current_position + dice_value
        
        # Check if position exceeds board size
        if new_position > self.BOARD_SIZE:
            return current_position, current_position, f"Player {player_id} rolled {dice_value}. Cannot move beyond {self.BOARD_SIZE}. Stay at position {current_position}."
        
        # Check for snakes
        if new_position in self.snakes:
            snake_to = self.snakes[new_position]
            message = f"Player {player_id} rolled {dice_value} and moved to {new_position}. Oh no! Snake! Slid down to {snake_to}."
            self.players[player_id] = snake_to
            return new_position, snake_to, message
        
        # Check for ladders
        if new_position in self.ladders:
            ladder_to = self.ladders[new_position]
            message = f"Player {player_id} rolled {dice_value} and moved to {new_position}. Great! Ladder! Climbed up to {ladder_to}."
            self.players[player_id] = ladder_to
            return new_position, ladder_to, message
        
        # Normal move
        self.players[player_id] = new_position
        message = f"Player {player_id} rolled {dice_value} and moved to {new_position}."
        return new_position, new_position, message
    
    def check_winner(self) -> bool:
        """
        Check if any player has reached the winning position
        
        Returns:
            bool: True if there's a winner, False otherwise
        """
        for player_id, position in self.players.items():
            if position == self.BOARD_SIZE:
                self.winner = player_id
                self.game_over = True
                return True
        return False
    
    def play_turn(self) -> str:
        """
        Execute one turn for the current player
        
        Returns:
            str: Message describing the turn result
        """
        if self.game_over:
            return f"Game Over! Player {self.winner} has won!"
        
        dice_value = self.roll_dice()
        new_pos, final_pos, message = self.move_player(self.current_player, dice_value)
        
        # Check for winner
        if self.check_winner():
            return message + f"\n🎉 Player {self.winner} has reached position {self.BOARD_SIZE} and won the game! 🎉"
        
        # Move to next player
        self.current_player = (self.current_player % self.num_players) + 1
        
        return message
    
    def get_board_state(self) -> str:
        """
        Get current state of all players
        
        Returns:
            str: Formatted string showing all player positions
        """
        state = "Current Board State:\n"
        for player_id, position in sorted(self.players.items()):
            state += f"Player {player_id}: Position {position}\n"
        return state
    
    def display_board_visual(self) -> str:
        """
        Display a visual representation of the board with player positions
        
        Returns:
            str: Visual board representation
        """
        board = ["." for _ in range(self.BOARD_SIZE + 1)]
        
        # Mark snakes
        for snake_head in self.snakes:
            board[snake_head] = "S"
        
        # Mark ladders
        for ladder_start in self.ladders:
            board[ladder_start] = "L"
        
        # Mark players
        for player_id, position in self.players.items():
            if position > 0:
                board[position] = str(player_id)
        
        # Create visual output
        visual = "Board Visual (Positions 1-100):\n"
        for i in range(1, self.BOARD_SIZE + 1, 10):
            row = [board[j] if j <= self.BOARD_SIZE else "." for j in range(i, min(i + 10, self.BOARD_SIZE + 1))]
            visual += f"{i:3d}-{min(i+9, self.BOARD_SIZE):3d}: {' '.join(row)}\n"
        
        visual += "\nLegend:\n"
        visual += "  L = Ladder\n"
        visual += "  S = Snake\n"
        visual += "  1-{} = Player\n".format(self.num_players)
        visual += "  . = Empty\n"
        
        return visual


def main():
    """Main game loop for interactive play"""
    print("=" * 50)
    print("Welcome to Snake and Ladder Game!")
    print("=" * 50)
    
    # Get number of players
    while True:
        try:
            num_players = int(input("\nHow many players? (2-4): "))
            if 2 <= num_players <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Initialize game
    game = SnakeLadderGame(num_players)
    
    print("\nGame initialized!")
    print(game.get_board_state())
    print(game.display_board_visual())
    
    # Game loop
    turn_count = 0
    while not game.game_over:
        input(f"\nPlayer {game.current_player}'s turn - Press Enter to roll dice...")
        turn_count += 1
        result = game.play_turn()
        print(result)
        print("\n" + game.get_board_state())
        
        if turn_count % 4 == 0:  # Show board visual every 4 turns
            print(game.display_board_visual())
    
    print("\n" + "=" * 50)
    print(f"Game ended after {turn_count} turns!")
    print("=" * 50)


if __name__ == "__main__":
    main()
