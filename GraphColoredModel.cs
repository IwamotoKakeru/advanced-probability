using System;
using System.Collections.Generic;

public class GraphColoringSimulatedAnnealing
{
    private int[] colors; // ノードの色
    private int[,] adjacencyMatrix; // 隣接行列
    private int numNodes; // ノードの数
    private int numColors; // 色の数
    private double temperature; // 温度
    private double coolingRate; // 冷却率

    public GraphColoringSimulatedAnnealing(int[,] adjacencyMatrix, int numColors, double initialTemperature, double coolingRate)
    {
        this.adjacencyMatrix = adjacencyMatrix;
        this.numNodes = adjacencyMatrix.GetLength(0);
        this.numColors = numColors;
        this.temperature = initialTemperature;
        this.coolingRate = coolingRate;
    }

    // グラフ彩色問題を解く
    public int[] Solve()
    {
        // ノードの色を初期化
        colors = new int[numNodes];

        // 初期解をランダムに生成
        Random random = new Random();
        for (int i = 0; i < numNodes; i++)
        {
            colors[i] = random.Next(numColors);
        }

        // 焼きなまし法を実行
        while (temperature > 0.1)
        {
            for (int i = 0; i < 100; i++) // 100回の反復ステップ
            {
                // ランダムなノードを選択
                int randomNode = random.Next(numNodes);

                // ノードの色を変更してエネルギーを計算
                int oldColor = colors[randomNode];
                int newColor = random.Next(numColors);
                colors[randomNode] = newColor;
                int deltaEnergy = CalculateDeltaEnergy(randomNode, oldColor, newColor);

                // 変更を受け入れるか判定
                if (deltaEnergy < 0 || random.NextDouble() < Math.Exp(-deltaEnergy / temperature))
                {
                    // 変更を受け入れる
                    continue;
                }
                else
                {
                    // 変更を破棄して元の色に戻す
                    colors[randomNode] = oldColor;
                }
            }

            // 温度を下げる
            temperature *= coolingRate;
        }

        return colors;
    }

    // ノードの色変更によるエネルギーの変化を計算
    private int CalculateDeltaEnergy(int node, int oldColor, int newColor)
    {
        int deltaEnergy = 0;
        for (int i = 0; i < numNodes; i++)
        {
            if (adjacencyMatrix[node, i] == 1 && i != node)
            {
                if (colors[i] == oldColor && colors[i] != newColor)
                {
                    deltaEnergy++;
                }
                else if (colors[i] == newColor && colors[i] != oldColor)
                {
                    deltaEnergy--;
                }
            }
        }
        return deltaEnergy;
    }
}

class Program
{
    static void Main(string[] args)
    {
        int[,] adjacencyMatrix = new int[,]
        {
            { 0, 1, 1, 0 },
            { 1, 0, 1, 1 },
            { 1, 1, 0, 1 },
            { 0, 1, 1, 0 }
        };

        int numColors = 3;
        double initialTemperature = 100.0;
        double coolingRate = 0.95;

        GraphColoringSimulatedAnnealing solver = new GraphColoringSimulatedAnnealing(adjacencyMatrix, numColors, initialTemperature, coolingRate);
        int[] colors = solver.Solve();

        Console.WriteLine("Node Colors:");
        for (int i = 0; i < colors.Length; i++)
        {
            Console.WriteLine($"Node {i + 1}: Color {colors[i] + 1}");
        }
    }
}
