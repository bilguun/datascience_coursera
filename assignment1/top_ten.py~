import sys
import json

def main():
	tweet_file = open(sys.argv[1])
	
	tweet = {}
	hashtags = {}
	
	for line in tweet_file:
		tweet = json.loads(line)
		if "entities" in tweet and tweet['entities']['hashtags']:
				for hashtag in tweet['entities']['hashtags']:
					if hashtag["text"] in hashtags:
						hashtags[hashtag["text"]] = hashtags[hashtag["text"]] + 1.0
					else:	 		
						hashtags[hashtag["text"]] = 1.0			
	i = 1
	for w in sorted(hashtags, key=hashtags.get, reverse=True):
		print w, hashtags[w]
		i += 1
		if i > 10:
			break
			
if __name__ == '__main__':
    main()
