print('lets play the game of rock paper and scissor')
a=input('hey playor 1,whats your weapon?')
b=input('hey playor 1,whats your weapon?')
while True:
		if(a==b):
			print('you both are equally strong;)')
		elif(a =='rock'):
			if(b=='scissor'):
				print('playor 1 wins')
			else:
				print('playor 2 wins')
			if(str(input('do you want to play another game')))=='yes':
				continue
			else:
				print('thanks')
			break
		elif(a=='paper'):
			if(b=='rock'):
				print('playor 1 wins')
			else:
				print('playor 2 wins')
			if(str(input('do you want to play another game')))=='yes':
				continue
			else:
				print('thanks')
			break
		elif(a=='scissor'):
			if(b=='paper'):
				print('playor 1 wins')
			else:
				print('playor 2 wins')
			if(str(input('do you want to play another game')))=='yes':
				continue
			else:
				print('thanks')
			break
		else:
			print('ooops!! invalid input')


