import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	sent = {}	
	for line in sent_file:
		line = line.strip()
		parts = [p.strip() for p in line.split("\t")]
		sent[parts[0]] = parts[1]
	tweet = {}	
	for line in tweet_file:
		tweet = json.loads(line)
		if tweet.has_key('delete'):
			print "deleted"
		else:
			score = 0.0
			for word in tweet["text"].split():
				if sent.has_key(word):
					score = score + float(sent[word])
			print float(score)
	  
if __name__ == '__main__':
    main()
