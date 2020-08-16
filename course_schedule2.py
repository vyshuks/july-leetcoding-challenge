"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = [[] for x in range(numCourses)]
        ind = [0 for x in range(numCourses)]
        res = [] 
        for p in prerequisites:
            if p[0] not in map[p[1]]:
                ind[p[0]] += 1
                map[p[1]].append(p[0])
        st = []
        for i in range(numCourses):
            if ind[i] == 0:
                st.append(i)
        count = 0
        while st:
            tmp = st[0]
            st.pop(0)
            res.append(tmp)
            count += 1
            for i in map[tmp]:
                ind[i] -= 1
                if ind[i] == 0:
                    st.append(i)
                         
        if count < numCourses:
            return []
        else: 
            return res