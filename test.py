def minus(Int1, Int2):
    res = int(Int1) - int(Int2)
    #print(res)
    return res

def plus(Int1, Int2):
    print(Int1, Int2)
    res = int(Int1) + int(Int2)
    #print(res)
    return res

def test1():
    a = ["prnt"]
    b = ["+", '-']
    line = "prnt 10 + 5 - 2".split(" ")
    print(line)
    for obj in line:
        print(obj)
        if obj in a:
            pass
        if obj in b:
            print(obj)
            if obj == "+":
                res = plus(line[line.index(obj)-1], line[line.index(obj)+1])
                line.remove(line[line.index(obj)+1])
                line.remove(line[line.index(obj)-1])
                line[line.index(obj)] = res
            if obj == "-":
                res = minus(line[line.index(obj)-1], line[line.index(obj)+1])
                line.remove(line[line.index(obj)+1])
                line.remove(line[line.index(obj)-1])
                line[line.index(obj)] = res

    print(line)
    pass




if __name__ == "__main__":
    test1()
    pass
