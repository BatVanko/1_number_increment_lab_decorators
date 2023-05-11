
def number_increment(fun):
    def increase():
        result = [x+1 for x in fun]
        return result

    return increase()

print(number_increment([1, 2, 3]))



