
def euler96Data():
    import csv
    file = open('p096_sudoku.txt', 'r')
    csvReader = csv.reader( file,  delimiter=" ")
    rows=[item[0] for item in csvReader if item[0]!='Grid']
    grids=[rows[i:i+9] for i in range(0,len(rows),9)]
    return [[[int(char) for char in item] for item in grid] for grid in grids]
     
grids=euler96Data()
