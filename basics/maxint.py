def maxint(a):
    max = a[0]
    for i in a:
        if i > max:
             max = i
    return max

if __name__ == '__main__':
    a = [10,0,-2,100,200,200,-200,2000]
    print(maxint(a))
