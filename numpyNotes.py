#notation
# nd1[row, col]
# nd1[3, 2] #3 down, 2 across
# nd1[0:3, 1:3] #non inclusive, 0 to 2 row, 1 to 2 column
# nd1[:,3] #all rows column 3
# nd1[-2:, 3] # -2: means go all the way to the end
# nd1[-1, 1:3] #last row or column

import numpy as np

def test_run():
    #2d array
    print(np.array([(2, 3, 4), (5, 6, 7)]))
    print(np.empty((5, 4)))  #empty array with 5 rows and 4 columns, default value will be value at memory address at the time of creation (random)
    print(np.ones((5,4)))   #array with 5 rows 4 columns and all value equal to 1
    print(np.ones((5,4), dtype=np.int_))

    print(np.zeros((5,4), dtype=np.int_))

    print(np.random.random((5,4)))  #5 rows and 4 columns of random number
    print(np.random.rand(5,4))  #same as above but not a tuple as param

    print(np.random.normal(size=(2,3))) #random number with normal distribution
    print(np.random.normal(50, 10, size=(2,3))) # random number will be near 50, mean 50, distribution 10

    print(np.random.randint(10)) #single int between 0 and 10
    print(np.random.randint(0, 10)) # same but specify low and high
    print(np.random.randint(0, 10, size=5)) #1D array
    print(np.random.randint(0, 10, size=(2, 3))) #2x3 of rand between 0 and 10

    a = np.random.random((5,4))
    print(a.shape) #returns (5,4)
    print(a.shape[0]) #returns rows
    print(a.shape[1]) #returns columns
    print(len(a.shape)) #dimension of array, 2
    print(a.size) #20 number of values in the array
    print(a.dtype) #float64 defaults to 64bit floating numbers

    #operations with array
    np.random.seed(693) #seed the random number generator
    b = np.random.randint(0, 10, size=(5,4)) #5x4 rand integer in 0 to 10

    #sum all elements
    sum = b.sum()

    #axis for column is 0, axis for row is 1
    sumColumn = b.sum(axis=0)
    sumRow = b.sum(axis=1)

    minColumn = b.min(axis=0)   #minimum of each column
    maxRow = b.max(axis=1)  #maximum of each row

    #find position of maximum value in 1D array
    b.argmax()  #returns index of max value

    #accessing elements in array
    c = np.random.rand(5, 4)
    element = c[3, 2]   #4th row, 3rd column, starts from 0
    elementSliced = c[0, 1:3]   #from 0th row, get value from 1st to 3rd column, exclude 3rd column
    topLeftCorner = c[0:2, 0:2] #2 across, 2 down
    columnsEveryRow = c[:, 0:3:2]   #selected columns 0, 2 for every row

    #modify array elements
    d = np.random.rand(5,4)
    d[0, 0] = 1
    d[0, :] = 2    #assign every element in 0th row the value 2
    d[:, 3] = [1, 2, 3, 4, 5] #assign values to column 3, the value assigned should have same number of elements as column

    #accessing elements
    e = np.random.rand(5)
    indices = np.array([1,2,2,3]) #we want value at index 1, 2, 2, 3
    print(e[indices])   #will give us values at each index

    #boolean arrays
    f = np.array([(20, 25, 10, 5, 23), (0, 2, 50, 1, 33, 21)])
    g = np.array([(2, 55, 30, 5, 23), (10, 32, 20, 15, 33, 21)])
    
    meanf = f.mean()
    print(f[f<meanf])    #print all value in f where f < mean

    #arithmetic operations
    print(2*f) #multiply every element by 2
    print(f/2) #divide every element by 2, int results in int
    print(f/2.0) #get float value
    print(f+g) #add 2 arrays
    print(f*g) #multiply
    

if __name__ == "__main__":
    test_run()