import random

def choose_options():
  options = ('piedra','papel', 'tijera') # Tupla

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('La opcion escogida no es valida', '\n')
    # continue
    return None, None
    
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option,'\n')
  return user_option, computer_option
  
def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano! \n')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano! \n')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('El usuario gano \n')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gana! \n')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano! \n')
      user_wins += 1
    else:
      print('piedra gana a papel')
      print('computer gano! \n')
      computer_wins += 1
  return user_wins, computer_wins
  
def check_winners(user_wins, computer_wins):
  if computer_wins == 2:
    print('El ganador es la computadora!!')
    exit()
  
  if user_wins == 2:
    print('El ganador es el usuario')
    exit()

  
def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  
  while True:
    
    print('***' * 10)
    print('ROUND', rounds)
    print('***' * 10,'\n')
  
    print('Computer Wins =>',computer_wins)
    print('USer Wins =>',user_wins, '\n')
    rounds += 1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    check_winners(user_wins, computer_wins)



run_game()