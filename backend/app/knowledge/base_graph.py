"""
Base class for graph-based knowledge structures.
"""

from collections import defaultdict


class BaseGraph:

    def __init__(self):
        self.graph = defaultdict(set)
        self._build()

    def _build(self):
        raise NotImplementedError

    def _add(self, parent: str, child: str):
        self.graph[parent].add(child)

    def children(self, node: str) -> list[str]:
        return sorted(self.graph.get(node, []))

    def has(self, node: str) -> bool:
        """Return True if the node exists anywhere in the graph."""
        if node in self.graph:
            return True
        return any(node in children for children in self.graph.values())

    def all_nodes(self) -> list[str]:
        nodes = set(self.graph.keys())

        for values in self.graph.values():
            nodes.update(values)

        return sorted(nodes)