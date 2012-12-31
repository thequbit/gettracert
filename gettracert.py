import subprocess
import sys

# get the traceroute for the hostname
def get_route(hostname):
	
	# create the command to execute
	cmd = "traceroute -w 1 %s" % hostname

	# execute the command
	p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	
	# create an array to return
	hops = []

	# iterate through the resulting lines of text and add them to the array of hops
	for line in p.stdout.readlines():
		# add the hop to the list
		hop = "%s %s" % (line[4:].split(" ")[0], line[4:].split(" ")[1])
		hops.append(hop)

	# return the array of hops
	return hops

# main entry point
def main(argv):

	print "Reading in hostnames to perform traceroute on ..."

	# open our file of hostnames and read in all of the lins
	lines = tuple(open('hostlist.txt', 'r'))

	print "... done"

	print "Running traceroute on %i hosts ..." % len(lines)

	# open up the output csv file
	f=open('./hops.csv', 'w')

	# write headers to csv file
	f.write("Host, Hop 0, Hop 1, Hop 2, Hop 3, Hop 4, Hop 5, Hop 6, Hop 7, Hop 8, Hop 9,\n")

	# iterate through the host list and get the route for each host
	for host in lines:
	
		# remove the newline from our host name
		host = host.rstrip()
	
		print "\t Traceroute on %s ..." % host

		# get the hops for the host
		hops = get_route(host)

		print "\t ... done"

		# create the line to write to the file
		line = ", ".join(hops)

		# write the line to the csv file
		f.write("%s, %s\n" % (host,line))

	# close our output file
	f.close()

	print "... done"

# jump to our entry point
if __name__ == '__main__': sys.exit(main(sys.argv))

