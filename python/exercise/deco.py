

# @decorate
# def target():
#     print('running target()')


# def target():
#     print('running target()')


# target = decorate(target)


def deco(func):
    def inner():
        print("running inner()")
    
    return inner


@deco
def target():
    print("running target()")

target
target()

