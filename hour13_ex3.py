from random import random


def count():
    cnt=0
    for i in range(10):
        if i>0 or i<1:
            cnt = cnt+1
            print(random())
    print(cnt)

count()


if __name__ == "__main__":
    main()