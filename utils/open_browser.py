import webbrowser
from langchain.tools import tool

@tool
def open_browser(url):
    """在默认浏览器中打开指定url"""
    try:
        webbrowser.open(url)
        return f"成功打开{url}"
    except Exception as e:
        return f"打开url失败 {e}"