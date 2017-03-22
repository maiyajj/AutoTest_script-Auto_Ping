# coding=utf-8
import os
# import typing
# from multiprocessing import Process


class Main:
    def ping(self):
        command = "ping  192.168.2.157 -i 3 -l 256 -w 1000 "
        os.system(command)

if __name__ == '__main__':
    Main().ping()
