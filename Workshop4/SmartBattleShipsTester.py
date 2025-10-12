from SmartBattleShips1 import SmartBattleShips

for N in (8,10,12,16,20):
	b = SmartBattleShips(N)
	g = b.test()
	print(f'N = {N}: Average guesses = {g}')
