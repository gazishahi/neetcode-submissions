class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each letter
        # collect its ascii value via ord
        # add to hash map based off combination
        # value should be array of tuples
        # key should be tuple

        group = defaultdict(list)

        for word in strs:
            sortW = "".join(sorted(word)) # O(nlogn)
            group[sortW].append(word)

        return list(group.values())