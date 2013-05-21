import sys
import json

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	sent = {}	
	for line in sent_file:
		line = line.strip()
		parts = [p.strip() for p in line.split("\t")]
		sent[parts[0]] = parts[1]

	tweet = {}
	states = {}	

	for line in tweet_file:
		tweet = json.loads(line)
		
		if 'place' in tweet:
			if tweet['place']:
				if 'country_code' in tweet['place'] and tweet['place']['country_code'] == 'US':
					score = 0.0
					for word in tweet["text"].split():
						if word in sent:
							score = score + float(sent[word])
					state = tweet['place']['full_name'][-2:]
					if state in states:	
						states[state] = states[state] + score
					else:
						states[state] = 0.0
	happiest = 0.0
	happiest_state = ''
	for state in states:
		if happiest <= states[state]:
			happiest = states[state]
			happiest_state = state
	
	print happiest_state
			
if __name__ == '__main__':
    main()
