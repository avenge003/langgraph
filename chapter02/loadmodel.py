import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True, verbose=True)

# 初始化模型
def load_model():
    model = init_chat_model(
        os.getenv("MODEL_NAME"),
        model_provider="openai",
        temperature=0.5,
        max_tokens=1024,
        timeout=60,
        max_retries=3,
        base_url=os.getenv("DASHSCOPE_API_URL"),
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        extra_body={
            "thinking": {
                "type": "disabled"
                }
        }
    )
    return model