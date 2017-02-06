with open('bandit24.txt', 'w') as f:
	for i in range(0, 10000):
		s = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ ' + str(i).zfill(4) + '\n'
		f.write(s)
