# TACO 第5课：Dify 知识库上传步骤

## 一、准备本地文件

先运行：

python src/lesson5/check_rag_cases.py
python src/lesson5/make_kb.py
python src/lesson5/make_test_queries.py

需要生成：

* data/taco_kb.txt
* data/dify_test_queries.txt

## 二、上传到 Dify

1. 打开 Dify。
2. 点击顶部 Knowledge。
3. 点击 Create Knowledge。
4. 选择上传文件。
5. 上传 data/taco_kb.txt。
6. 选择 High Quality。
7. 等待知识库状态变成 Available。
8. 使用 data/dify_test_queries.txt 中的测试言论进行检索。
9. 记录 Top-3 检索结果。
10. 判断结果是否合理。

## 三、注意事项

* taco_kb.txt 是上传到 Dify 的知识库文件。
* dify_test_queries.txt 是检索测试用语。
* 如果 Dify 无法访问，可以先看老师投屏演示。
* 不要把 API Key 上传到 GitHub。
* 不要截图公开展示 API Key。
* 如果检索效果不好，先检查 taco_kb.txt 里每条案例是否用 --- 分隔。
* 如果英文查询效果不好，可以考虑给案例库补充英文摘要。
