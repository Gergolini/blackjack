import time

value_cards = {"A":[1,11],
               "K":10,
               "Q":10,
               "J":10}
card_score = {k:-1 for k, v in value_cards.items()} 
num_score1 = {str(i):1 for i in range(2,7)}
num_score2 = {str(i):0 for i in range(7,10)}
card_score.update(num_score1)
card_score.update(num_score2)
card_score["10"] = -1

num_values = {str(i):i for i in range(2,11)}
value_cards.update(num_values)

def timer(func):
    def function_wrapper(*args, **kargs):
        start = time.time()
        func(*args, **kargs)
        end = time.time()
        print("Function {} finished execution in {} millisecs.".format(func.__name__, (end-start)*1000))
    return function_wrapper


