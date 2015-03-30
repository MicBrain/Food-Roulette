import urllib
sock = urllib.urlopen("http://www.geoiptool.com/")
htmlSource = sock.read()
sock.close()

longIndex = htmlSource.index("Longitude:") + 75 #The 75 is to get to the actual Longitude
temp = htmlSource[longIndex:]
longitude = htmlSource[longIndex: (longIndex + temp.index("</td>"))]

latIndex = htmlSource.index("Latitude:") + 74 #The 74 is to get to the actual Latitude
temp = htmlSource[latIndex:]
latitude = htmlSource[latIndex: (latIndex + temp.index("</td>"))]

cityIndex = htmlSource.index("City:") + 70 #The 74 is to get to the actual Latitude
temp = htmlSource[cityIndex:]
city = htmlSource[cityIndex: (cityIndex + temp.index("</td>"))]


def getLatitude():
	return Decimal(latitude)

def getLongitude():
	return Decimal(longitude)

def getCity():
	return city
