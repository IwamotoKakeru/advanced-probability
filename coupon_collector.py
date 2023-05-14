import random


class Node:  # クーポンコレクタノードの作成
    def __init__(self):
        self.node_num = 0
        self.visit_flag = False

    def __init__(self, node_num):
        self.node_num = node_num
        self.visit_flag = False

    def visit_node(self):
        self.visit_flag = True

    def get_visit_flag(self):
        return self.visit_flag


def main():  # クーポンコレクタのシュミレーションを実行
    num_of_nodes = 5
    current_node_num = 0
    num_of_attempts = 0
    all_visit_flag = False

    # クーポンコレクタの実体化
    node = []
    for num in range(num_of_nodes):
        node.append(Node(num))

    while (not all_visit_flag):
        node[current_node_num].visit_node()

        # 次のノードへの移動
        seed_num = current_node_num + random.randint(1, num_of_nodes-1)
        current_node_num = seed_num % num_of_nodes

        # すべてのノードを訪れたか確認
        for num in range(num_of_nodes):
            if (not node[num].get_visit_flag()):
                all_visit_flag = False
                break
            else:
                all_visit_flag = True

        num_of_attempts += 1

    print(num_of_attempts)


if __name__ == "__main__":
    main()
