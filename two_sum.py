nums = [2,7,11,15]
target = 9

# Non optimal O(n^2)
"""def two_sum(nums:list, target:int) -> list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)): #Несколько раз вычисляю длину
            if nums[i] + nums[j] == target:
                return [i,j]
        break
"""


def twoSum(nums: list[int], target: int)-> list[int]:
    n = len(nums)
    a = nums.copy()

    nums.sort()
    
    #делаю два указателя, чтобы идти с двух концов, как Гаусс при формуле прогрессии
    l = 0 
    r = n-1

    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            break
        elif sum > target:
            r -= 1 # Перелет, уменьшаем правый
        else:
            l += 1 # Недолет, увеличиваем левый
        
        # посокльку нам изначально надо найти позиции в несортированном массиве, мы их ищем
        v = []
        for i in range(n):
            if nums[l] == a[i]:
                v.append(i)
            elif nums[r] == a[i]:
                v.append(i)
    return v








print(twoSum(nums=nums, target=target))


