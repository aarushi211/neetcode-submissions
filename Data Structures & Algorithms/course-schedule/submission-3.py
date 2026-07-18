class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_count = [0]*numCourses
        prevMap = defaultdict(list)
        for crs, pre in prerequisites:
            prevMap[pre].append(crs)
            prereq_count[crs] += 1

        queue = deque()

        for crs in range(numCourses):
            if prereq_count[crs] == 0:
                queue.append(crs)

        finish = 0

        while queue:
            pre = queue.popleft()
            finish += 1
            for crs in prevMap[pre]:
                prereq_count[crs] -= 1
                if prereq_count[crs] == 0:
                    queue.append(crs)

        return finish == numCourses