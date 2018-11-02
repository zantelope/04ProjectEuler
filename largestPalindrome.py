
def largestPalindrome():

  ### initiate variable to store largest palindrom product found
  largest = 0
  
  ### iterate through all 3 digit numbers for 2 sets, i and j
  for i in range(999):
    for j in range(999):
      
      ###determine if product is a palindrome as well as larger than the previous largest value
      if str((i + 1) * (j + 1))[::-1] == str((i + 1) * (j + 1)) and (i + 1) * (j + 1) > largest:

        ### if both conditions are met, replace largest with current value of (i + 1)(j + 1)
        largest = (i + 1) * (j + 1)
        
  ### return
  return largest


print(largestPalindrome())
