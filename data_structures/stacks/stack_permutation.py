# %%
'''Python Program to check for Stack Permutations. 
What are Stack Permutations?
If the elements of the input queue can be permuted into the order of the elements in the output queue using '''

# %%
from queue import Queue
from collections import deque

# %%
def checkStackPermutation(inp, output, length):       
    # Input queue  
    inpQ = Queue() 
    for i in range(length): 
        inpQ.put(inp[i])  
  
    # output queue  
    outQ = Queue() 
    for i in range(length): 
        outQ.put(output[i])  
  
    # stack to be used for permutation  
    tempStack = deque()
    while (not inpQ.empty()): 
        element = inpQ.queue[0]  
        inpQ.get() 
        if (element == outQ.queue[0]): 
            outQ.get()  
            while (len(tempStack) != 0): 
                if (tempStack[-1] == outQ.queue[0]): 
                    tempStack.pop()  
                    outQ.get() 
                else: 
                    break
        else: 
            tempStack.append(element) 
  
    # If after processing, both Input  
    # queue and stack are empty then   
    # the Input queue is permutable 
    # otherwise not.  
    return (inpQ.empty() and 
        len(tempStack) == 0) 

# %%
if __name__ == '__main__':  
    inp = list(map(int, input().split()))
  
    # Output Queue  
    output = list(map(int, input().split())) 
  
    length = len(inp)
  
    if (checkStackPermutation(inp, output, length)):  
        print("Yes, the output is a possible stack permutation of the input.")  
    else: 
        print("No, the output is not a stack permutation of the input") 

# %%
