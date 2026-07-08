# TACO 第7课：Dify 工作流 2——TACO 概率引擎

用途：本文件说明第7课 Dify 网页端工作流的搭建步骤，供学生手动操作时参考。

## 一、本节课目标

使用第6课输出的 hardness、domain、reasoning，结合第5课创建的 TACO 知识库，检索相似历史案例，并输出 TACO 概率。

## 二、工作流结构

Start
输入 hardness / domain / reasoning

LLM① Format Retrieval Query
把结构化结果转换成自然语言检索查询

Knowledge Retrieval
从 TACO 知识库中检索 Top-3 相似案例

LLM② Probability Engine
根据相似案例输出 TACO 概率和置信度

Code Validate Probability Output
清洗 JSON，保证概率在 0-100 之间

End
输出 taco_probability / confidence / reasoning / key_cases

## 三、Dify 操作步骤

1. 打开 Dify。
2. 进入 Studio。
3. Create from Blank。
4. 选择 Workflow。
5. 应用名称建议：TACO Probability Engine。
6. 配置 Start 节点，添加：

   * hardness
   * domain
   * reasoning
7. 添加 LLM① 节点，粘贴 src/lesson7/format_query_prompt.txt。
8. 添加 Knowledge Retrieval 节点，选择第5课创建的 TACO 案例库。
9. 设置 Top-K = 3。
10. 添加 LLM② 节点，粘贴 src/lesson7/probability_prompt.txt。
11. 添加 Code 节点，粘贴 src/lesson7/validate_probability_code.py。
12. 配置 End 节点，输出：

    * taco_probability
    * confidence
    * reasoning
    * key_cases
13. 使用 src/lesson7/lesson7_test_inputs.txt 中的 A / B / C 三组数据测试。

## 四、测试要求

至少测试三组：

A：强硬关税
B：软化谈判
C：模糊表态

每组记录：

* 输入 hardness
* 输入 domain
* 输入 reasoning
* taco_probability
* confidence
* reasoning
* key_cases
* 是否合理

## 五、注意事项

* probability 表示这次有多大概率 TACO。
* confidence 表示 AI 对这个概率有多大把握。
* 如果检索案例不相关，不能盲目相信概率。
* 如果案例很少或结果冲突，confidence 应该偏低。
* 不要把 Dify API Key 写进代码。
* 本节课重点是网页端搭建工作流，不是写 API 代码。
