# Created by Murtaza Bambot on 12/15/12

# This script will take in a CSV list of links and will
# visit each webpage and pull the email addresses listed
# on that page

import urllib.request
import re
import csv


EMAIL_REGEX = '[\w.-]+@[\w.-]+\.[\w]{1,4}'

# Visits the URL and pulls information in string format
# Page information is returned when used
def getPageText(url):
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	page = response.read()
	return page.decode()


# Returns a tuple of all emails found from a page based of
# a regex
def parseForEmails(page):
	return re.findall(r"[\w.-]+@[\w.-]+\.[\w]{1,4}", page)


# Takes in a csv file of urls and opens and reads
# the csv file, returning a list object of the urls  
def readCSV(filename):
	aFile = open(filename, 'r', newline = '')
	reader = csv.reader(aFile, delimiter=',')
	urlList = []

	for each in reader:
		urlList.append(each)

	return urlList

# Takes a list object of urls and parses each one for
# emails, creating a list object of emails
def createEmailList(urlList):
	emailList = []
	for url in urlList:
		print(url[0])
		emailTuple = parseForEmails(getPageText(url[0]))
		emailList.append(list(emailTuple))
	return emailList


# Creates a new csv file with the list of emails scraped
# from the provided urls 
def newCSVFile(emailList):
	csvfile = open('scrapedEmails.csv', 'w', newline='')
	writer = csv.writer(csvfile, delimiter = ',')
	for email in emailList:
		writer.writerow(email)
	csvfile.close()



# To use, uncomment the following lines of code and change the
# words 'filename.csv' to the name of your intended file. Remember
# the function only accepts string arguements.

# After running the code, your file with the list of emails
# will be in the same folder as your script, under the name
# "scrapedEmails.csv"

# urlList = readCSV('filename.csv')
# emailList = createEmailList(urlList)
# newCSVFile(emailList)
