from Player_Interface import Player_Interface  # Importing the Player_Interface class from a module called Player_Interface
game = Player_Interface()  # Creating an instance of the Player_Interface class
# Continuously run the game loop while the game is running
while game.running:
    game.curr_menu.display_menu()  # Display the current menu of the game
    game.game_loop()  # Execute the game loop

