#----------------------------------- SRART -----------------------------------------------#
#          OF CODE WHICH IS ACCEPTABLE BY THE LEETCODE 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


# ------------------------------------- END --------------------------------------------# 

# TRY 03 CORRECT ONE

l = list(map(int, input("Enter numbers: ").split()))

print(l)

for i in range(len(l) - 1, -1, -1):

    if l[i] < 9:
        l[i] += 1
        break          # We are done

    l[i] = 0           # Current digit was 9, so make it 0 and continue

else:
    # This runs only if the loop never executed 'break'
    l.insert(0, 1)

print(l)

# 
# TRY 01 

# l = [1,2,9]

# k=l[-1]
# if k==9:
#     l[-1]=0
#     k=l[-1-1]
#     # k=k+1
#     print(k)
# else:
#     l[-1]=l[-1]+1

# print(l)
# print(len(l))
 


#  TRY CODE 02


# for i in range(len(l)):
#     last=l[-1]
#     if l[-1] == 9:
#         l[-1]=0
#         # if l[-1]==0:
#         #     l[-1-1]=l[-1-1]=1
#         print(l)

#     elif l[-1]==0:
#         l[-1]=l[-2]
#         l[-2]=l[-2]=1

#     print(l)

    
# for i in range(len(l)-1, -1, -1):
#     if l[i]==9:
#         l[i]=0
#         j = i - 1
#         l[j]=l[j]+1
#     print(l)

# else:
#     l[-1]=l[-1]+1

# print(l)

