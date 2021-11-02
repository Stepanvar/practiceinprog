import func_module
from time import time
def py_fib(n):
    if (n <= 1):
        return n
    return py_fib(n-1) + py_fib(n-2)
def py_rsqrt(n):
    n = 1 / (n ** 0.5)
    return n
number1 = int(input("enter number for fib\n"))
print("c_fib")
t = time()
res = func_module.c_fib(number1)
t = time() - t
print("c_result %f, time %f" %(res, t))

print("py_fib")
t = time()
res = py_fib(number1)
t = time() - t
print("py_result %f, time %f" %(res, t))
number2 = int(input("enter number for rsqrt\n"))
print("c_Q_rsqrt")
t = time()
res = func_module.c_Q_rsqrt(number2)
t = time() - t
print("c_result %f, time %f" %(res, t))

print("py_rsqrt")
t = time()
res = py_rsqrt(number2)
t = time() - t
print("py_result %f, time %f" %(res, t))

