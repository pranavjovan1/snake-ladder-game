# Snake and Ladder Game 🐍🪜

A classic Snake and Ladder board game implementation in Python with interactive gameplay for 2-4 players.

## Features

- **2-4 Player Support**: Play with friends or against multiple opponents
- **100-Square Board**: Standard board with strategic snake and ladder placements
- **7 Snakes**: Risk squares that slide you down the board
- **9 Ladders**: Reward squares that boost you up the board
- **Interactive Gameplay**: Real-time turn management and board updates
- **Visual Board Display**: See all player positions and obstacles at a glance
- **Dice Rolling**: Random dice rolls (1-6) for each turn
- **Winner Detection**: Automatic win detection when reaching position 100

## How to Play

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/pranavjovan1/snake-ladder-game.git
cd snake-ladder-game
```

2. Run the game:
```bash
python snake_ladder_game.py
```

3. Follow the prompts to:
   - Select number of players (2-4)
   - Take turns rolling the dice
   - Navigate the board with snakes and ladders
   - Reach position 100 to win!

### Game Rules

- Players start at position 0
- Each turn, roll a dice to move 1-6 squares
- Landing on a ladder climbs you up to a higher position
- Landing on a snake slides you down to a lower position
- Cannot move beyond position 100 (you must roll the exact number)
- First player to reach position 100 wins!

## Board Layout

```
Legend:
  L = Ladder (climb up!)
  S = Snake (slide down!)
  1-4 = Player number
  . = Empty square
```

## File Structure

```
snake-ladder-game/
├── snake_ladder_game.py    # Main game implementation
├── test_game.py            # Unit tests for game logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Code Structure

### SnakeLadderGame Class

Main game class with methods:
- `__init__(num_players)` - Initialize game
- `roll_dice()` - Simulate dice roll
- `move_player(player_id, dice_value)` - Handle player movement
- `check_winner()` - Check if anyone won
- `play_turn()` - Execute a player's turn
- `get_board_state()` - Get current positions
- `display_board_visual()` - Display visual board

## Example Game Session

```
==================================================
Welcome to Snake and Ladder Game!
==================================================

How many players? (2-4): 2

Game initialized!
Current Board State:
Player 1: Position 0
Player 2: Position 0

Board Visual (Positions 1-100):
  1-10: . . L . L . . . L .
...

Player 1's turn - Press Enter to roll dice...
Player 1 rolled 5 and moved to 5. Great! Ladder! Climbed up to 14.

Player 2's turn - Press Enter to roll dice...
Player 2 rolled 3 and moved to 3. Great! Ladder! Climbed up to 22.

```

## Snake and Ladder Positions

### Snakes (Position → Slide to)
- 17 → 4
- 54 → 31
- 62 → 19
- 87 → 24
- 93 → 73
- 95 → 75
- 98 → 79

### Ladders (Position → Climb to)
- 3 → 22
- 5 → 14
- 9 → 31
- 20 → 38
- 32 → 61
- 42 → 84
- 51 → 67
- 57 → 72
- 71 → 91

## Running Tests

```bash
python -m pytest test_game.py -v
```

## Requirements

- Python 3.7+
- No external dependencies required for basic gameplay
- pytest (for running tests)

## License

MIT License - See LICENSE file for details

## Author

Created by pranavjovan1

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests

## Future Enhancements

- [ ] Graphical UI with Tkinter/Pygame
- [ ] Network multiplayer support
- [ ] Save/load game state
- [ ] Leaderboard system
- [ ] Customizable board size and snakes/ladders
- [ ] AI opponent
- [ ] Sound effects and animations

---

**Enjoy the game! 🎮🎲**
