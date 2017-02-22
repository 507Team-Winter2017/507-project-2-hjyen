#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

import requests
from bs4 import BeautifulSoup
import re
 
def nyt_10headings():
	base_url = 'http://www.nytimes.com'
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, 'html.parser')

	count = 1
	for story_heading in soup.find_all(class_="story-heading"): 
		if count < 11:
			count += 1
			if story_heading.a: 
				print(story_heading.a.text.replace("\n", " ").strip())
			else: 
				print(story_heading.contents[0].strip())
		else:
			break

nyt_10headings()


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

def michi_most_read():
	base_url = 'https://www.michigandaily.com/'
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, 'html.parser')

	most_read = soup.find(class_="view-most-read")
	for ol in most_read.find_all("ol"):
		for li in ol.find_all("li"):
			print (li.get_text())

michi_most_read()


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
def cat_alt():
	base_url = 'http://newmantaylor.com/gallery.html'
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, 'html.parser')

	for img in soup.find_all("img"):
		if img.has_attr("alt"):
			print (img["alt"])
		else:
			print ("No alternative text provided!")

cat_alt()

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here


def get_faculty_node(page):
	url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
	base_url = url+page
	r = requests.get(base_url, headers={'User-Agent': 'SI_CLASS'})
	soup = BeautifulSoup(r.text, 'html.parser')
	contact_page_lst=[]
	for div in soup.find_all(class_="field-item even"):
		for node in div.find_all("a"):
			if node.get_text() == "Contact Details":
				contact_page_lst.append(node["href"])
	return (contact_page_lst)


def total_faculty_node():
	page_lst=["","&page=1","&page=2","&page=3","&page=4","&page=5"]
	total_faculty = []
	for p in page_lst:
		total_faculty += get_faculty_node(p)
	return (total_faculty)

total_nodes = total_faculty_node()



def get_contact(node):
	url = "https://www.si.umich.edu"
	base_url = url+node
	r = requests.get(base_url, headers={'User-Agent': 'SI_CLASS'})
	email = re.findall("[a-zA-Z0-9]+@umich.edu", r.text)
	return (email[0])


def email(lst):
	count =1
	for node in lst:
		print (str(count), get_contact(node))
		count +=1

email(total_nodes)




