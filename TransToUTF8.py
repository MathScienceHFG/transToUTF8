# -*- coding: utf-8 -*-

##
#   @file       TransToUTF8.py
#   @brief      递归搜索指定目录，将所有指定类型的文件，编码为UTF8，保持原名。
#
#   @author     legong.sun@gmail.com
#   @date       2016-05-02
#


import os
import sys
from FileManager import FileManager as fm

__author__ = 'legong.sun@gmail.com'

rootDir = sys.argv[1]
fileType = '.' + sys.argv[2]

codeType = '.utf8'
srcDirList = fm.findFiles(rootDir, fileType)                    # src files:  *.fileType
midDirList = fm.findFiles(rootDir, codeType)                    # tmp files:  *.fileType.codeType

# clean existed mid files
for midDir in midDirList:
    os.system("rm -f {}".format(midDir))
    print "removed", midDir

# trans all src files into dst type, with same names
for srcDir in srcDirList:
    dstDir = srcDir                                             # eg. *.cpp
    midDir = srcDir + codeType                                  # eg. *.cpp.utf8
    os.system("nkf32.exe -w {} > {}".format(srcDir, midDir))    # eg. *cpp > *.cpp.utf8
    os.system("rm -f {}".format(srcDir))                        # eg. rm -f *cpp
    os.system("mv {} {}".format(midDir, dstDir))                # eg. mv *cpp.utf8 *.cpp
    print "finished", srcDir
