# TACO 第4课：历史案例量化分析

本节课目标：
使用 taco_cases.csv 分析 20 个历史案例，观察 TACO / HOLD 的数量、不同资产的 5 日市场反应、不同领域的差异，并生成第5课 RAG 知识库需要的 rag_cases.csv。

运行顺序：

1. python src/lesson4/load_cases.py
2. python src/lesson4/check_cases.py
3. python src/lesson4/boxplot_taco_vs_hold.py
4. python src/lesson4/scatter_hardness_uso.py
5. python src/lesson4/domain_analysis.py
6. python src/lesson4/format_rag.py

生成文件：

* data/boxplot_taco_vs_hold.png
* data/scatter_hardness_uso.png
* data/domain_summary.csv
* data/domain_uso_bar.png
* data/rag_cases.csv

注意：

* taco_cases.csv 放在项目根目录。
* result 如果是 NOT_TACO，会被统一视为 HOLD。
* rag_cases.csv 是第5课 Dify 知识库的输入文件。
