# TACO 第7课：Workflow 2 测试记录

用途：本文件用于记录第7课 Dify 工作流 2 的课堂测试结果。

| 测试     | 输入摘要                   | hardness | domain | 预期概率 | 实际概率 | confidence | 是否合理 | 备注 |
| ------ | ---------------------- | -------: | ------ | ---: | ---: | ---------- | ---- | -- |
| A 强硬关税 | 100% tariffs on China  |        9 | tariff |      |      |            |      |    |
| B 软化谈判 | open to dialogue       |        3 | tariff |      |      |            |      |    |
| C 模糊表态 | might do something big |        5 | other  |      |      |            |      |    |

## 分析问题

请回答：

1. A / B / C 三组测试的概率有什么差异？
2. 哪一组 confidence 最低？为什么？
3. Knowledge Retrieval 返回的案例是否和输入相关？
4. 概率判断是否引用了历史案例？
5. 如果结果不合理，应该调整 LLM① 查询、知识库内容，还是 LLM② Prompt？
