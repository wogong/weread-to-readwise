# 微信读书笔记 Readwise 转换器
将微信读书笔记转换为可导入 Readwise 的 CSV 文件。

## 如何使用
1. 下载代码到本地
2. 进入微信读书->笔记，点击“导出”
3. 点击底部的“复制到剪切板”
4. 把剪贴板内容粘贴进一个 txt 文件
5. `python3 weread2readwise.py --path [txt 文件地址]` 运行本工具，生成一个 CSV 文件
6. 在 Readwise [这个页面](https://readwise.io/import_bulk) 导入该 CSV 文件

## 注意
1. 可使用 --url 选项添加书籍 URL 地址，虽然我没发现有什么用
2. 可使用 --date 选项指定读书笔记的日期，默认为运行该工具日期

## 致谢
本工具启发自 https://github.com/mtfront/weread-notion

# weread2readwise
This tool converts Weread notes to a csv compatible with Readwise.

## How to use
        1. In Weread, go into your notes, click "export/导出"
        2. Click "Copy to clipboard/复制到剪贴板”
        3. Paste the copied notes into a txt file
        4. Run this script by typing 'weread2readwise.py --path [txt file path]', the script will create a csv file
        5. In Readwise, import the csv file in this page: https://readwise.io/import_bulk

## Notes
1. You can use the --url option to add the book URL address, although I didn't find it useful
2. You can use the --date option to specify the date of the book note, the default is the date the tool was run

## Acknowledgements
This tool was inspired by https://github.com/mtfront/weread-notion
