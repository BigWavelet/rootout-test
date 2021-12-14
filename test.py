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

def main():
    while True:
        try:
            now = time.time()
            time.sleep(2)
            print("time: ", now)

        except KeyboardInterupt as e:
            print("Aborted.")


if __name__ == "__main__":
    main()
