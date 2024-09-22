import streamlit as st
from table import periodic_table as pt
import re

findElements = r"[A-Z][a-z]?\d*"
findMultiplier = r'^\d+'

st.write("Tanish Munjal")
compound = st.text_input("Enter your compound:", "")

def parseCompound(c):
    elements = {}
    c = c.split("*")
    # st.write(c)
    elems = re.findall(findElements, c[0]) #H2
    elemMult = int(re.findall(findMultiplier, c[0])[0]) #7
    hydrateMult = int(re.findall(findMultiplier, c[1])[0]) #7
    hydrates = re.findall(findElements, c[1])
    
    for i in elems:
        e = re.split(r"\d", i)[0]
        num = i.replace(e, "")
        if num == '': 
            num=1
        else:
            num = int(num)

        elements[e] = num * elemMult
    
    for i in hydrates:
        e = re.split(r"\d", i)[0]
        num = i.replace(e, "")
        if num == '': 
            num=1
        else:
            num = int(num)

        elements[e] = num * hydrateMult
    
    return elements
 
def calcMm(c):
    elems = parseCompound(c)
    mm = 0
    for i in elems:
        mm += pt[i] * elems[i]
    return mm
        


if(compound != ""):
    st.write(f"Molar mass = {calcMm(compound)}")
