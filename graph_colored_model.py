import numpy as np
import random
import math


class GraphColoringSimulatedAnnealing:
    def __init__(self, adjacency_matrix, num_colors, initial_temperature, cooling_rate):
        self.adjacency_matrix = adjacency_matrix
        self.num_nodes = adjacency_matrix.shape[0]
        self.num_colors = num_colors
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def solve(self):
        # ノードの色を初期化
        colors = np.random.randint(
            low=0, high=self.num_colors, size=self.num_nodes)

        # 焼きなまし法を実行
        while self.temperature > 0.1:
            for _ in range(100):  # 100回の反復ステップ
                # ランダムなノードを選択
                random_node = random.randint(0, self.num_nodes - 1)

                # ノードの色を変更してエネルギーを計算
                old_color = colors[random_node]
                new_color = random.randint(0, self.num_colors - 1)
                delta_energy = self.calculate_delta_energy(
                    colors, random_node, old_color, new_color)

                # 変更を受け入れるか判定
                if delta_energy < 0 or random.random() < math.exp(delta_energy / self.temperature):
                    # 変更を受け入れる
                    colors[random_node] = new_color
                else:
                    # 変更を破棄して元の色に戻す
                    colors[random_node] = old_color

            # 温度を下げる
            self.temperature *= self.cooling_rate

        return colors

    def calculate_delta_energy(self, colors, node, old_color, new_color):
        delta_energy = 0
        for i in range(self.num_nodes):
            if self.adjacency_matrix[node, i] == 1 and i != node:
                if colors[i] == old_color and colors[i] != new_color:
                    delta_energy += 1
                elif colors[i] == new_color and colors[i] != old_color:
                    delta_energy -= 1
        return delta_energy


adjacency_matrix = np.array([[0, 1, 1, 0],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [0, 1, 1, 0]])

num_colors = 4
initial_temperature = 100.0
cooling_rate = 0.95

solver = GraphColoringSimulatedAnnealing(
    adjacency_matrix, num_colors, initial_temperature, cooling_rate)
colors = solver.solve()

print("Node Colors:")
for i in range(len(colors)):
    print(f"Node {i + 1}: Color {colors[i] + 1}")
