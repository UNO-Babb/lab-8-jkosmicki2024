#ProcessData.py
#Name: Jacob Kosmicki
#Date: 4/2/2025
#Assignment: Lab 08

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    IDNUM = data[3]
    year = data[5]
    if (year.find("F")!=-1):
      year="FR"
    elif (year.find("h")!=-1):
      year="SO"
    elif (year.find("J")!=-1):
      year="JR"
    elif (year.find("i")!=-1):
      year="SR"

    major = data[6]
    abrv_Major = major[0:3]
    
    student_id = makeID(first, last, IDNUM, abrv_Major,"-",year)
    output = data[0]
    outFile.write(output)
    
    print(student_id)
  inFile.close()
  outFile.close()
  
def makeID(first, last, Idnum, major, line, year):
  print(first, last, Idnum, major, line, year)
  idlen = len(Idnum)

  while len(last) < 5:
    last = last + "X"
  id = first[0] + last + Idnum[idlen - 3: ]
  return id 

if __name__ == '__main__':
  main()