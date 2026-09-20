def func_args(*args):
    print(args)
    print("Number of arguments:", len(args))
    print("The second argument:", args[1] if len(args) > 1 else None)
    pass

def func_kwargs(**kwargs):
    print(kwargs)
    print("Number of keyword arguments:", len(kwargs))
    print("The value of 'a':", kwargs.get('a'))
    pass

func_args(1, 2, 3)
func_kwargs(a=111, b=222, c="ccc", d="ddd")