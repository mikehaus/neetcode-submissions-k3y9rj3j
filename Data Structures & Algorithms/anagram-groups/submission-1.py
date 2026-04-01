from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            val = ''.join(sorted(word.lower()))
            print(word)
            groups[val].append(word)

        return list(groups.values())