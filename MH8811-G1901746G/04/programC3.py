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
#The minimum function#
def my_min(fname):
    smallest_so_far = None
    for number in fname :
        if smallest_so_far is None:
            smallest_so_far = number
        elif number < smallest_so_far:
            smallest_so_far = number
    return smallest_so_far
print('Minimum is', my_min(fname))
#The maximum function#
def my_max(fname):
    largest_so_far = None
    for number in fname :
        if largest_so_far is None:
            largest_so_far = number
        elif number > largest_so_far:
            largest_so_far = number
    return largest_so_far
print('Maximum is', my_max(fname))
#The average function#
def my_average(fname):
    num=0
    sum=0
    for number in fname :
        num=num +1
        sum=sum+number
    average = sum / num
    return average
print('Average is', my_average(fname))
#The median function#
def my_median(fname):
    fname.sort()
    num=0
    for number in fname:
        num=num+1
    if num % 2 == 1:
        r= int(len(fname)/2)
        median = fname[r]
    else:
        r=int((len(fname)-1)/2)
        median = (fname[r]+fname[r+1])/2
    return median
print('Median is', my_median(fname))
#The range function#
def my_range(fname):
    range = my_max(fname)- my_min(fname)
    return range
print('Range is', my_range(fname))