import math

# Function to check whether the given 
# number is Proth Prime or Not. 
def isProthPrime(n):
    prime = [0 for i in range((n * 2))] 
    def SieveOfEratosthenes(n): 
         # false if i is Not a prime, else true. 
        for i in range(1, n + 2): 
             prime[i] = True
  
        prime[1] = False
  
        for p in range(2, math.ceil(n**(0.5))): 
  
            # If prime[p] is not changed, 
            # then it is a prime 
            if (prime[p] == True):  
                for i in range(p * p, n + 1, p): 
                    prime[i] = False
                    
    # Utility function to check power of two 
    def isPowerOfTwo(n): 
        return (n and (n & (n - 1)) == False) 
  
    # Function to check if the given 
    # number is Proth number or not 
    def isProthNumber(n): 
        k = 1
        while (k < (n // k)): 
            # check if k divides n or not 
            if (n % k == 0): 
  
                # Check if n/k is power of 2 or not 
                if (isPowerOfTwo(n // k)): 
                    return True
          
            # update k to next odd number 
            k = k + 2
      
        #n is not proth number 
        return False
    SieveOfEratosthenes(n)
    # Check n for Proth Number 
    if (isProthNumber(n - 1)):  
        # if number is prime, return true 
        if (prime[n]):
            print(str(n) + ' is proth prime')
            return True
        else: 
            print(str(n) + ' is not proth prime')
            return False
      
    else:
        print(str(n) + ' is not proth number')
        return False



# if number is proth prime.   
isProthPrime(10)
