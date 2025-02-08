#fib.py

from functools import lru_cache
import time
import matplotlib.pyplot as plt

def timer(func):
  def wrapper(n):
    start = time.time()
    result = func(n)
    end = time.time()
    execution_time = end - start
    print(f"Finished in {execution_time:.8f}s: f({n}) -> {result}")
    return result
  return wrapper

@lru_cache()
@timer
def fib(n: int) -> int:
  if n < 2:
    return n
  return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
  x = []
  y = []

  for n in range (0, 101):
    start = time.time()
    fib_num = fib(n)
    end = time.time()
    execution_time = end - start

    x.append(n)
    y.append(execution_time)


plt.plot(x,y)
plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.grid(True)
plt.show()