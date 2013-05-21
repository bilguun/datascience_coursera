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
	value = record[1]
	mr.emit_intermediate(value[:-10], value[:-10])	

def reducer(key, list_of_values):
	for v in set(list_of_values):
		mr.emit((v))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
