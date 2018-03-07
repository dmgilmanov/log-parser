import re
from collections import Counter
import csv

def reader(filename):
	regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' #Create pattern re for parse Apache log file - match all IP addresses
	
	with open(filename) as f:             		#Open log file and assign it to f variable
		log = f.read()                      
		ips_list = re.findall(regexp, log)  	#Create ips_list and findall IP inside log file
		
	return ips_list;
	
def count(ips_list):							#Calculate the number of IP address. 
	return(Counter(ips_list))
	
	
def write_csv(count):
	with open('output.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		
		header = ['IP', 'Frequency']
		writer.writerow(header)
		
		for item in count:
			writer.writerow( (item, count[item]) )
		
if __name__ == '__main__':
	write_csv(count(reader('test.log')))
