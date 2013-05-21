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
    mr.emit_intermediate(value, record)

def reducer(key, list_of_values):
	order = []
	line = []
	
	for v in list_of_values:
		if "order" in v:
			order.append(v)
		else:
			line.append(v)
			
	for o in order:
		for l in line:
			joined = []
			for oi in o:
				joined.append(oi)
			for li in l:
				joined.append(li)
			mr.emit((joined))
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
