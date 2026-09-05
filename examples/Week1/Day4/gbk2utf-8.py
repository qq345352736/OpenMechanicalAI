# 一次性转换文件编码
with open('sales.csv', 'r', encoding='gbk') as f:
    content = f.read()

with open('sales_utf8.csv', 'w', encoding='utf-8') as f:
    f.write(content)

print("转换完成，新文件：sales_utf8.csv")