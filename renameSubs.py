import re
import os
subsFile = os.popen('ls *.ssa')
subsList = subsFile.readlines()
subsList= [re.sub("\s$","",name) for name in subsList]
subsList= [re.sub('\s','\\ ',name) for name in subsList]

print subsList
movFile = os.popen('ls *.mkv')
movList = movFile.readlines()
print movList
newName = [re.sub('\n','',name) for name in movList]
newName = [re.sub('mkv','ssa',name) for name in newName]
newName = [re.sub('\s$','',name) for name in newName]
newName = [re.sub('\s','\\ ',name) for name in newName]
print newName
for i in xrange(0,len(newName)):
   print('mv '+re.sub('\n','',subsList[i])+ ' ' + newName[i])
   os.popen('mv '+re.sub('\n','',subsList[i])+ ' ' + newName[i])
