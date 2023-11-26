class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodeCount = {}

        for edge in edges:
            for node in edge:
                nodeCount[node] = nodeCount.get(node, 0) + 1

        for node, count in nodeCount.items():
            if count == len(edges):
                return node
