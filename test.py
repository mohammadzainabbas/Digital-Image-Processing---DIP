# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:36:24 2017

@author: GMD
"""


def DefineLabel(left,upper,lftdiag=0,rghtdiag=0):    
    if(left!=0):
        return left
    elif(lftdiag!=0):
        return lftdiag
    elif(upper!=0):
        return upper
    elif(rghtdiag!=0):
        return rghtdiag
    return 0
def ObjectClassification(img,connectivity=4):
    import numpy as n
    size=n.shape(img)
    named=n.zeros(size,dtype=n.int)
    
    list_objects=[]
    newlabel=1
    
    for i in range(1,size[0]):
        for j in range(1,size[1]):
            if (img[i,j]==255):
                thislabel=0
                if(connectivity==8):
                    thislabel=DefineLabel(named[i,j-1],named[i-1,j],named[i-1,j-1],named[i-1,j+1])
                else:
                    thislabel=DefineLabel(left=named[i,j-1],upper=named[i-1,j])
                if(thislabel==0):
                    thislabel=newlabel
                    list_objects.append([thislabel])
                    newlabel=newlabel+1
                named[i,j]=thislabel
                populateList(thislabel,named[i-1,j],named[i,j-1],list_objects)
    sortLList(list_objects)
    return (named,list_objects)

def populateList(LBL_curr,LBL_left,LBL_upper,list_objects):
    if(LBL_upper!=0 and LBL_left!=0 and LBL_upper!=LBL_left):
        upperindex=findindex(list_objects,LBL_upper)
        leftindex=findindex(list_objects,LBL_left)
        if(upperindex!=leftindex):
            listinlistcopy(list_objects,upperindex,leftindex)
    
     
def listinlistcopy(lista,dstloc,srcloc):
    while(lista[srcloc].__len__()>0):
        lista[dstloc].append(lista[srcloc].pop())
    lista.__delitem__(srcloc)
    
def findindex(lista,value):
    r=-1
    for k in range(lista.__len__()):
        if(lista[k].count(value)>0):
            r=k
            break
    return r
def sortLList(llists):
    for k in range(1,llists.__len__()):
        llists[k].sort()

def AssignMinLabel(labeledimg,list_objects):
    import numpy as n
    size=n.shape(labeledimg)
    newimg=n.zeros((size),dtype=n.uint8)
    for i in range(0,size[0]):
        for j in range(0,size[1]):
            if(labeledimg[i,j]!=0):
                newimg[i,j]=(findindex(list_objects,labeledimg[i,j])+1)*40
    return newimg

def LabelDetectSegment(img,connectivity=8):
    n1,l1=ObjectClassification(img,connectivity)
    res=AssignMinLabel(n1,l1)
    return res,l1
    
import cv2 as c
img=c.imread('cc.png',0)
c.imshow('img',img)
c.waitKey(0)
img_objects,l1=LabelDetectSegment(img,connectivity=8)
c.imshow('img',img_objects)
c.waitKey(0)
c.destroyAllWindows()
print(len(l1))