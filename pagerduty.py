import sys

def calculatePercentage(lower, upper, intervals):
	"""
	Given a list of tuple integer pairs, this function returns the percentage 
	of at least one overlap within the specified integer upper and lower bounds

	Example call
	lower = 10
	upper = 20
	intervals = [(8,15),(18,19)]

	This will return 0.6 since (10,15) and (18,19) fall within bounds
	"""

	if lower == upper: return 0
	if lower > upper: return 0

	count = 0
	myLower = lower
	for interval in intervals:
		t1, t2 = interval
		if (t2 > lower) and (t2 < upper):
			count += t2 - max(lower, t1)
			lower = t2

		elif (t2 > lower) and (t1 >= lower) and (t1 < upper):
			count += upper - max(lower, t1)
			break

	return float(count) / (upper - myLower)

if __name__ == '__main__':
	queryWindowLine = ""
	try:
		queryWindowLine = raw_input()
	except:
		print "something went wrong!"

		
	queryWindowArr = queryWindowLine.split()
	if len(queryWindowArr) != 2:
		print "Badly formatted input, expected 2 values!: '%s'" % queryWindowLine

		
	lowerBound = upperBound = 0
	try:
		lowerBound = int(queryWindowArr[0])
		upperBound = int(queryWindowArr[1])
	except ValueError:
		print "Non numeric bounds for query window supplied!"

		
	numIncidents = 0
	try:
		numIncidents = int(raw_input())
	except ValueError:
		print "Non numeric value for number of incidents supplied!"

		
	intervals = []
	for i in range(numIncidents):
		incidentLine = ""
		try:
			incidentLine = raw_input()
		except:
			print "something went wrong"

			
		incidentArr = incidentLine.split()
		if len(incidentArr) != 2:
			continue

			
		try:
			triggerTime = int(incidentArr[0])
			resolveTime = int(incidentArr[1])

			intervals.append((triggerTime, resolveTime))
		except ValueError:
			print "Non numeric incident values supplied!"
			#sys.exit(1)
		
	print calculatePercentage(lowerBound, upperBound, intervals)
		

	

