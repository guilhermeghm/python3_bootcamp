def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t (a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

@enforce(float, float)
def divide(a,b):
    print(a/b)

repeat_msg("hello", '3')
repeat_msg("hello", 3)
divide(1,2)
divide('1','4')

#What the zip function will do:
#("hello", str) ('3', int)