# Lesson 3 Test Log

| 文件 | 运行命令 | 是否成功 | 生成文件 | 备注 |
|---|---|---|---|---|
| read_market_data.py | python src\lesson3\read_market_data.py |  |  |  |
| spy_trend.py | python src\lesson3\spy_trend.py |  | data\spy_trend.png |  |
| four_assets_normalized.py | python src\lesson3\four_assets_normalized.py |  | data\four_assets_normalized.png |  |
| taco_events.py | python src\lesson3\taco_events.py |  | data\taco_events.png |  |
| correlation.py | python src\lesson3\correlation.py |  | data\correlation_matrix.csv |  |
| correlation_heatmap.py | python src\lesson3\correlation_heatmap.py |  | data\correlation_heatmap.png |  |

## 思考题

1. 为什么不能直接把 USO、GLD、SPY、QQQ 的原始价格放在同一张图里比较？
2. parse_dates=["date"] 的作用是什么？
3. ax.axvline() 为什么要配合 pd.Timestamp() 使用？
4. 相关系数接近 +1、0、-1 分别是什么意思？
5. 为什么说相关不等于因果？
