import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
	tweet_file = open(sys.argv[1])

	for line in tweet_file:
		tweet = json.loads(line)
		if "place" in tweet:
			print tweet["place"]#.keys()		
	  
if __name__ == '__main__':
    main()
