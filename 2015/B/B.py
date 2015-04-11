# Input file
fname = "B-trial"
# fname = "B-small-attempt0"
# fname = "B-large"
inputfile = fname + ".in"
outputfilename = fname + ".out"
lines = [line.strip() for line in open(inputfile)]
# print lines

steps = int(lines.pop(0))
result = list()

# print lines
# Solution

for nTest in xrange(0, steps):
	result.append(0)

# Output file
# print result
outputfile = open(outputfilename, 'w')
for nCase in xrange(0, len(result)):
	outputfile.write("Case #%d: %d \n" % ((nCase + 1), (result[nCase])) )
