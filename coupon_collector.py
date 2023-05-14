import random
import matplotlib.pyplot as plt
import numpy as np


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


def run_coupon_collector_sim(num_of_nodes: int):  # クーポンコレクタのシュミレーションを実行
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

    return num_of_attempts


def exact_coupon_collector_average(num_of_nodes):
    num_of_run = 10000
    sum = 0

    for num in range(num_of_run):
        sum += run_coupon_collector_sim(num_of_nodes)

    average = sum / num_of_run
    return average


def main():
    min_nodes = 2
    max_nodes = 16

    plot_range = range(min_nodes, max_nodes+1)
    plot_value = []

    for num_of_nodes in plot_range:
        average = exact_coupon_collector_average(num_of_nodes)
        plot_value.append(average)
        print(average)

    #近似曲線
    a,b,c=np.polyfit(plot_range,plot_value,2)
    print('a='+str(a))
    print('b='+str(b))
    print('c='+str(c))

    # グラフの設定・表示
    plt.plot(plot_range, plot_value, marker="o", linestyle='--')
    plt.xlabel("Number of Vertexes")
    plt.ylabel("Number of Attempts")
    plt.xlim(0, max_nodes+1)
    plt.ylim(0, plot_value[len(plot_range)-1]+2)
    plt.grid(True)
    for i in range(1, len(plot_range)+1):
        plt.text(i, plot_value[i-1], plot_value[i-1])
    plt.show()


if __name__ == "__main__":
    main()
