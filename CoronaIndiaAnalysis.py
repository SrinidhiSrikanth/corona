# importing libraries 

import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os 
import numpy as np 
import matplotlib.pyplot as plt 
extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo', 'State/UT','Total confirmes cases(Including foreign nationals)','Cured/Discharged/Migrated','Death'] 

response = requests.get(URL).content 
soup = BeautifulSoup(response, 'html.parser') 
header = extract_contents(soup.tr.find_all('th')) 

stats = [] 
all_rows = soup.find_all('tr') 

for row in all_rows: 
	stat = extract_contents(row.find_all('td')) 
	if stat: 
		if len(stat) == 5: 
			# last row 
			stat = ['', *stat] 
			stats.append(stat)
		elif len(stat) == 6:
			stats.append(stat) 




objects = [] #states
for row in stats : 
	objects.append(row[2]) 


y_pos = np.arange(len(objects)) 
cases = []
for row in stats : 
        cases.append(int(row[3]))

cured = []
for row in stats : 
        cured.append(int(row[4]))
        
death = []
for row in stats : 
        death.append(int(row[5]))
       
performance = []
for row in stats : 
        performance.append(int(row[3])+int(row[4]))

table = tabulate(stats, headers=SHORT_HEADERS) 
choice='yes'

while (choice == 'Yes' or choice == 'yes' or choice == 'YES'):
        print("Select an option: 1. India's COVID-19 tracker\n","2. Save state-wise data in a text file\n",\
              "3. Graphical representation of total number of cases nation wide\n","4. Graphical representation of cases cured nation wide\n",\
              "5. Graphical representation of deaths nation wide\n",sep='                  ')
        option= int(input())
        if (option==0):
                exit()
        elif(option==1):
                print(table)
        elif (option == 2):
                f= open('table.txt','w')
                f.write(table)
                f.close()
        elif (option == 3):
                #bar graph for total cases
                plt.barh(y_pos,cases, align='center', alpha=0.5,
                                                        color=(234/256.0, 128/256.0, 252/256.0), 
                                                        edgecolor=(106/256.0, 27/256.0, 154/256.0))
                plt.yticks(y_pos, objects) #placing the numbers
                plt.xlim(1,8000)#providing limits
                plt.xlabel('Total cases')
                plt.ylabel('States')
                plt.title('States vs Total covid-19 cases')
                plt.show()
        elif (option ==4):
                plt.barh(y_pos,cured, align='center', alpha=0.5,
                                                         color=(234/256.0, 128/256.0, 252/256.0),
                                                         edgecolor=(106/256.0, 27/256.0, 154/256.0))
                plt.yticks(y_pos, objects) #placing the numbers
                plt.xlim(1,800)#providing limits
                plt.xlabel('Total cured')
                plt.ylabel('States')
                plt.title('States vs Cured cases')
                plt.show()
        elif(option==5):
                plt.barh(y_pos,death, align='center', alpha=0.5,
                                                         color=(234/256.0, 128/256.0, 252/256.0),
                                                         edgecolor=(106/256.0, 27/256.0, 154/256.0))
                plt.yticks(y_pos, objects) #placing the numbers
                plt.xlim(1,500)#providing limits
                plt.xlabel('Total deaths')
                plt.ylabel('States')
                plt.title('States vs Total deaths')
                plt.show()
                
        choice=input("Would you like to continue?Yes/No\n")
