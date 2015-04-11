# Input file
fname = "D-trial"
# fname = "D-small-attempt0"
# fname = "D-large"
inputfile = fname + ".in"
outputfilename = fname + ".out"
lines = [line.strip() for line in open(inputfile)]
# print lines

steps = int(lines.pop(0))
result = list()

# print lines
# Solution
for nTest in xrange(0, steps):
	foundSolution = False
	(x, r, c) = map(int, lines[nTest].split(" "))
	print ((nTest + 1), x, r, c)

	if (x == 1):
		print ">> x equals 1"
		foundSolution = True
	elif (r * c % x == 0):
		# there is number of x in r*c
		if (r >= x) and (c >= x):
			print ">> can't do longer"
			foundSolution = True
		elif (x >= 7) and (r >= 3) and (c >= 3):
			pass # RICHARD locks GABRIEL with one cell inside the square
		else:
			(a, b) = (1, x)
			while (a <= b+1):
				# print (a, b)
				foundSolution = True
				
				if (((a > c) and (b > c)) or ((a > r) and (b > r))):
					# print "<< aha"
					foundSolution = False
					break

				a = a + 1
				b = b - 1

	if (foundSolution):
		result.append("GABRIEL")
	else:
		result.append("RICHARD")

# Output file
# print result
outputfile = open(outputfilename, 'w')
for nCase in xrange(0, len(result)):
	outputfile.write("Case #%d: %s\n" % ((nCase + 1), (result[nCase])) )
