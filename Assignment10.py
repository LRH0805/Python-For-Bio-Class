#!/usr/bin/python
import sys
import math

def ave_stderr(x): #defining function we are creating using variable x (array)
	ave = sum(x)/len(x) #sum of numbers over amount of numbers
	#print "mean: %f" % ave

	ssq = 0.0
	for y in x:
		ssq += (y-ave)*(y-ave) #sum of squares 

	#print "ssq: %f" % ssq	

	var = ssq/(len(x) -1) #calculate variance
	#print "var: %f" % var

	sdev = math.sqrt(var) #math package sqrt function
	#print "stdev: %f" % sdev

	stderr = sdev / math.sqrt(len(x)) #calculate standard error
	#print "stderr %f" %stderr

	return (ave,stderr) #after calculating, send back to where it was sent from
	
# end ave_stderr

fname = sys.argv[1]

user_numbers = []
handle = open(fname, "r")
i=1
for line in handle:
	linearr = line.split()
	for s in linearr[i:]:
		user_numbers.append(float(s))
	i +=1
handle.close()

#print user_numbers
(a,s) = ave_stderr(user_numbers)
print "%f +/- %f" % (a,s)
