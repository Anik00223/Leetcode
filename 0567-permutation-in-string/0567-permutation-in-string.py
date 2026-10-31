class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        for i in range(len(s1)):
            count2[s2[i]] = count2.get(s2[i], 0) + 1

        if count1 == count2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            count2[s2[left]] -= 1

            if count2[s2[left]] == 0:
                del count2[s2[left]]

            left += 1

            if count1 == count2:
                return True

        return False