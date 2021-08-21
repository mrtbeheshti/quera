from functions import f, g, h
from threading import Thread


def solve():
    tf = []
    tg = []
    th = []
    for i in range(4):
        tf.append(Thread(name=str(i + 1), target=f[i]))
        tf[i].start()
    for i in range(2):
        tf[2 * i].join()
        tf[2 * i + 1].join()
        tg.append(Thread(name=str(i + 1), target=g[i]))
        tg[i].start()
    tg[0].join()
    tg[1].join()
    th.append(Thread(name="1", target=h[0]))
    th[0].start()
