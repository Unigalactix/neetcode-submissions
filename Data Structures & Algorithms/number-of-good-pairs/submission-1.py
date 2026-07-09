class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen_counts={}
        total_pairs=0

        for num in nums:
            if num in seen_counts:
                total_pairs += seen_counts[num]
                seen_counts[num]+=1
            else:
                seen_counts[num]=1
        return total_pairs