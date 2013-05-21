import sys
import json

def main():
	tweet_file = open(sys.argv[1])
	tweet = {}
	word_freq = {}
	total_nwords = 0
	
	for line in tweet_file:
		tweet = json.loads(line)
		if "text" in tweet:
			for word in tweet["text"].split():
				if word in word_freq:
					word_freq[word] += 1.0
				else:
					word_freq[word] = 1.0
				total_nwords += 1
		
	for key in word_freq.keys():
		word_freq[key] = word_freq[key]/total_nwords
		print key.encode("utf8") + " " + str(word_freq[key]).encode("utf8")
			  	
if __name__ == '__main__':
    main()
