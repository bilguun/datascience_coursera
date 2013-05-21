import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	key = record[0]
	if key == "a":
		for k in range(0, 5):
			value = []
			value.append(record[1])
			value.append(k)
			mr.emit_intermediate(tuple(value),record)				
	else:
		for i in range(0,5):
			value = []
			value.append(i)		
			value.append(record[2])	
			mr.emit_intermediate(tuple(value),record)		

def reducer(key, list_of_values):
	a = []
	b = []
	for v in list_of_values:
		if v[0] == "a":
			a.append(v)
		else:
			b.append(v)
	sorted(a, key=lambda a: a[2])
	sorted(b, key=lambda b: b[1])
	multsum=0;		
	for ae in a:
		for be in b:
			if ae[2] == be[1]:
				multsum += ae[3]*be[3]
	result = list(key)
	result.append(multsum)
	mr.emit((tuple(result)))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
