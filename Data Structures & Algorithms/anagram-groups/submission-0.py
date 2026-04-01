class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}

        for word in strs:
            counts = [0] * 26 
            for c in word.lower():
                if c.isalpha():
                    index = ord(c) - ord('a')  # map 'a'->0, 'b'->1, ..., 'z'->25
                    counts[index] += 1

            key = tuple(counts)

            if key not in anagramGroups:
                anagramGroups[key] = [] 
            anagramGroups[key].append(word)

        return list(anagramGroups.values())