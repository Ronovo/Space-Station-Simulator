import json
import os

class Game:
    """Static utility class with game-wide functions"""

    @staticmethod
    def save_character(player_data,character_data):

        Game.save_game(player_data)

    @staticmethod
    def save_game(player_data):
        """Save the game to a JSON file"""
        # Create saves directory if it doesn't exist
        if not os.path.exists("game/saves"):
            os.makedirs("game/saves")
        
        # Save game to JSON file
        filename = f"game/saves/{player_data.get("Player Name")}.json"
        try:
            with open(filename, "w") as f:
                json.dump(player_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    @staticmethod
    def load_player_data(filename, base_path):
        """Load a saved game from file"""
        # Remove .json extension if present (though it should be passed without it now)
        if filename.endswith(".json"):
            filename = filename[:-5]

        # Load game data from the correct path
        file_path = os.path.join(base_path, "game", "saves", filename + ".json")  # Updated path
        with open(file_path, "r") as f:
            player_data = json.load(f)
            return player_data

    @staticmethod
    def check_player_saves(base_path):
        file_path = os.path.join(base_path, "game", "saves")
        if not os.path.exists(file_path):
            return True
        if not os.path.isdir(file_path):
            return False # Not a directory
        return not os.listdir(file_path)