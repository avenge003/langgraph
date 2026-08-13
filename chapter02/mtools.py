from langchain.tools import tool
from typing import Literal

@tool(parse_docstring=True)
def get_weather(city: str = "北京") -> str:
    """
    获取城市的天气

    Args:
        city: 城市名称，默认值为北京
    """
    return f"{city}的天气是晴朗的"

@tool(parse_docstring=True)
def get_news(domain: Literal["科技", "社会", "经济", "文化", "国际"]):
    """
    获取特定领域的新闻

    Args:
        domain: 新闻领域，默认值为科技、社会、经济、文化、国际
    """
    news_content = ""
    if domain == "科技":
        news_content = "科技新闻内容"
    elif domain == "社会":
        news_content = "社会新闻内容"
    elif domain == "经济":
        news_content = "经济新闻内容"
    elif domain == "文化":
        news_content = "文化新闻内容"
    elif domain == "国际":
        news_content = "国际新闻内容"
    else:
        news_content = "未知新闻领域"
    return news_content