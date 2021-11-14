
import csv
file=open('triangleInteriors.txt','r')
csvReader = csv.reader( file,  delimiter=",")
pointsABCD=[[int(item) for item in row] for row in csvReader]

