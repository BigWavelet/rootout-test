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


def main():
    while True:
        try:
            now = time.time()
            time.sleep(2)
            print("time: ", now)

        except KeyboardInterupt as e:
            print("Aborted.")


if __name__ == "__main__":
    rook.start(token='1e554fe5624d46422fb8b8b4260fad3da52a2452a4be54e09128bb5b65005408', labels={"env":"dev"})
    main()
