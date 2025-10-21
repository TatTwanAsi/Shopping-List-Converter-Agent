from docx import Document
import re
import requests
from langchain.tools import tool

# @tool   # 定义工具的修饰符
def get_shopping_items(file_path):
    """返回一个items列表, 元素是[数量, 商品url]"""

    shopping_items = []
    try:
        document = Document(file_path)

    except FileNotFoundError as e:
        print("Error! file not found!!: {e}")
        raise e

    for paragraph in document.paragraphs:
        text = paragraph.text
        pattern = r'(?:\(([^)]+)\)\s*)?(https?://[^\s]+)'
        item_matches = re.findall(pattern, text)
        for count, url in item_matches:
            number = re.findall(r'\d+', count)
            shopping_items.append({
                'count' : int(number[0]) if number else 1, 
                'url' : url
            })

    
    return shopping_items