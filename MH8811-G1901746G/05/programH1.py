import json
import sys
#define serialize that put 'list' first to easily distinguish in deserialize, item spaced by "|", type of item spaced by";", key and value spaced by":"#
def serialize(x):
    datatype = type(x)
    if datatype is list:
        res="list|"
        for i in x:
            res=res+str(i)+";"+str(type(i))+"|" 
        return res[:-1]
    
    elif datatype is dict:
        res="dict|"
        for i in x:
            res=res+str(i)+":"+str(x[i])+";"+str(type(x[i]))+"|"
        return res[:-1]
#define deserialize that delete "|" ";" ":" first and get it back to the before form#
def deserialize(z):
    lst_of_string=z.split("|")
    datatype=lst_of_string[0]
    lst_of_string=lst_of_string[1:]

    if datatype=='list':
        res=list()
        for m in lst_of_string:
            i=m.split(";")
            v=i[0]
            v_type=i[1]
            if v_type=="<class 'int'>":
                res.append(int(v))
            elif v_type=="<class 'float'>":
                res.append(float(v))
            elif v_type=="<class 'str'>":
                res.append(v)
        return res

    elif datatype == 'dict':
        res = dict()
        for m in lst_of_string:
            m_split=m.split(":")
            key=m_split[0]
            i=m_split[1]

            i=i.split(";")
            v=i[0]
            v_type=i[1]
            if v_type=="<class 'int'>":
                res[key]=int(v)
            elif v_type=="<class 'float'>":
                res[key]=float(v)
            elif v_type=="<class 'str'>":
                res[key]=v
        return res
#define compare to compare whether deserialze can successfully change the serialzed one to the orign#
def compare(a1,a2):
    if a1==a2:
        print('Success')
    else:
        print('Faile')
#open and load the file#    
filename=input('Please enter the file name want to open')
file_open=open(filename)
x=json.load(file_open)
file_open.close()
#serialize the file and then save#
serialize=serialize(x)
filename=input('Please enter the file name want to save')
file_saved=open(filename,'w')
file_saved.write(serialize)
file_saved.close()
#read the saved file and deserialize it#
file_read=open(filename)
z=file_read.read()
file_read.close()
y= deserialize(z)
#compare whether deserialze can successfully change the serialzed one to the orign#
compare(x,y)
