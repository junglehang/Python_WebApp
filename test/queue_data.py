import multiprocessing
import time

def add_data(queue):
	for i in range(3):
		queue.put(i)


def read_data(queue):
	while True:
		#判断条件来跳出循环(队列里面没有数据了)
		#判断队列为空
		if queue.empty():
			break
		value = queue.get()
		print(value)

if __name__ == '__main__':
#默认队列可以放入多个数据
	queue = multiprocessing.Queue(3)
	#创建子进程执行任务
	add_process = multiprocessing.Process(target=add_data,args=(queue,))
	read_process =multiprocessing.Process(target=read_data,args=(queue,))
	add_process.start()
	read_process.start()

	#进程用的不多一个应用程序一个进程
	#多任务的时候可以使用线程也可以使用进程
	#从资源的角度来说,线程更节省资源
	#从代码稳定的角度来说:多进程要比多线程稳定的多
