# DrawTool
This is a drawing tool.

## 云雨图
### 特点：
1. 数据分布：展示每个特征的数据分布；
2. 中心趋势： 结合箱线图和散点图，展示数据分布的趋势；
3. 异常值： 显示数据分布的异常值；
4. 特征比较： 适合比较多个特征之间的数据分布。

### Usage
```python
import pandas as pd 
import numpy as np 
from drawbox.cloudrain import cloudrain

np.random.seed(42) 
data = pd.DataFrame({ 
    'Group A': np.random.normal(0, 1, 100), 
    'Group B': np.random.normal(2, 1.5, 100), 
    'Group C': np.random.normal(-1, 0.5, 100), 
    'Group D': np.random.normal(1, 2, 100) 
})
categories = ['Group A', 'Group B', 'Group C', 'Group D']

custom_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'] 
cloudrain(
    data, 
    categories, 
    colors=custom_colors, 
    figsize=(12, 8), 
    save_path='raincloud_plot.png'
)
```



## License
MIT