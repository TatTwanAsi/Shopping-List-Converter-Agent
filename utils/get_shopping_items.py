from docx import Document
import re
import requests

def get_shopping_items(file_path):
    """返回一个items列表, 元素是[数量, 商品url]"""

    shopping_items = []
    try:
        document = Document(file_path)

    except FileNotFoundError as e:
        print("Error! file not found!!: {e}")

    for paragraph in document.paragraphs:
        text = paragraph.text
        pattern = r'\(x(\d+)\)\s*(https?://[^\s]+)'
        item_matches = re.findall(pattern, text)
        for count, url in item_matches:
            shopping_items.append([int(count), url])
    
    return shopping_items