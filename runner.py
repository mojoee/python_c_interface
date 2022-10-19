import ctypes


def addition(a,b):
    result = mylib.addition_c(int(a), int(b))
    return result


libfile = r"D:\Moritz\02_Projects\00_Kiva\12_BinPackingProblem\my_approach\bin_packer\RecursivePartitioningAlgorithm\tinker\python_c_interface\build\lib.win-amd64-cpython-310\simple_addition.pyd"
mylib = ctypes.CDLL(libfile)
addition(10,11)

