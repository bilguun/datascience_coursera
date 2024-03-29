import sys
import json

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	sent = {}
	new_terms = {}	
	for line in sent_file:
		line = line.lower().strip()
		parts = [p.strip() for p in line.split("\t")]
		sent[parts[0]] = parts[1]
	tweet = {}	
	for line in tweet_file:
		tweet = json.loads(line)
		if not tweet.has_key('delete'):
			score = 0.0
			tweet_terms = {}
			for word in tweet["text"].lower().split():
				if sent.has_key(word):
					score = score + float(sent[word])
				else:
					tweet_terms[word] = 0.0
			for key in tweet_terms:
				tweet_terms[key] = score	
				if key in new_terms:
					new_terms[key] += tweet_terms[key]
				else:
					new_terms[key] = tweet_terms[key]
			
	for key in new_terms:
		print key.encode('utf8') + " " + str(new_terms[key]).encode('utf8')
				
if __name__ == '__main__':
    main()
