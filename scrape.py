import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re


# field location table
# len: [name, major, hometown, passage]
fld = {
	19: [4, 9, None, 16],
	15: [4, 9, None, 12],
	32: [10, 15, 20, 27],
	48: [4, 9, 12, 15],
	25: [4, 15, None, 22],
	21: [4, 15, None, 18],
	26: [4, 9, 14, 21],
	48: [4, 9, 12, 15],
	37: [10, 16, 22, 28],
	18: [4, 9, 12, 15],
	24: [10, 15, 18, 21],
	28: [10, 15, 22, 25],
	29: [10, 17, 24, None]
}

def isFellowEntry(entry):
	return len(entry) in fld

def isYear(child):
	return "h2" in str(child)

target = "http://bonderman.uw.edu/undergraduate-fellow-profiles/"
page = urllib2.urlopen(target)
soup = BeautifulSoup(page, 'html.parser')

# reall skillz
fellows = {}

big_freakin_box = soup.find('div', attrs={'id': 'main_content'}).find_all(['p', 'h2'])

fellow_id = 0
year = None

hashtable = {}

for child in big_freakin_box:
	if isYear(str(child)):
		year = re.split('<|>',str(child))[2]
		continue

	entry = re.split('<|>|\n',str(child))

	# fields
	if isFellowEntry(entry):
		key = len(entry)
		fields = fld[key]
		vals = [entry[i] if i!=None else "" for i in fields ]

		# speical cases
		if vals[1] == "":
			vals[1] = entry[17]
		if vals[1] == "/a":
			vals[0] = "Unidentified"
			vals[1] = "Unidentified"


		fellows[fellow_id] = {"name": vals[0], "majors": vals[1], "hometown": vals[2], "paragraph": vals[3], "year": year}
		fellow_id += 1

df = pd.DataFrame(fellows).transpose()
#print df.head()
df.to_csv("BIGDAAATA.csv",index = False)


