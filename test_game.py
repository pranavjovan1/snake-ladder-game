"""
Unit tests for Snake and Ladder Game
"""

import pytest
from snake_ladder_game import SnakeLadderGame


class TestSnakeLadderGame:
    """Test cases for SnakeLadderGame class"""
    
    def test_game_initialization(self):
        """Test that game initializes correctly"""
        game = SnakeLadderGame(2)
        assert game.num_players == 2
        assert game.players == {1: 0, 2: 0}
        assert game.current_player == 1
        assert game.game_over is False
    
    def test_snake_setup(self):
        """Test that snakes are set up correctly"""
        game = SnakeLadderGame(2)
        snakes = game.snakes
        assert 17 in snakes
        assert snakes[17] == 4
        assert len(snakes) == 7
    
    def test_ladder_setup(self):
        """Test that ladders are set up correctly"""
        game = SnakeLadderGame(2)
        ladders = game.ladders
        assert 3 in ladders
        assert ladders[3] == 22
        assert len(ladders) == 9
    
    def test_dice_roll(self):
        """Test that dice roll returns valid value"""
        game = SnakeLadderGame(2)
        for _ in range(100):
            roll = game.roll_dice()
            assert 1 <= roll <= 6
    
    def test_normal_move(self):
        """Test normal player movement"""
        game = SnakeLadderGame(2)
        new_pos, final_pos, message = game.move_player(1, 5)
        assert game.players[1] == 5
        assert final_pos == 5
        assert "moved to 5" in message
    
    def test_snake_movement(self):
        """Test player hits a snake"""
        game = SnakeLadderGame(2)
        game.players[1] = 15
        new_pos, final_pos, message = game.move_player(1, 2)
        assert game.players[1] == 4  # Snake at 17 goes to 4
        assert "Snake" in message
        assert "Slid down" in message
    
    def test_ladder_movement(self):
        """Test player climbs a ladder"""
        game = SnakeLadderGame(2)
        game.players[1] = 1
        new_pos, final_pos, message = game.move_player(1, 2)
        assert game.players[1] == 22  # Ladder at 3 goes to 22
        assert "Ladder" in message
        assert "Climbed up" in message
    
    def test_move_beyond_board(self):
        """Test that player cannot move beyond position 100"""
        game = SnakeLadderGame(2)
        game.players[1] = 98
        current_pos, final_pos, message = game.move_player(1, 5)
        assert game.players[1] == 98  # Should stay at current position
        assert "Cannot move beyond" in message
    
    def test_winner_detection(self):
        """Test winner detection"""
        game = SnakeLadderGame(2)
        game.players[1] = 100
        assert game.check_winner() is True
        assert game.winner == 1
        assert game.game_over is True
    
    def test_no_winner(self):
        """Test no winner when no one at 100"""
        game = SnakeLadderGame(2)
        game.players[1] = 50
        game.players[2] = 75
        assert game.check_winner() is False
        assert game.game_over is False
    
    def test_board_state(self):
        """Test board state display"""
        game = SnakeLadderGame(2)
        game.players[1] = 10
        game.players[2] = 20
        state = game.get_board_state()
        assert "Player 1: Position 10" in state
        assert "Player 2: Position 20" in state
    
    def test_board_visual(self):
        """Test board visual display"""
        game = SnakeLadderGame(2)
        visual = game.display_board_visual()
        assert "Board Visual" in visual
        assert "Legend" in visual
        assert "Ladder" in visual
        assert "Snake" in visual
    
    def test_multiple_players(self):
        """Test game with 3 and 4 players"""
        for num_players in [2, 3, 4]:
            game = SnakeLadderGame(num_players)
            assert len(game.players) == num_players
            assert all(pos == 0 for pos in game.players.values())
    
    def test_player_turn_rotation(self):
        """Test that player turns rotate correctly"""
        game = SnakeLadderGame(3)
        assert game.current_player == 1
        game.current_player = (game.current_player % 3) + 1
        assert game.current_player == 2
        game.current_player = (game.current_player % 3) + 1
        assert game.current_player == 3
        game.current_player = (game.current_player % 3) + 1
        assert game.current_player == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
