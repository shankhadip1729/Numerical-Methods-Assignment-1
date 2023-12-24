import Fibonacci
import time
init = time.time()
x = Fibonacci.firstnfib(100)
print(x)
final = time.time()
t = final - init
print(t)