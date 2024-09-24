import streamlit as st
from table import periodic_table as pt
import re

findElements = r"[A-Z][a-z]?\d?"
findMultiplier = r'^\d+'

st.write("Tanish Munjal")
compound = st.text_input("Enter your compound:", "")

def parseCompound(c):
    elements = {}
    c = c.split("*")
    elems = re.findall(findElements, c[0]) #H2
    elemMult = 1 if re.findall(findMultiplier, c[0]) == [] else int(re.findall(findMultiplier, c[0])[0])#7
    
    try:
        hydrates = re.findall(findElements, c[1])
        hydrateMult =  1 if re.findall(findMultiplier, c[1]) == [] else int(re.findall(findMultiplier, c[1])[0])#7
    except:
        hydrateMult = 1
        hydrates = []
    
    for i in elems:
        e = re.split(r"\d", i)[0]
        num = i.replace(e, "")
        if num == '': 
            num=1
        else:
            num = int(num)

        if e in elements:
            elements[e] += num * elemMult
        else:
            elements[e] = num * elemMult
        
    
    for i in hydrates:
        e = re.split(r"\d", i)[0]
        num = i.replace(e, "")
        if num == '': 
            num=1
        else:
            num = int(num)

        if e in elements:
            elements[e] += num * hydrateMult
        else:
            elements[e] = num * hydrateMult
        
    return elements

def calcMm(c):
    elems = parseCompound(c)
    mm = 0
    st.write(elems)
    try:
        for i in elems:
            mm += pt[i] * elems[i]
        return mm
    except:
        st.write("Monkey, not all of them are real elements")
        return "Monkey"

    

if(compound != ""):
    st.write(f"Molar mass = {calcMm(compound)}")
