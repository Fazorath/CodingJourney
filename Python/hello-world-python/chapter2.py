banned_users = ['Yoenis', 'Alberto', 'Yannah']
prompt = "\nAdd a player to your Team"
prompt += "\nEnter 'Quit' When youre done"

players = []
while True:
  player = input(prompt)
  if player == 'Quit':
    break
  elif player in banned_users:
    print(f"{banned_users} is Banned !")
    continue
  else:
    players.apppend(player)

print("\nYour Team:")
for player in players:
  print(player)