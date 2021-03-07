#
#  Covert PDF into text files
#
import requests
import random
import time
import urllib
import json
import pdfplumber
import re
import sys
pdf_saving_path = './pdf/'
txt_saving_path = './txt/'

def main(argv):
    with pdfplumber.open(pdf_saving_path + '五方光电招股说明书0.pdf') as pdf:
            txt_file_path = txt_saving_path + "aaaaaa" + ".txt"
            f = open(txt_file_path, "wb")
            page_count = len(pdf.pages)
            print(page_count)  # 得到页数
            for page in pdf.pages:
                print('---------- 第[%d]页 ----------' % page.page_number)
                # 获取当前页面的全部文本信息，包括表格中的文字
                #print(page.extract_text())
                f.write(bytes(page.extract_text(), encoding="utf8"))
                for pdf_table in page.extract_tables(table_settings={"vertical_strategy": "text",
                                                                     "horizontal_strategy": "lines",
                                                                     "intersection_tolerance": 20}):  # 边缘相交合并单元格大小
                    # print(pdf_table)
                    for row in pdf_table:
                        # 去掉回车换行
                        famatrow = [re.sub('\s+', '', cell) if cell is not None else None for cell in row]
                        print(famatrow)
                        if isinstance(famatrow,list) is True:
                            if famatrow[0] is not None:
                                f.write(bytes(famatrow[0], encoding="utf8"))
                        else:
                            if famatrow is not None:
                                f.write(bytes(famatrow, encoding="utf8"))
            f.close()


if __name__ == '__main__':
    main(sys.argv)
