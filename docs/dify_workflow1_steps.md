# TACO 第6课：Dify 工作流1 言论分类器搭建步骤

## 一、创建 Workflow App

1. 打开 Dify。
2. 点击 Studio。
3. 点击 Create from Blank。
4. 类型选择 Workflow。
5. App 名称建议：
   TACO Statement Classifier
6. 创建后进入工作流编辑页面。

## 二、Start 节点

创建输入变量：

变量名：trump_statement
类型：Text
说明：输入一条特朗普相关言论。

## 三、LLM 节点

1. 添加 LLM 节点。
2. 模型选择课堂可用模型。
3. 把 src/lesson6/classifier_prompt.txt 的内容复制到 Prompt。
4. 确认变量引用是：
   {{trump_statement}}
5. 输出变量命名为：
   llm_output

## 四、Code 节点

1. 添加 Code 节点。
2. 输入变量连接 LLM 输出。
3. 参数名设置为：
   llm_output
4. 把 src/lesson6/code_node.py 中的 import 和 main 函数复制进去。
5. 输出应包含：
   hardness
   domain
   reasoning

## 五、End 节点

最终输出三个字段：

hardness
domain
reasoning

## 六、测试

使用 data/lesson6_manual_test_cases.txt 中的测试语句进行测试。

检查：

1. 是否能正常运行。
2. 输出是否是 JSON。
3. hardness 是否为 1-10。
4. domain 是否合法。
5. reasoning 是否清楚。
6. 和 expected_hardness 的误差是否 ≤ 2。
