################Ways Exercise 1
def ways(n):

    count = 0 #count variable has 0 stored
    for y in range((n // 5)+1): #loops form 0 to n//5(division), this tells how many cents we can use.
        x = n - 5 * y #calculates how many cents left
        if x >= 0:      # if condition for checking
            count += 1  #increments the count for each check
    print(count)    #prints count
    return
        


ways(12)
ways(20)
ways(3)
ways(1)

##################################################
##################################################
################Ways Exercise 2

def ways(cents, coin_types = [1,5]):
    #saving the solved value
    save ={}
    # n = coins left to make
    # i = coin in use
    def count(n,i):
        #if exactly 0 cents left
        if n == 0:
            return 1
        # if we ran out of cents and went below 0 or ran out of ocins
        #coin types will depend on the inputs to the function
        if n < 0 or i == len(coin_types):
            return 0
        
        # savechecjing if (n,i) in save
        if (n,i) in save:
            return save[(n,i)]
        
        #include starts at it and keeps using the coin again and again until n becomes 0
        include = count(n - coin_types[i],i)
        #exclude will try with other coins until the n becomes 0
        exclude = count(n, i + 1)

        #saves the include and exclude to get the full combination of all coins provided by user
        save[(n,i)] = include + exclude
        #returns include coin_types[i] + exclude coin_types[i]
        return save[(n,i)]
    return count(cents, 0)

print(ways(100,[25,10,5,1]))

##################################################
##################################################
################Numpy Lowest_score Exercise 1


import numpy as np #importing numpy lib
names = ['Hannah','Astrid','Abdul','Mauve','Jung'] # array list of names
scores = [99,71,85,62,91] #array list of numbers and stored in scores variable
def lowest_score(names,scores): #defining a function 
    #print(str(names[scores.argmin()]) + " has the lowest score")
    print(str(names[scores.index(min(scores))]))
    #print(str(names[scores.argmax()]) + " has the highest score")

lowest_score(names, scores)



##################################################
##################################################
################Numpy sort names Exercise 2

import numpy as np  # importing numpy
names = np.array(['Hannah','Astrid','Abdul','Mauve','Jung'])  #creating array list string data and storing in names
scores = np.array([99,71,85,62,91])                     # creating  array list integers and storing in scores
def sort_names(names,scores):   #defining a function with parameters 
    # using argsort() function from numpy library that sorts based on indices from lowest to highest 
    # thats why i used [::-1], which sorts from highest to lowest
    print(str(names[scores.argsort()[::-1]]))

sort_names(names, scores)  #calling function
