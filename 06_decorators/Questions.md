1.  Timing Function Execution
    Problem: Write a decorator that measures the time a function takes to execute.

    Ans. def timer(func):
    def wraper(*args, \*\*kargs):
    start = time.time()
    result = func(*args, \*\*kargs)
    end = time.time()
    print(f"{func.**name**} run in {end - start} time")
    return result
    return wraper

    @timer
    def example_function(n):
    time.sleep(n)

    example_function(2)

2.  Debugging Function Calls
    Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

    def debug(func):
    def wraper(*args, \*\*kwargs):
    args_value = ", ".join(str(arg) for arg in args)
    kwargs_value = ", ".join(f"{k} {v}" for k, v in kwargs.items())
    print(f"calling: {func.**name**} with args {args_value} and kwargs {kwargs_value}")
    return func(*args, \*\*kwargs)

    return wraper

    @debug
    def hello():
    print("hello")

    @debug
    def greet(name, greeting = "hello"):
    print(f"{greeting} {name}")

    greet("kamal", "mr.")
    hello()

3.  Cache Return Values
    Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
