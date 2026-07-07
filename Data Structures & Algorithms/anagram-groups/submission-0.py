from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)
        for word in strs:
            sorted_label="".join(sorted(word))
            buckets[sorted_label].append(word)
        return list(buckets.values())