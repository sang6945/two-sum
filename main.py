def twoSum(nums, target):
    result=[]
    flag=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i]+nums[j]==target):
                result.append(i)
                result.append(j)
                flag=1
                break
        if(flag==1):
            break
    return result
