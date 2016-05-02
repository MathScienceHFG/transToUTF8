# -*- coding: utf-8 -*-

##
#   @file       TransToUTF8.py
#   @brief      递归搜索指定目录，将所有指定类型的文件，编码为UTF8(No BOM)+windows改行形式(CRLF)，并保持原名。
#
#   @author     legong.sun@gmail.com
#   @date       2016-05-02
#

import os
import sys
from FileManager import FileManager as fm

__author__ = 'legong.sun@gmail.com'

rootDir = sys.argv[1]           # 递归搜索 root dir
fileType = '.' + sys.argv[2]    # 指定文件类型， eg：cpp, hpp, py

codeType = '.utf8'
srcDirList = fm.findFiles(rootDir, fileType)                    # src files:  *.fileType

# trans all src files into dst type, with same names
for srcDir in srcDirList:
    # using nkf32.exe to trans the file
    # download from: http://www.vector.co.jp/soft/win95/util/se295331.html
    os.system("nkf32.exe -w -Lw --overwrite {}".format(srcDir))
    print "finished", srcDir
    # -j            :JISコード(ISO-2022-JP)を出力(省略可能)
    # -e            :EUCコードを出力
    # -s            :Shift-JISコードを出力
    # -w            :UTF-8コードを出力（BOM無し）
    # -Lu           :unix改行形式(LF)に変換
    # -Lw           :windows改行形式(CRLF)に変換
    # -Lm           :macintosh改行形式(CR)に変換
    # -g(--guess)   :自動判別の結果を表示
    # --overwrite   :引数のファイルに直接上書き
    # --version     :バージョン情報を表示
