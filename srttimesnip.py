import re 
import datetime
import time
import os
from collections import OrderedDict
from gensim.summarization.summarizer import summarize


def convert_time(timestring):
    
    nums = list(map(float, re.findall(r'\d+', timestring)))
    return 3600*nums[0] + 60*nums[1] + nums[2] + nums[3]/1000


substring = 'he.srt' #name of the srt file reference

for root, subdirs, files in os.walk('C:/Users/LTS WinPro/Desktop'): #Your filepath
    for filename in files:
        if substring in filename:
            f = open(os.path.join(root,filename))
            lines = f.readlines()


times_texts = []
current_times , current_text = None, ""
for line in lines:
    times = re.findall("[0-9]*:[0-9]*:[0-9]*,[0-9]*", line)
    if times != []:
        current_times = list(map(convert_time, times))
    elif line == '\n':
        times_texts.append((current_times, current_text))
        current_times, current_text = None, ""
    elif current_times is not None:
        current_text = current_text + line.replace("\n"," ")

#print (times_texts)
#for key,value in times_texts: 
    #print(key,value)

res = []

counter = int(input("how many inputs?"))


def geninp(inp_time, out_time):
    for i in range(counter):
        inp_time = float(inp_time)
        out_time = float(out_time)
        #inp_time = float(input("enter start time in seconds: "))
        #out_time = float(input("enter end time in seoconds: "))
        for key,value in times_texts:
            if ((key[0] > inp_time) and (key[1] < out_time)):
                #print(value)
                temp = [key,value]
                res.append(temp)
                #res.append(key,value)
    return res

#print(res)        
s=""
for key, value in res: 
    #print(value)
    sst = s.join(value)
    #print(sst)
    sum+=sst

#print(sum)
print(summarize(sum, ratio=0.2))



        


