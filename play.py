from src.client.game_engine import GameEngine
from src.client.user_input.terminal import Terminal

# you are able to create any client interface by changing the user_input
client_terminal = Terminal()
GameEngine(user_input=client_terminal).execute()