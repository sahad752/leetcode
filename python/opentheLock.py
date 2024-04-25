from collections import deque

class Solution:

    def getNextCombinations(self, combination: str):
        nextCombinations = []

        for i, value in enumerate(combination):
            for valueDifference in (-1, 1):
                rotatedValue = (int(value) + valueDifference) % 10

                nextCombinations.append(combination[:i] + str(rotatedValue) + combination[i + 1:])

        return nextCombinations

    def openLock(self, deadends, target: str) :
        deadEnds = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}

		# Keep searching while there are still valid paths.
        while queue:
            combination, depth = queue.popleft()

			# We've found our target.
            if combination == target:
                return depth

			# We've hit a dead end and terminate searching from this node.
            if combination in deadEnds:
                continue

			# Get the nodes connected to the current node.
            for nextCombination in self.getNextCombinations(combination):
				# If we've not visited the node before, then add it to the queue to perform BFS on again.
                if nextCombination not in seen:
                    seen.add(nextCombination)
                    queue.append((nextCombination, depth + 1))

		# We searched all valid routes but could not get to the target.
        return -1



a = Solution().openLock(["0201","0101","0102","1212","2002"], "0202")
print(a)