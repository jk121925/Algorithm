from BSTree import Node, BSTree

class AVLnode(Node):
    def __init__(self,data):
        super().__init__(data)
        self.height = 0

class AVLTree(BSTree):
    def get_height(self,node):
        if node is None:
            return -1
        
        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        return 1 + max(left_height,right_height)
    
    def get_balance(self,node):
        return self.get_height(node.left) - self.get_height(node.right)
    
    def _insert(self, node, data):
        if node is None:
            return AVLnode(data)
        if node.data > data:
            node.left = self._insert(node.left,data)
        else:
            node.right = self._insert(node.right,data)
        
        node.height = self.get_height(node)
        node= self.balancing(node)
        return node

    def _delete(self,node,data):
        if node is None:
            return 
        if node.data <data:
            node = node.right
        elif node.data > data:
            node = node.left
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self.find_most_left(node.right)
                node.data = temp.data
                self._delete(node.right, temp.data)
        return node
    def rotate_right(self,node):
        child=node.left
        node.left, child.right = child.right, node
        node.height = self.get_height(node)
        child.height = self.get_height(child)
        return child
    def rotate_left(self,node):
        child = node.right
        node.right, child.left = child.left, node
        node.height = self.get_height(node)
        child.height = self.get_height(child)
        return child
    def rotate_left_right(self,node):
        child = node.left
        grandchild = child.right
        child.right, node.left = grandchild.left, grandchild.right
        grandchild.left, grandchild.right = child,node
        child.height = self.get_height(child)
        node.height = self.get_height(node)
        grandchild.height = self.get_height(grandchild)

        return grandchild
    def rotate_right_left(self,node):
        child = node.right
        grandchild = child.left
        node.right,child.left = grandchild.left, grandchild.right
        grandchild.left,grandchild.right = node, child
        node.height = self.get_height(node)
        child.height = self.get_height(child)
        grandchild.height = self.get_height(grandchild)
        return grandchild

    def balancing(self,node):
        balance_factor = self.get_balance(node)
        if balance_factor == 2:
            if self.get_balance(node.left) >=0:
                node = self.rotate_right(node)
            else:
                node = self.rotate_left_right(node)
        elif balance_factor == -2:
            if self.get_balance(node.right) <=0:
                node = self.rotate_left(node)
            else:
                node = self.rotate_right_left(node)
        return node



def level_order(tree):
    q = [tree.root]
    res = []
    while q:
        node = q.pop(0)
        res.append((node.data, node.height, tree.get_balance(node)))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

def get_data(msg):
    print(msg, end=">>> ")
    data = input()
    if data.isdigit():
        return int(data)
    return None

if __name__ == "__main__":
    tree = AVLTree()

    while True:
        menu = """

실행할 명령어를 선택하세요.

[0] AVL 트리의 상태 출력 [(노드 값, 높이, 균형 지수), ...]
[1] 노드 추가
[2] 노드 삭제
[3] 노드 검색
[9] 끝내기

"""

        print(menu, end=" >>> ")
        command = int(input())
        print()

        if command == 0 and tree.root is not None:
            print(level_order(tree))
        elif command == 1:
            data = get_data("트리에 추가할 정수를 입력하세요.")
            if data is not None:
                tree.insert(data)
                print(f"{data}(을)를 트리에 추가했습니다.")
            else:
                print("값을 잘못 입력했습니다.")
        elif command == 2:
            data = get_data("트리에서 삭제할 정수를 입력하세요.")
            if data is not None:
                tree.delete(data)
                print(f"{data}(을)를 트리에서 삭제했습니다.")
            else:
                print("값을 잘못 입력했습니다.")
        elif command == 3:
            data = get_data("검색할 값을 입력하세요.")
            if data is not None:
                if data in tree:
                    print(f"{data}(이)가 리스트에 있습니다.")
                else:
                    print(f"{data}(이)가 리스트에 없습니다.")
            else:
                print("값을 잘못 입력했습니다.")
        elif command == 9:
            break
