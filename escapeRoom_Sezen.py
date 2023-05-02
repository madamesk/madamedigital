# Text-Based Advemture Game
# Your goal is to survive

# making the rooms

# diamond room
def dining_room():
  # some prompts
  print("\nYou are now in the dining room, you are very thursty and you see a bottle !")
  print("And there is a door too!")
  print("What would you do? (1 or 2)")
  print("1). Take the liquid from the bottle and go through the door.")
  print("2). Just go through the door.")
  
  # take input()
  answer = input(">")
  
  if answer == "1":
    # the player is dead, call game_over() function with the "reason"
    game_over("The liquid is poisend! The moment you drink it, you die!")
  elif answer == "2":
    # the player won the game
    print("\nNice, you're are very smart! Congrats you reached the garden! you win the game!")
    # activate play_again() function
    play_again()
  else:
    # call game_over() with "reason"
    game_over("Go and learn how to type a number.")

# monster room
def kitchen_room():
  # some prompts
  # '\n' is to print the line in a new line
  print("\nNow you entered the kitchen with a zombie bird!")
  print("The zombie bird is sleeping.\nWhat would you do? (1 or 2)")
  print("1). Go back, left the kitchen an close the door silently.")
  print("2). Kill the zombie bird and show your courage!")

  # take input()
  answer = input(">")

  if answer == "1":
    # lead him to the diamond_room()
    dining_room()
  elif answer == "2":
    # the player is dead, call game_over() with "reason"
    game_over("The zombie bird was hungry, he/it ate you.")
  else:
    # game_over() with "reason"
    game_over("Go and learn how to type a number.")


# function to ask play again or not
def play_again():
  print("\nDo you want to play again? (y or n)")
  
  # convert the player's input to lower_case
  answer = input(">").lower()

  if "y" in answer:
    # if player typed "yes" or "y" start the game from the beginning
    start()
  else:
    # if user types anything besides "yes" or "y", exit() the program
    exit()


# game_over function accepts an argument called "reason"
def game_over(reason):
  # print the "reason" in a new line (\n)
  print("\n" + reason)
  print("Game Over!")
  # ask player to play again or not by activating play_again() function
  play_again()


def start():
  # give some prompts.
  print("\nYou are standing in a dark room with a key in your hand.")
  print("There are two doors one to your left and the other to your right , which one do you take? (l or r)")
  
  # convert the player's input() to lower_case
  answer = input(">").lower()

  if "l" in answer:
    # if player typed "left" or "l" lead him to bear_room()
    dining_room()
  elif "r" in answer:
    # else if player typed "right" or "r" lead him to monster_room()
    kitchen_room()
  else:
    # else call game_over() function with the "reason" argument
    game_over("Don't you know how to type something properly?")


# start the game
start()