# TACO 第10课：Streamlit 前端开发步骤

用途：本文件说明第10课 Streamlit 前端的创建、启动和测试方法。

## 一、本节课目标

把第9课 FastAPI 后端接口 POST /analyze 接入 Streamlit 前端页面。

用户在网页中输入 Trump 相关言论，点击 Analyze 后，页面展示：

* 强硬度 hardness
* TACO 概率 taco_probability
* 置信度 confidence
* USO / GLD / SPY 市场方向
* 市场方向柱状图
* 分析理由
* 完整 JSON

## 二、为什么需要前端

第9课的后端只能通过 Swagger UI 或代码调用。
第10课的前端让普通用户可以通过网页输入和查看结果。

结构：

Streamlit 前端
↓
FastAPI 后端
↓
Dify 三个工作流
↓
返回完整 JSON
↓
Streamlit 展示结果

## 三、项目结构

不要在项目根目录创建 app.py。
因为项目中已经有 app 文件夹作为 FastAPI 后端包。

第10课前端文件统一放在：

frontend/streamlit_app.py

## 四、安装依赖

pip install streamlit requests matplotlib

如果网络慢：

pip install streamlit requests matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple

## 五、启动后端

终端 1：

cd D:\TACO\TACO_Project
python -m uvicorn app.main:app --reload

确认可以访问：

http://127.0.0.1:8000/health

## 六、启动前端

终端 2：

cd D:\TACO\TACO_Project
streamlit run frontend/streamlit_app.py

浏览器打开：

http://localhost:8501

## 七、测试输入

Trump threatens to impose 25% tariffs on imported goods next week.

Trump says he may delay the tariff plan and continue negotiations.

We might do something big next week.

## 八、页面功能检查

页面应包含：

1. 标题 TACO雷达
2. 输入框
3. Analyze 按钮
4. Clear 按钮
5. 强硬度指标卡
6. TACO 概率指标卡
7. 置信度指标卡
8. USO / GLD / SPY 方向指标
9. 市场方向柱状图
10. 分析理由
11. key_cases
12. 完整 JSON 展开区
13. 最近 5 次分析记录
14. 投资建议免责声明

## 九、常见问题

1. 前端显示无法连接后端
   请先启动 FastAPI 后端：
   python -m uvicorn app.main:app --reload

2. 后端返回 500
   检查 .env、Dify API Key、Workflow ID、工作流是否发布。

3. 后端返回 504
   Dify 响应超时，请稍后重试。

4. 页面结果点击后消失
   检查是否使用 st.session_state 保存 result。

5. 图表多次点击后变慢
   检查是否在 st.pyplot(fig) 后使用 plt.close(fig)。

6. KeyError
   检查是否使用 get() 读取嵌套 JSON。
