#!/usr/bin/python

# Input file
# fname = "B-trial"
# fname = "B-small-attempt0"
# fname = "B-small-attempt1"
# fname = "B-small-attempt2"
# fname = "B-small-attempt3"
fname = "B-small-attempt4"
# fname = "B-large"
inputfile = fname + ".in"
outputfilename = fname + ".out"
lines = [line.strip() for line in open(inputfile)]
# print lines

steps = int(lines.pop(0))
result = list()

# print lines
# Solution

def splitPancakes( num ):
	if (num % 2 == 0):
		return (num/2, num/2)
	else:
		return ((num-1)/2, ((num-1)/2)+1)

for nTest in xrange(0, steps):
	specialMinutes = 0
	splitResults = list()
	
	dinners = int (lines[2 * nTest])
	pancakes = sorted(map(int, lines[2 * nTest + 1].split(" ")))
	print (nTest+1, dinners, pancakes)

	# minuteTaken = 0
	splitResults.append(max(pancakes))
	while (max(pancakes) > 3):
		currentSplit = splitPancakes(max(pancakes))
		# if (currentSplit[1] + specialMinutes + 1 < max(pancakes) + specialMinutes):
		specialMinutes += 1
		pancakes[len(pancakes)-1] = currentSplit[0]
		pancakes.append(currentSplit[1])
		pancakes = sorted(pancakes)
		splitResults.append(max(pancakes) + specialMinutes)
		print ("N:", pancakes, specialMinutes, max(pancakes) + specialMinutes, min(splitResults))
		# else:
		# 	break

	result.append(min(splitResults))

# Output file
# print result
outputfile = open(outputfilename, 'w')
for nCase in xrange(0, len(result)):
	outputfile.write("Case #%d: %d\n" % ((nCase + 1), (result[nCase])) )
