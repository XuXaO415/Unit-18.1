def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers 
    - lowest: lowest number to print 
    - highest: highest number to print 

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """


    # colors = ['red', 'orange', 'yellow', 'green']
    # for color in colors:
    #     print(color)
    
    #for num in range(10):
      #print(num):
    # YOUR CODE HERE
    for num in nums:
        if num >= lowest and num <= highest:
            print(f"{num} fits")
    


in_range([10, 20, 30, 40, 50], 15, 30)            
