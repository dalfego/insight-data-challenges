"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Example 1:

Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:

Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

"""

#YOUR CODE GOES HERE
def max_profit_helper(price):
  
    profit = 0
    
    for i in range(len(price)-1):
      	# Look for the largest difference (profit) and update
        if ((max(price[i+1:]) - price[i]) > profit):
            profit = (max(price[i+1:])-price[i])
            
    return profit


##DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)

def main():
    TEST_CASE1 = [7, 6, 4, 3, 1]
    TEST_CASE2 = [7, 1, 5, 3, 6, 4]

    print ("Testing your code with TEST_CASE1, the expected output is 0, your output is {}".format(max_profit(TEST_CASE1)))
    print ("Testing your code with TEST_CASE2, the expected output is 5, your output is {}".format(max_profit(TEST_CASE2)))

    
if __name__ == "__main__":
    main()

