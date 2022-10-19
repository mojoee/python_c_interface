import ctypes


def addition(a,b):
    result = mylib.addition(int(a), int(b))
    return result


libfile = r"build\lib.win-amd64-3.7\decision_tree.pyd"
mylib = ctypes.CDLL(libfile)
addition(4,5)

