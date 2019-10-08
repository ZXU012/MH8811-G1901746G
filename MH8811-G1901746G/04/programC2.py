list = [9, 41, 12, 3, 74, 15]
print(list)
#The minimum function#
def my_min(list):
    smallest_so_far = None
    for number in list :
        if smallest_so_far is None:
            smallest_so_far = number
        elif number < smallest_so_far:
            smallest_so_far = number
    return smallest_so_far
print('Minimum is', my_min(list))
#The maximum function#
def my_max(list):
    largest_so_far = None
    for number in list :
        if largest_so_far is None:
            largest_so_far = number
        elif number > largest_so_far:
            largest_so_far = number
    return largest_so_far
print('Maximum is', my_max(list))
#The average function#
def my_average(list):
    num=0
    sum=0
    for number in list:
        num=num +1
        sum=sum+number
    average = sum / num
    return average
print('Average is', my_average(list))
#The median function#
def my_median(list):
    list.sort()
    num=0
    for number in list:
        num=num+1
    if num % 2 == 1:
        r= int(len(list)/2)
        median = list[r]
    else:
        r=int((len(list)-1)/2)
        median = (list[r]+list[r+1])/2
    return median
print('Median is', my_median(list))
#The range function#
def my_range(list):
    range = my_max(list)- my_min(list)
    return range
print('Range is', my_range(list))