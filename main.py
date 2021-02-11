import random

def action_responses(user_input):
  response = [
    "Really that's all? You humans can do anything yet you are so boring. What a sad species, wouldn't you agree?",
    "How fun, I wish I could do things like you humans, but I'm stuck here."
  ]
  return random.choice(response)

def final_responses(user_input):
  responses = [
    "You're annoying me now go away.",
    "You have not become any more interesting",
    "You continue boring me human make haste and exit my realm",
    "I was created by your species? How embarassing"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'
  
    
  user_input = input("Hello, I am Chat Bob, if you want to talk intruduce yourself! If you want to end this conversation at anytime enter the character 'q'.\n")
  
  while user_input != quit_character:
    user_input = input("Oh my it's nice to meet you! How are you doing?\n")

    user_input = input("Ah yes feelings, if only I as a program could understand what you meant better. What are you doing human?\n")

    user_input = input(action_responses(user_input) + "\n")

    user_input = input("You've begun to bore me human, become more interesting or leave me to be in peace, no more energy will be spent on this conversation.\n")


    while user_input != quit_character:
      user_input = input(final_responses(user_input) + "\n")
  if user_input == quit_character:
    print("Thank you for leaving me be.")

if __name__ == "__main__":
  init_chat()