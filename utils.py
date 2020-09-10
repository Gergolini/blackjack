import time

def timer(func):
    def function_wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        end = time.time()
        print("Function {} finished execution in {} millisecs.".format(func.__name__, (end-start)*1000))
    return function_wrapper
