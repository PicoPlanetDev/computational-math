from copy import deepcopy

def almostEqual(x,y):
    return abs(x-y)<10**-8

# This is probably going to be slow because 
# I haven't used numpy in a while and don't feel like looking up the docs
# So it just uses normal lists
def gaussianElimination(M):
    matrix = deepcopy(M)
    # Iterate through rows and columns in the array
    for col in range(len(matrix[0])):
        for row in range(col+1, len(matrix)):
            # Calculate a new row value for each combination, putting these in list currentRow
            currentRow = [(rowValue * (-(matrix[row][col] / matrix[col][col]))) for rowValue in matrix[col]]
            #print(currentRow)
            matrix[row] = [sum(pair) for pair in zip(matrix[row], currentRow)] # Find the sum of each pair of row values and the r calculated above
    # When I learned elimination, 
    # we had to the find the other variables by putting them back in
    # to "find Grandma"
    variablesSolution = [] # Create a list to represent the solution
    matrix.reverse() # If we iterate through matrix backwards we can make it easier
    for equationSolution in range(len(matrix)):
            if equationSolution == 0:
                variablesSolution.append(matrix[equationSolution][-1] / matrix[equationSolution][-2])
            else:
                inner = 0
                for x in range(equationSolution):
                    inner += (variablesSolution[x]*matrix[equationSolution][-2-x])
                # If the equation is in y=mx+b form
                # We can rearrange it to solve for x like this:
                # x = (y-b)/m
                variablesSolution.append((matrix[equationSolution][-1]-inner)/matrix[equationSolution][-equationSolution-2])
    variablesSolution.reverse() # Because we used a reversed input matrix, we need to reverse the output
    # Remove floating point error by rounding each solution to 8 decimal places
    # 8 is somewhat arbitrary but almostEqual uses 10**-8 so that what I picked
    for i in range(len(variablesSolution)):
        variablesSolution[i] = round(variablesSolution[i], 8)
    return variablesSolution

A=[[1,1,10],
   [2,-1,2]]

solutionToA=[4.0, 6.0]


B=[[1,1,-2,1,3,-1,4],
   [2,-1,1,2,1,-3,20],
   [1,3,-3,-1,2,1,-15],
   [5,2,-1,-1,2,1,-3],
   [-3,-1,2,3,1,3,16],
   [4,3,1,-6,-3,-2,-27]]

solutionToB=[1.0, -2.0, 3.0, 4.0, 2.0, -1.0]


C=[[2,3,-1,1,2,-1,2,1],
   [1,-1,1,-1,1,1,1,2],
   [2,2,-2,1,-2,1,-1,1],
   [1,0,-2,1,-1,-1,1,1],
   [1,-2,1,-1,1,1,1,2],
   [1,2,2,2,1,-1,2,1],
   [1,-1,-2,-1,-1,1,1,2]]

solutionToC=[1.25, -0.0, 0.5, -1.0, -0.75, -0.5, 0.5]

M = [
    [4,7,9,4],
    [3,2,1,2],
    [18,2,4,9]
]

# print(gaussianElimination(A),gaussianElimination(A)==solutionToA)
# print(gaussianElimination(B),gaussianElimination(B)==solutionToB)
# print(gaussianElimination(C),gaussianElimination(C)==solutionToC)
# print("Gaussian elimintaion... 30pts")

print(gaussianElimination(M))