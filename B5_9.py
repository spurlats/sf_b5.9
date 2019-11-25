import time

NUM_RUNS = 1000

class time_see:
	def __init__(self, func, num_runs = 100):
		self.start = 0
		self.num_runs = num_runs
		self.func = func
	def __enter__(self):
		self.start = time.time()
		return self
	def __exit__ (self, *args, **kwargs):
		avg_time = (time.time() - self.start) / self.num_runs
		print("Среднее время выполнения, мкс = %.5f" % (avg_time * 1_000_000))


def fib(first_num, second_num):
    result = 0
    last_res = []
    last_res.append(second_num)
    while result < 40000000000000:
        result = first_num + second_num
        first_num = second_num
        second_num = result
        if result % 2==0:
            last_res.append(result)
    return(sum(last_res))


with time_see(fib, NUM_RUNS) as ts:
	for i in range(NUM_RUNS):
		fib(1,2)