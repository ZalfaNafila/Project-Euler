n = 1000;

#find how many numbers were the multiple of 3 OR 5
mt3 = 999 // 3
mt5 = 999 // 5
#find how many numbers were the multiple of 3 AND 5 (3 * 5 = 15)
mt15 = 999 // 15

#find the total sum of them
#formula = n(2a +(n-1)b) / 2
multi3 = 3 * ((n-1)//3 *((n-1)//3+1)) // 2
multi5 = 5 * ((n-1)//5 *((n-1)//5+1)) // 2
multi15 = 15 * ((n-1)//15 *((n-1)//15+1)) // 2

total = multi3 + multi5 - multi15 #need to be substracted with 15 because we don't need multiple of 3 AND 5
print(total)
