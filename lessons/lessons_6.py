def log_action(func):
    def wrapper(*args, **kwargs):
        print("Начало операции")
        result = func(*args, **kwargs)
        print("Конец операции")
        return result
    return wrapper

def make_order(x):
    print("Заказ создан", x)
    return 100

def do_something():
    print("order function")
    return "OK"
# print(make_order)
make_order = log_action(make_order)
print(make_order)
order = make_order(12345)
print(order)
do_something = log_action(do_something)
res = do_something()
print(res)

# make_order()