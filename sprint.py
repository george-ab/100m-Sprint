from msvcrt import getch
import os, sys, time

lines = []
key_pressed = False
counter = 0
if not(os.path.isfile('highscores.txt')):
	file = open('highscores.txt', 'w')
	file.write('George\n')
	file.write('0')
else:
	try:
		file = open('highscores.txt', 'r')
		for line in file: lines.append(line)
		file.close()
	except:
		print('Error reading file. Applying temporary fix')
		lines = ['George', '0']

name = lines[0]
high_score = lines[1]

def run():
	if(counter % 10 == 0):
		print(str(counter) + 'm')


while True:
	print('''
	##########################################################
	#                   100m sprint                          #
	#                                                        #
	#           Tap Q and W as fast as you can               #
	#                                                        #
	#               Press enter to start                     #
	##########################################################
		''')
	print('High Score: {} by {}'.format(high_score, name))
	input()
	os.system('cls')

	start_time = time.time()
	while counter <= 100:
		key = ord(getch())

		if(key == 113 and not key_pressed):
			# 'Q' Key
			key_pressed = True
			run()
			counter += 1
		elif(key == 119 and key_pressed):
			# 'W' Key
			key_pressed = False
		else:
			pass

	fin_time = time.time() - start_time
	fin_time = round(fin_time,2)
	os.system('cls')
	print('YOU WIN! TIME: ' + str(fin_time))
	if(float(fin_time) < float(high_score)):
		print('You got the high score!')
		name = input('Name: ')
		high_score = fin_time
		file = open('highscores.txt', 'w')
		file.write(name + '\n')
		file.write(str(high_score))
		file.close()
	counter = 0
	os.system('cls')
