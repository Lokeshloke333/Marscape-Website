import re
content = open('index.html', encoding='utf-8').read()
# Find all elements with wixui-rich-text or wixui-button or wixui-box
# The regex looks for class="... wixui-rich-text ..." id="comp-..."
ids = re.findall(r'class="[^"]*(?:wixui-rich-text|wixui-button|wixui-box)[^"]*"[^>]*id="(comp-[^"]+)"', content)
# Sometimes id is before class
ids2 = re.findall(r'id="(comp-[^"]+)"[^>]*class="[^"]*(?:wixui-rich-text|wixui-button|wixui-box)[^"]*"', content)
all_ids = set(ids + ids2)
print(','.join(['#' + i for i in all_ids]))
