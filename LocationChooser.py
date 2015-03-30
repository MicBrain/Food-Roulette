from random import randrange

def choose(name_list):
	# dict = {}
	# for name, loc in locDict.iteritems():
	# 	lat, lng = gmaps.address_to_latlng(loc)
	# 	distance = math.sqrt(math.pow((lat - LocationFinder.getLatitude()), 2) + math.pow((lng - LocationFinder.getLongitude()), 2))
	# 	score = 5 - distance * 140 + rateDict[name]
	# 	dict[name] = score

	# l = []
	# for key, value in dict.iteritems():
	# 	l.append(value)

	# heapsort(l)

	
	#print dict
	#key, value = dict.get("Wood Tavern")
	#print "key is:",key, "value: ",value
	#print name_list
	return name_list[randrange(len(name_list))]
