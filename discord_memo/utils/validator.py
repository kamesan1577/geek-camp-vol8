import re

"""
以下パターンの場合True
^[a-z]: 小文字アルファベット
ぁ-ん: ひらがな
ァ-ヶ: カタカナ
一-龥: 漢字
0-9: 数字
_: 下線
-: ハイフン
🌀-🗿: 絵文字
"""


def is_valid_tag_name(tag_name: str) -> bool:
    pattern = r"^[a-zぁ-んァ-ヶ一-龥0-9_\-🌀-🗿]+$"
    return bool(re.match(pattern, tag_name))