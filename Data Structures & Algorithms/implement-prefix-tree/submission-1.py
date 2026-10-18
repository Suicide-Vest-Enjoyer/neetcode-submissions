class Node:
    __slots__ = ("next", "end")

    def __init__(self):
        self.next = {}
        self.end = False


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            nxt = cur.next.get(c)
            if nxt is None:
                nxt = cur.next[c] = Node()
            cur = nxt
        cur.end = True

    def _find(self, s: str):
        cur = self.root
        for c in s:
            cur = cur.next.get(c)
            if cur is None:
                return None
        return cur

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None