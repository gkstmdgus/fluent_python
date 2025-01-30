def chain(*iterables):
    # before
    # for it in iterables:
    #     for i in it:
    #         yield i

    for it in iterables:
        yield from it

print(list(chain("ABC", range(2))))