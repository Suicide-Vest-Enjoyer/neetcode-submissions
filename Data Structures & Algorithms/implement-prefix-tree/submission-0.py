class Node:
    def __init__(self):
        self.pos = {}
        self.end = False
    


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, v in enumerate(word):
            if v not in cur.pos:
                cur.pos[v] = Node()
            cur = cur.pos.get(v)
            if i + 1 >= len(word):
                cur.end = True
          
    def search(self, word: str) -> bool:
        cur = self.root
        for i, v in enumerate(word):
            if v not in cur.pos.keys():
                return False
            cur = cur.pos.get(v)
            if i+1 >= len(word):
                return True if cur.end else False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i, v in enumerate(prefix):
            if v not in cur.pos.keys():
                return False
            cur = cur.pos.get(v)
        return True