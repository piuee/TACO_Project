# TACO 第9课：FastAPI 后端测试记录

用途：本文件用于记录第9课 FastAPI 后端接口测试结果。

| 编号 | 输入言论                   | 状态码 | 是否返回 classification | 是否返回 taco_probability | 是否返回 market_prediction | 耗时 | 备注 |
| -- | ---------------------- | --: | ------------------- | --------------------- | ---------------------- | -- | -- |
| 1  | 25% tariffs            |     |                     |                       |                        |    |    |
| 2  | delay and negotiations |     |                     |                       |                        |    |    |
| 3  | something big          |     |                     |                       |                        |    |    |

## 测试问题

1. /health 是否正常返回 ok？
2. /docs 是否可以打开？
3. POST /analyze 是否返回完整 JSON？
4. 如果返回 500，错误原因是什么？
5. 如果返回 504，可能是什么原因？
6. 为什么 API Key 不能写在 main.py 里？
