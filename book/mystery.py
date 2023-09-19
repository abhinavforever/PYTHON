def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)
def change(arg: list):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)
