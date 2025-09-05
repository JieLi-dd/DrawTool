import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 创建数据
    data = {
        'A': [5.74507123, 4.792603548, 5.971532807, 7.284544785, 4.648769938, 4.648794565, 7.368819223, 4.222594673,
              3.787259596, 4.247364435, 6.373103177, 5.493126664, 4.205359694, 5.76900115, 5.145616324, 6.452967486,
              3.946920359, 4.508506678, 4.41183777, 2.804727578, 3.444180416, 5.391582908, 5.007670185, 4.6481193],
        'B': [5.301555, 6.495226, 6.588743, 6.037267, 6.806457, 7.484861, 9.263423, 7.578967, 6.731845, 7.856801,
              7.567885, 6.912605, 5.983848, 5.182183, 6.464182, 8.027679, 7.256912, 5.505113, 7.207817, 7.462381,
              5.939371, 7.18447, 7.06955, 5.628436],
        'C': [6.357787, 6.560785, 7.083051, 7.053802, 4.622331, 5.062175, 6.515035, 4.762185, 8.133033, 4.047912,
              5.848215, 6.588317, 6.280992, 5.3773, 5.791878, 5.506999, 5.410635, 6.849602, 6.357015, 5.30709, 6.8996,
              6.3073, 6.812562, 6.629629],
        'D': [6.507809, 6.991674, 9.345128, 9.098666, 7.962377, 8.211189, 10.2998, 7.053641, 6.633561, 8.270709,
              8.615161, 11.37711, 9.710763, 6.961573, 6.382854, 8.885455, 5.62358, 11.29663, 10.12299, 7.155484,
              4.916358, 10.43697, 7.793828, 10.22807],
        'E': [1.927244, 3.220812, 4.006817, 4.061075, 3.414915, 4.809705, 2.612093, 4.264503, 3.016744, 2.151077,
              3.159455, 2.593988, 6.193284, 5.146132, 3.989636, 5.923927, 4.100579, 2.880331, 5.980061, 4.700583,
              2.65158, 3.75256, 2.861696, 2.20236]
    }

    # 转换为DataFrame
    df = pd.DataFrame(data)

    # 数据集的特征变量名
    categories = ['A', 'B', 'C', 'D', 'E']

    fig, ax = plt.subplots(figsize=(10, 8))

    box_colors = violin_colors = ["#d36a87", "#ea9979", "#83b6b5", "#bcdfa7", "#a596ee"]
    # box_colors = violin_colors = ['#9bb55e', '#fcd744', '#dc8e4e', '#ba7ab1', '#ea617b']

    positions = np.arange(len(categories))
    box_width = 0.15
    violin_width = 0.5

    for i, category in enumerate(categories):
        data_points = df[category].values

        box_pos = positions[i] - box_width / 100
        box = ax.boxplot(
            data_points,
            positions=[box_pos],
            widths=box_width,
            patch_artist=True,
            showfliers=False,
            notch=True,
            medianprops={"color": "black", "linewidth": 3},
            boxprops={'facecolor': box_colors[i], 'edgecolor': violin_colors[i], 'linewidth': 2},
            whiskerprops={'color': violin_colors[i], 'linewidth': 3},
            capprops={'color': violin_colors[i], 'linewidth': 3},
        )

        violin_pos = positions[i] + box_width / 50
        violin = ax.violinplot(
            data_points,
            positions=[violin_pos],
            widths=violin_width,
            showextrema=False,
            showmedians=False,
            showmeans=False,
        )
        for pc in violin['bodies']:
            pc.set_facecolor(violin_colors[i])
            pc.set_edgecolor(violin_colors[i])
            pc.set_alpha(0.35)
            vertices = pc.get_paths()[0].vertices
            vertices[:, 0] = np.where(vertices[:, 0] > violin_pos, vertices[:, 0], violin_pos)

        ax.scatter(
            np.random.normal(positions[i]-box_width, 0.04, len(data_points)),
            data_points,
            alpha=0.8,
            color=violin_colors[i],
            edgecolors='white',
            linewidth=0.58,
            s=50,
            zorder=3
        )

    ax.set_xticks(positions)
    ax.set_xticklabels(categories, fontsize=20)

    ax.set_ylabel('Value', fontsize=20)
    ax.set_yticklabels(ax.get_yticks(), fontsize=20)

    ax.grid(axis='y', linestyle='--', alpha=0.7)

    for spine in ['top', 'right', 'bottom', 'left']:
        ax.spines[spine].set_visible(True)
        ax.spines[spine].set_linewidth(1)
        ax.spines[spine].set_color('gray')

    plt.title('Raincloud plots', pad=20, fontsize=22)
    plt.tight_layout()
    plt.show()