# -*- coding: UTF-8 -*-
from meituan import Meituan

if __name__ == '__main__':
    a = """

███╗   ███╗███████╗██╗     ████████╗██╗   ██╗ █████╗ ███╗   ██╗
████╗ ████║██╔════╝██║     ╚══██╔══╝██║   ██║██╔══██╗████╗  ██║
██╔████╔██║█████╗  ██║        ██║   ██║   ██║███████║██╔██╗ ██║
██║╚██╔╝██║██╔══╝  ██║        ██║   ██║   ██║██╔══██║██║╚██╗██║
██║ ╚═╝ ██║███████╗██║███████╗██║   ╚██████╔╝██║  ██║██║ ╚████║
╚═╝     ╚═╝╚══════╝╚═╝╚══════╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
"""
    print(a)

    meituan = Meituan()
    meituan.coupons()


