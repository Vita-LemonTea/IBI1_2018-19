# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:16:51 2019

@author: panho
"""
# import necessary libraries
import re
from xml.dom.minidom import parse
import xml.dom.minidom

#open the xml file and create the DOM tree
DOMTree = xml.dom.minidom.parse("predator-prey.xml")
collection = DOMTree.documentElement
parameters = collection.getElementsByTagName("parameter")


for parameter in parameters:
    #value = parameter.getElementsByTagName('value')
    value = parameter.getAttribute('value')
    id = parameter.getAttribute('id')
    if re.search("k_predator_breeds",id):
        #change the value with a number
    elif re.search("k_predator_dies",id):
        #change the value with a number
    elif re.search("k_prey_breeds",id):
        #change the value with a number
    elif re.search("k_prey_dies",id):
        #change the value with a number

#rewrite the XML file

# import necessary libraries
import os
import numpy as np
import re
import matplotlib.pyplot as plt

#set the working directory
os.chdir(r'C:/Users/panho/Documents/git/IBI1_2018-19/Practical13')


   
    
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()

#change xml to cps
y = xml_to_cps()

os.system("CopasiSE.exe predator-prey.cps")

#open results file
data = open('modelResults.csv')
l = []

#get the comma-separated information
for line in data:    
    line = line.rstrip()
    line = re.split(r',',line)
    l.append(line)

#results only include data
results = np.array(l)
nameA = results[0][1]
nameB = results[0][2]
results = np.delete(results, 0, axis = 0)
results = results.astype(np.float)


plt.figure(figsize=(6,4),dpi=150)
plt.title("Time course") 
plt.xlabel("time") 
plt.ylabel("population size") 
plt.plot(results[0:,1], label = 'predator(b=0.02, d=0.4')
plt.plot(results[0:,2], label = 'prey(b=0.1, d=0.02)')
plt.legend()
plt.show()


#delete the time
results = np.delete(results, 0, axis = 1)

plt.figure(figsize=(6,4),dpi=150)
plt.title("Limit cycle") 
plt.xlabel("predator population") 
plt.ylabel("prey population") 
x = results[0:,0]
y = results[0:,1]
plt.plot(x,y)


plt.show()