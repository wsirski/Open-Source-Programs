#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:21:44 2023

@author: williamsirski
"""

print("Trailer Fill Calculator")


print("What is the pallet width, in inches?")
pw=float(input())
print("What is the pallet length, in inches?")
pl=float(input())
print("What is the part diameter, in inches?")
pd=float(input())
print("What is the part height, in inches?")
ph=float(input())
print("What is the part stack height, in inches?")
psh=float(input())
print("What is the padding thickness, in inches?")
pad=float(input())
print("What is the part weight, in pounds?")
pweight=float(input())
carboarddensity=43 

width=pw-2*pad
length=pl-2*pad

rows1=round(53*12/pw)
rows2=round(53*12/pl)
columns1=round(101/pl)
columns2=round(101/pw)
n1=rows1*columns1
n2=rows2*columns2

if n1 > n2:
    print("Number of Rows of Pallets: "+str(rows1))    
    print("Number of Columns of Pallets: "+str(columns1))
    npallets=n1
else:
    print("Number of Rows of Pallets: "+str(rows2))    
    print("Number of Columns of Pallets: "+str(columns2))
    npallets=n2

r1=round(width/pd)
r2=round(length/pd)
c1=round(length/(pd+3**0.5/2*pd))
if c1 != 1:
    lengthadd=length-pd
    c1add=round(length/(3**0.5/2*pd))
    c1=c1add+1
c2=round(width/(pd+3**0.5/2*pd))
if c2 != 1:
    widthadd=width-pd
    c2add=round(width/(3**0.5/2*pd))
    c2=c2add+1
nlevel1=c1*r1-int(c1/2)
nlevel2=c2*r2-int(c2/2)
if nlevel1 > nlevel2:
    print("Parts per level: "+str(nlevel1))
    nlevel=nlevel1
else:
    print("Parts per level: "+str(nlevel2))
    nlevel=nlevel2
levels=round((110-4.5-2*pad-ph)/psh)
npallet=levels*nlevel
print("Parts per Pallet: "+str(npallet))
ntruck=npallet*npallets
print("Parts per Truck: "+str(ntruck))
weight=pweight*ntruck+npallets*36+npallets*pad/12*43/144*(2*width*length+2*width*105.5+2*length*105.5)
print("Weight in Trailer: "+str(weight))