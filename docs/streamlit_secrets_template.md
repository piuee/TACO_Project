# Streamlit Cloud Secrets 模板

请在 Streamlit Cloud 的 App Settings → Secrets 中填写以下内容。

注意：

* 这里的内容是模板。
* 不要把真实 API Key 写进 GitHub。
* 不要把真实 Secrets 截图公开展示。
* 不要创建并提交真实 .streamlit/secrets.toml。

```toml
DIFY_API_KEY = "app-xxxxxxxxxxxx"
WF1_ID = "your_workflow_1_id"
WF2_ID = "your_workflow_2_id"
WF3_ID = "your_workflow_3_id"
DIFY_BASE_URL = "https://api.dify.ai"
```

变量说明：

* DIFY_API_KEY：Dify Workflow API Key
* WF1_ID：第6课 Statement Classifier 工作流 ID
* WF2_ID：第7课 TACO Probability Engine 工作流 ID
* WF3_ID：第8课 Market Impact Predictor 工作流 ID
* DIFY_BASE_URL：Dify API 基础地址，默认 https://api.dify.ai
