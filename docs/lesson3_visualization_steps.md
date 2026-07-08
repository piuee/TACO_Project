# Lesson 3 - Financial Data Visualization

第3课主题：金融数据可视化与事件标注。

## 运行前检查

请先确认下面的数据文件存在：

```powershell
data\market_data_2018_2025.csv
```

这个 CSV 应包含：

- date
- USO_Close
- GLD_Close
- SPY_Close
- QQQ_Close

## 推荐运行命令

```powershell
cd D:\TACO\TACO_Project
python src\lesson3\read_market_data.py
python src\lesson3\spy_trend.py
python src\lesson3\four_assets_normalized.py
python src\lesson3\taco_events.py
python src\lesson3\correlation.py
python src\lesson3\correlation_heatmap.py
```

也可以一次运行全部第3课脚本：

```powershell
python src\lesson3\lesson3_run_all.py
```

## 关键概念

`parse_dates=["date"]` 的作用是把 CSV 中的 date 列从普通字符串转换成日期类型。这样 pandas 和 matplotlib 才能更自然地按时间顺序筛选、索引和绘图。

`fig` 可以理解为整张画布，`ax` 是画布上的一个坐标系。第3课使用 `fig, ax = plt.subplots()`，再用 `ax.plot()`、`ax.set_title()` 等方法控制图表。

四资产归一化公式：

```python
df_norm = price_df / price_df.iloc[0] * 100
```

它表示把每个资产第一天的价格设为 100，后面的数值表示相对第一天的变化。这样 USO、GLD、SPY、QQQ 即使原始价格不同，也可以放在同一张图中比较走势。

`ax.axvline()` 用来画竖线，适合标注某个事件发生的日期。事件日期建议写成 `pd.Timestamp(date)`，这样它和 pandas 的日期索引类型一致，画图时更稳定。

相关系数范围是 -1 到 +1：

- 接近 +1：两个变量通常同向变化。
- 接近 0：两个变量线性关系较弱。
- 接近 -1：两个变量通常反向变化。

相关不等于因果。即使两个变量一起变化，也不能直接说明一个变量导致了另一个变量变化，还需要结合事件背景、机制和更多证据。

## 输出文件

第3课输出 PNG 文件可用于 GitHub 项目展示：

- data\spy_trend.png
- data\four_assets_normalized.png
- data\taco_events.png
- data\correlation_heatmap.png（如果 taco_cases.csv 可用）

相关矩阵也会保存为：

- data\correlation_matrix.csv（如果 taco_cases.csv 可用）
