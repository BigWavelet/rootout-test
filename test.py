# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Description :
   Author :       bigwavelet
   date：          2021/12/14
-------------------------------------------------
   Change Activity:
                   2021/12/14:
-------------------------------------------------
"""

import time

import rook


a = 5
e = 6
g = 10


class A:
   a = 1
   b = 2
   
def main():
    while True:
        try:
            now = time.time()
            b = 4
            c = 3
            f = A()
            e = 8
            g = [1,2,3]
            dict_obj = {"a": a, "b": b}
            dict_obj2 = {"f": f}
            time.sleep(2)
            print("time: ", now)

        except KeyboardInterupt as e:
            print("Aborted.")


if __name__ == "__main__":
    rook.start(token='1e554fe5624d46422fb8b8b4260fad3da52a2452a4be54e09128bb5b65005408', labels={"env":"dev"})
    main()
