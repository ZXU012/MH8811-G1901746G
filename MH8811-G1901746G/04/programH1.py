def getFileLines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            lines.append(line)
    fhandle.close()
    return lines
fname = 'xuzhicheng.csv'
fname = getFileLines(fname)
fname = list(map(float,fname))
def my_average(fname):
    num=0
    sum=0
    for number in fname :
        num=num +1
        sum=sum+number
    average = sum / num
    return average
def my_variance(fname):
    difference_square=0
    for number in fname:
        difference_square=difference_square+((number-my_average(fname))**2)/(len(fname)-1)
    return  difference_square
print('Variance is', my_variance(fname))
