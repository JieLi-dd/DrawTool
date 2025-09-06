import matplotlib.pyplot as plt
import numpy as np


def cloudrain(data, categories, colors=["#d36a87", "#ea9979", "#83b6b5", "#bcdfa7", "#a596ee"], figsize=(10, 8), save_path=None):
    fig, ax = plt.subplots(figsize=figsize)

    box_colors = violin_colors = colors
    # box_colors = violin_colors = ["#d36a87", "#ea9979", "#83b6b5", "#bcdfa7", "#a596ee"]
    # box_colors = violin_colors = ['#9bb55e', '#fcd744', '#dc8e4e', '#ba7ab1', '#ea617b']

    positions = np.arange(len(categories))
    box_width = 0.15
    violin_width = 0.5

    for i, category in enumerate(categories):
        data_points = data[category].values

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
            np.random.normal(positions[i] - box_width, 0.04, len(data_points)),
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

    if save_path is not None:
        plt.savefig(save_path)
    else:
        plt.show()