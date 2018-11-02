def largestPalindrome():
  
  ### initiate variable to store largest palindrom product found
  largest = 0
  
  ### iterate through all 3 digit numbers for 2 sets, i and j
  for i in range(100, 1000):
    for j in range(100, 1000):
      
      ###determine if product is a palindrome as well as larger than the previous largest value
      if str(i * j)[::-1] == str(i * j) and i * j > largest:

        ### if both conditions are met, replace largest with current value of i * j
        largest = i * j
        
  ### return
  return largest


print(largestPalindrome())
