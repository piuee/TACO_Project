# TACO 第6课：Prompt 调优指南

## 1. 如果分数普遍偏高

解决方法：

* 增加低强硬度 few-shot。
* 强调 1-3 分是模糊表态或观察性语言。
* 要求没有具体数字、期限或威胁时不要给高分。

## 2. 如果分数普遍偏低

解决方法：

* 增加强硬 few-shot。
* 强调出现 tariff、ban、sanction、impose、restrict、immediately 等词时分数应更高。
* 有具体税率和时间期限时通常是 7-9 分。

## 3. 如果 domain 经常错

解决方法：

* 在 Prompt 中补充 domain 定义。
* 给每个 domain 至少一个 few-shot 示例。
* tech、energy、fx 容易混，要增加例子。

## 4. 如果输出不是 JSON

解决方法：

* 在 Prompt 最后强调“只输出 JSON”。
* 不要让模型写解释段落。
* 用 Code 节点兜底清理。

## 5. 如果 reasoning 太长

解决方法：

* 要求 reasoning 不超过 30 个中文字符。
* 只写核心理由，不要写长篇分析。
