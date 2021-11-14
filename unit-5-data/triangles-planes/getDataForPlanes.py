
import csv
file=open('pointsOnAPlane.txt','r')
csvReader = csv.reader( file,  delimiter=",")
fourTriples=[[int(item) for item in row] for row in csvReader]

