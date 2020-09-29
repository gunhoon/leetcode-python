class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        max_len = 0

        head = tail = 0

        for i, c in enumerate(s):
            index = hashmap.get(c)

            if index is not None and index >= head:
                if (tail - head) > max_len:
                    max_len =  tail - head
                head = index + 1

            hashmap[c] = i
            tail = i + 1

        if (tail - head) > max_len:
            max_len =  tail - head

        return max_len
