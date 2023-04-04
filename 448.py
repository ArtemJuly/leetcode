
nums = [1,1]
#nums = [4,3,2,7,8,2,3,1]

#print([0] * len(nums))

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    numsCounter = [0] * len(nums)
    for num in nums:
        numsCounter[num-1] += 1 # Счтчик сколько раз встречается число
    dissapearedNums = []
    for i in range(0, len(numsCounter)):
        if (numsCounter[i] == 0):
            dissapearedNums.append(i+1)
    return dissapearedNums

print(findDisappearedNumbers(nums))
    
