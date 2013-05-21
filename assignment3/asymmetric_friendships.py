import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	value = record[:]
	record.sort()
	key = ''.join(record[:])
	mr.emit_intermediate(key, value)	

def reducer(key, list_of_values):
	if len(list_of_values) == 1:
		v = list_of_values[0]
		mr.emit((tuple(v)))
		v.reverse()
		mr.emit((tuple(v)))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
