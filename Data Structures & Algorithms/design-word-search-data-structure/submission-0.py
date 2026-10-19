class Node:
    def __init__(self):
        self.next = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for v in word:
            if v not in cur.next:
                cur.next[v] = Node()
            cur = cur.next[v]

        cur.is_end = True

    def search(self, word: str) -> bool:

        def dfs(cur, i):
            if i == len(word):
                return cur.is_end

            v = word[i]

            if v == ".":
                for node in cur.next.values():
                    if dfs(node, i + 1):
                        return True
                return False

            if v not in cur.next:
                return False

            return dfs(cur.next[v], i + 1)

        return dfs(self.root, 0)