import sys
import random

#make sure that a count parameter is passed in
if len(sys.argv) < 2:
    print "Error: Invalid number of parameters"
    print "Usage: nameGenerator.py {COUNT}"
    sys.exit()

count = int(sys.argv[1])

#make sure that count is a useful value
if count < 1:
    print "Error: COUNT should be an int greater than 0"
    print "Usage: nameGenerator.py {COUNT}"
    sys.exit()

firstnames = []
lastnames = []
fullnames = set()

#load firstnames
with open('firstNames.txt', 'r') as fnfile:
    for firstname in fnfile:
	firstnames.append(firstname)

#load lastnames
with open('lastNames.txt', 'r') as lnfile:
    for lastname in lnfile:
	lastnames.append(lastname)

#add firstname and lastname to set of fullnames until count reached.
while len(fullnames) < count:
    currentFirstName = firstnames[random.randint(0, len(firstnames)-1)]
    currentLastName = lastnames[random.randint(0, len(lastnames)-1)]
    currentFullName = currentFirstName[:-1] + "," + currentLastName[:-1]
    fullnames.add(currentFullName)

with open('names_list.csv', 'wb') as outfile:
    # add column headers (firstname, lastname)
    outfile.write('firstname,lastname\n')

    for name in fullnames:
	outfile.write(name + '\n')

