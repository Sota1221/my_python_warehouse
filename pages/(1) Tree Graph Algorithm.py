import streamlit as st

st.title("Tree/Graph Algorithm")
st.text("まず探索アルゴリズムを紹介します。\nその後、それ以外のTree, Graph特有のよく使うアルゴリズムを紹介します。")

st.markdown("# Search Algorithms")

st.markdown("## Depth First Search")
st.text("いわゆる「DFS」「深さS優先探索」です。")

st.markdown("### Recursive DFS for Tree")
st.text("再帰を利用する実装です。")
st.text("treeを探索する場合。")
code = """
def dfs(node):
    if node is None:
        return
    print(node.val)
    for child in node.children:
        dfs(node)

dfs(root)
"""
st.code(code, language="python")

st.markdown("### Preorder DFS for Binary Tree")
st.text("Binary Tree (二分木)を探索場合は、以下の3種類のdfsのたどり方があります。")
code = """
def preorder(root):
    if root is None:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
"""
st.code(code, language="python")

st.markdown("### Inorder DFS for Binary Tree")
code = """
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
"""
st.code(code, language="python")
st.text("BST(Binary Search Tree, 二分探索木)を小さい要素から辿るときによく使います。")
st.markdown("#### Related Problems")
st.markdown("* [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)")

st.markdown("### Postorder DFS for Binary Tree")
code = """
def postorder(root):
    postorder(root.left)
    postorder(root.right)
    print(root.val)
"""
st.code(code, language="python")
st.text("binary treeでなくとも、全てのchild(next node)を回ってからそれらのparentにアクセスする場合、postorderと見なせます。\npostorderで拾っていった要素を逆順にソートすると topological sort(トポロジカルソート)になります。")


st.markdown("### Recursive DFS for Graph")
st.text("続いて、dfsでグラフを探索する場合です。treeのときとほぼ同じ考え方です。")
st.text("Gは現在のノードに対し、隣接したノードのセットを返す辞書です。")
code = """
def dfs(node):
    if node in visited:
        return
    print(node.val)
    visited.add(node)
    for neighbor_node in G[node]:
        dfs(neighbor_node)

visited = set()
dfs(start_node)
"""
st.code(code, language="python")


st.markdown("### Recursive DFS for Grid")
st.text("グリッドを探索する場合もほぼ同様です。\nvisitedを使う代わりにグリッド上の値を-1や#などに置き換えていやり方もよく使われます。")
code = """
def dfs(r, c):
    if not (0 <= r < ROW and 0 <= c < COL) or grid[r][c] == -1:
        return
    print(grid[r][c].val)
    grid[r][c] = -1 # mark as visited
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dfs(r + dr, c + dc)

ROW, COL = len(grid), len(grid[0])
dfs(start_r, start_c)
"""
st.text("特定パスを見つける場合はfor文を抜けた後、grid[r][c]をもとの値に戻すやり方がよく使われます。")
st.code(code, language="python")
st.text("Time Complexity: O(n)\nSpace Complexity: O(n)")


st.markdown("### Iterative DFS for Tree")
st.text("stackを用いた繰り返し処理による実装です。")
st.text("treeを探索する場合。")
code = """
def dfs(root):
    stack = [root]
    while stack:
        curr_node = stack.pop()
        print(curr_node.val)
        for child in curr_node.children:
            if child:
                stack.append(child)

dfs(root)
"""
st.code(code, language="python")


st.markdown("### Iterative DFS for Graph")
st.text("グラフを探索する場合。")
code = """
def dfs(start_node):
    stack, visited = [start_node], {start_node}
    while stack:
        curr_node = stack.pop()
        print(curr_node.val)
        for neighbor_node in G[curr_node]:
            if neibor_node not in visited:
                stack.append(neighbor_node)
                visited.add(neighbor_node)
"""
st.code(code, language="python")
st.text("Time Complexity: O(n)\nSpace Complexity: O(n)")


st.markdown("### Iterative DFS for Grid")
st.text("グリッドを探索する場合。")
code = """
def dfs(start_r, start_c):
    stack = [(start_r, start_c))]
    while stack:
        r, c = stack.pop()
        print(grid[curr_r][curr_c])
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if grid[r + dr][c + dc] != -1:
                grid[r + dr][c + dc] = -1
                stack.append((r + dr, c + dc))

dfs(start_r, start_c)
"""
st.code(code, language="python")
st.text("Time Complexity: O(n)\nSpace Complexity: O(n)")



st.markdown("## Breadth First Search for Tree")
st.text("いわゆる「BFS」「幅優先探索」です。以下はtree構造で探索する場合です。")

st.markdown("### Iterative BFS for Tree")
st.text("BFSはqueueを用いた繰り返し処理で実装します。")
code = """
from collections import deque
def bfs(root):
    queue = deque([root])
    while queue:
        curr_node = queue.popleft()
        print(curr_node.val)
        for child in curr_node.children:
            if child:
                queue.append(child)

bfs(root)
"""
st.code(code, language="python")

st.markdown("### Level Order BFS")
st.text("もし各レベルが終わるたびに何かの処理をする必要がある場合は次のようにします。")
code = """
from collections import deque
def level_order(root):
    queue = deque([root])
    while queue:
        size = len(queue)
        for _ in range(size):
            curr_node = queue.popleft()
            print(curr_node.val)
            for child in curr_node.children:
                if child:
                    queue.append(child)
        # Do SOMETHING HERE

level_order(root)
"""
st.code(code, language="python")


st.text("Time Complexity: O(n)\nSpace Complexity: O(n)")
st.markdown("#### Related Problems")
st.markdown("* [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)")
st.markdown("* [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)")


st.markdown("### BFS for Graph")
st.text("グラフで行う場合もTreeのときとほぼ同じです。")

code = """
from collections import deque
def bfs(start_node):
    queue, visited = [(start_node)], {start_node}
    while queue:
        curr_node = queue.popleft()
        print(curr_node.val)
        for neighbor_node in G[curr_node]:
            if neighbor_node not in visited:
                queue.append(neighbor_node)
                visited.add(neighbor_node)
"""
st.code(code, language="python")


st.markdown("### BFS for Grid")
st.text("グリッドもとくに大きな変更はありません。")

code = """
from collections import deque
def bfs(start_r, start_c):
    queue = [(start_r, start_c)]
    while queue:
        r, c = queue.popleft()
        print(curr_node.val)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if grid[r + dr][c + dc] != -1:
                queue.append((r + dr, c + dc))
                grid[r + dr][c + dc] = -1

bfs(start_r, start_c)
"""
st.code(code, language="python")


st.markdown("## Shortest Path for Weighted Graph")
st.markdown("### Dijekstra")
st.text("辺が非負の重みの場合、ダイクストラアルゴリズムを使います。経路復元も併せて実装します。\nここでは1からnまでのn個のノードから成る重み付きグラフがあるとします。")

code = """
from heapq import heappush, heappop
from collections import defaultdict
def dijkstra(start, goal):
    node_to_dist = {i: float("inf") for i in range(1, n + 1)}
    curr_to_prev = defaultdict(int)
    node_to_dist[start_node] = 0
    heap_candidates = []
    while heap_candidates:
        curr_dist, curr_node = heappop(heap_candidates)
        if curr_dist > node_to_dist[curr_node]:
            continue
        if curr_node == goal:
            break
        for neighbor_node, neighbor_weight in G[curr_node]:
            if curr_dist + neighbor_weight < node_to_dist[neighbor_node]:
                node_to_dist[neighbor_node] = curr_dist + neighbor_weight
                heappush(heap_candidates,(node_to_dist[neighbor_node], neighbor_node))
                curr_to_prev[neighbor_node] = curr_node
    return node_to_dist, curr_to_prev

def get_path(goal):
    curr_node, path = goal, []
    while curr_node:
        path.append(curr_node)
        curr_node = curr_to_prev[curr_node]
    return path[::-1]

node_to_dist, curr_to_prev = dijkstra()
path = get_path()
"""
st.code(code, language="python")
st.text("経路復元をしない場合は、curr_to_prevがいりません。")
st.text("Time Complexity: O((E + V)log V)\nSpace Complexity: O(V + E)")

st.markdown("#### Related Problems")
st.markdown("* [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/)")
st.markdown("* [1514. Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/)")


st.markdown("# Other Tree Algorithms")
st.markdown("## Trie")

code = """
class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
"""
st.code(code, language="python")
st.markdown("#### Related Problems")
st.markdown("* [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)")
st.markdown("* [212. Word Search II](https://leetcode.com/problems/word-search-ii/)")


st.markdown("# Other Graph Algorithms")
st.markdown("## Union Find")

code = """
def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def same(x, y):
    return find(x) == find(y)

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        x, y = y, x
    par[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1
"""
st.code(code, language="python")
st.markdown("#### Related Problems")
st.markdown("* [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)")
st.markdown("* [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)")