def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):      O(N²) SOLUTION
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return None
        
        db = {}
        sz = len(nums)
        for idx in range(sz):
            db[nums[idx]] = idx
            
        for idx in range(sz):
            diff = target - nums[idx]
            idy = db.get(diff, 0)
            if idy != 0 and idy != idx:
                return [idx, idy]
        return None
    
