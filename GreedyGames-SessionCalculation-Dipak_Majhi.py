from datetime import *

text_file = open("data.dat", "r")   
mylist = text_file.read().split('\n')
row = len(mylist)
mylist = [mylis.replace('\xad','-') for mylis in mylist]
print mylist
print "\n"
ses = 1
tses = 1
formatt = '%Y-%m-%d %H:%M:%S.%f'
j=1
temp=1

dif = datetime.strptime(mylist[1], formatt) - datetime.strptime(mylist[0],formatt)
myarr = dif
tvsestime = datetime.strptime(mylist[0], formatt) - datetime.strptime(mylist[0], formatt)

for i in range(3,row,2):
    
    diff = datetime.strptime(mylist[i-1], formatt) - datetime.strptime(mylist[i-2], formatt)    
    dif = datetime.strptime(mylist[i], formatt) - datetime.strptime(mylist[i-1], formatt) 
    
    if diff < timedelta(seconds = 30): 
        myarr +=dif
        
        
    if diff > timedelta(seconds = 29): 
        if(temp==1):
            print "Session time "+str(j)+" : {}".format(myarr)
            j+=1
            tvsestime += myarr
            
        if dif>timedelta(seconds = 60): 
            ses+=1
            myarr = dif
            temp=1
            
        if dif<timedelta(seconds = 60):
            temp=0
        
        tses+=1
        
    if ((i == row-1) and dif>timedelta(seconds = 60)):
        tvsestime += myarr
        print "Session time "+str(j)+" : {}".format(myarr)
        j+=1
        print "\nTotal Session time : {}".format(tvsestime)
        
print "\nAverage Session time : {}".format(tvsestime/ses)
print "\nTotal Number of sessions = {}".format(tses)
print "\nNumber of valid sessions = {}".format(ses)

text_file.close()
