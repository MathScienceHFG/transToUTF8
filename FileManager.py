# -*- coding: utf-8 -*-

##
#   @file       FileManager.py
#   @brief      some I/O operator for folder and path
#
#   @author     legong.sun@gmail.com
#   @date       2016-05-02
#


import os
import cPickle as pk

import sys


class FileManager:

    """
    some I/O operator for folder and path
    """

    @staticmethod
    def __addEndSlash(srcDir):
        dstDir = srcDir
        if sys.platform == "darwin":
            slashType = '/'
        else:
            slashType = '\\'
        if dstDir[-1] is not slashType:
            dstDir += slashType
        return dstDir

    @staticmethod
    def __changeSlashType(srcDir):
        if sys.platform == 'darwin':
            dstDir = srcDir.replace('\\', '/')
        else:
            dstDir = srcDir.replace('/', '\\')
        return dstDir

    @staticmethod
    def dump(data, path):
        pk.dump(data, open(path, "wb"))

    @staticmethod
    def load(path):
        return pk.load(open(path, "rb"))

    @staticmethod
    def findFiles(dirSrc, fType):
        fileList = []

        def reFind(dirSrc, fType):
            dirSrc = FileManager.addDirEndSlash(dirSrc)
            if os.path.isdir(dirSrc) == False:
                return []
            for s in os.listdir(dirSrc):
                newDir = os.path.join(dirSrc, s)

                # print os.path.splitext(newDir)[1]

                if newDir and (os.path.splitext(newDir)[1] == fType):
                    fileList.append(newDir)
                elif os.path.isdir(newDir):
                    reFind(newDir, fType)
            return fileList

        return reFind(dirSrc, fType)


    @staticmethod
    def addDirEndSlash(srcDir):
        newDir = FileManager.__changeSlashType(srcDir)
        newDir = FileManager.__addEndSlash(newDir)
        return newDir

    @staticmethod
    def makeFolder(dstDir, overwrite=False):
        dstDir = FileManager.addDirEndSlash(dstDir)
        if os.path.isdir(dstDir) is False:
            os.system(str.format("mkdir {0}", dstDir))

        elif os.path.isdir(dstDir) and overwrite is True:
            os.system(str.format("rm -rf {0}", dstDir))
            os.system(str.format("mkdir {0}", dstDir))
