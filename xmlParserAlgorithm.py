# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:59:01 2021

@author: EBB
"""




class Attribute:
    
    val = []
    def __init__(self , key , val):
        
    
        self.val.append(key)
        self.val.append(val)

    def getAttribute(self):
        return self.val


class Element:
    
    children = []
    attributes = []
    innerText =""
    parent = ""
    tag = ""
    
    def __init__(self , tag):
        self.tag = tag
    
    
    def setInnerText(self , text):
        self.innerText = text
        
    def addAttributes(self , attr):
        self.attributes.append(attr)
    
    def addChildren(self , child):
        self.attributes.append(child)
    
    def getElementTag(self):
        return self.tag
        


class XmlTree:
    Root = ""
    Elements = []
    RootTag = ""
    RootAttribute = []
    RootInnerHtml = ""
    
    def __init__ (self ):
        pass
    
    def addElement(self ,el):
        self.Elements.append(el)
    
    def appendElement(self , e):
        self.EleElements.append(e)
        
    def getElements(self):
        return self.Elements
    

def clear(str_list):
    while '' in str_list:
        str_list.remove('')

f = open("read.xml","r")

lines = f.read().strip().replace("\n","").replace("\t","")
lines = lines.strip()
f.close()
count = 0
f2 = open("writeFile.txt","a")
f2.write(lines)
f2.close()
tree = XmlTree()
arr = lines.split("<")
xmlParserStack = []

for i in arr :
    global e
    i = i.strip()
    try:
        if i[-1] == ">" and i[0] != "/": # saf eelement tanımı 
            
            getElemenent = 0
            currentCursor = 0
            elemName = True
           
            for j in i : 
                if j != " ":
                    currentCursor +=1
                if j == " " and elemName :
                    e = Element(i[getElemenent : currentCursor])
                    xmlParserStack.append(e)
                    tree.addElement(e)
                    elemName = False
                    break
          
            i = (i[currentCursor:len(i)-1]).strip()
            tempArr = i.split("=")
          
            
            
            if len(tempArr) == 2 :

                tempAttribute = Attribute(tempArr[0],tempArr[1].replace("\"","").replace("'",""))
                tree.getElements()[-1].addAttributes(tempAttribute)
     
            elif len(tempArr) > 2:
                cleanVersion = []
                for m in range(len(tempArr)):
                    if m == 0 or m == len(tempArr)-1:
                        pass
                    else:
                        abe = (tempArr[m].split("\""))
                        clear(abe)
                        
                        cleanVersion.append(tempArr[0])
                        for d in abe:
                            cleanVersion.append(d)
                        cleanVersion.append(tempArr[-1])
                rlenght = len(cleanVersion)-1
               
                for q in range(rlenght):
                    tempAttribute = Attribute(cleanVersion[q],cleanVersion[q+1].replace("\"","").replace("'",""))
                    tree.getElements()[-1].addAttributes(tempAttribute)
                       # print(cleanVersion)

            #print(i ," bu element tanımınıdır ")
        elif i[-1] == ">" and i[0] == "/": # element kapanması olduğu garanti
            i = i.replace("/","").replace(">","")
           # print(" i : " , i ,"  LastElement : " ,  xmlParserStack[-1].getElementTag())
            
            if xmlParserStack[-1].getElementTag() == i :
                xmlParserStack.remove(i)
            else:
                print("Hatalı Veri")
            
            
        elif i[-1] != ">": # içinde inner html var ve yeni bir element
            tempA = i.split(">")
            if len(tempA) ==1:
                e = Element(tempA[0].replace(">",""))
                xmlParserStack.append(e)
                tree.addElement(e)
                # inner htmli boş
            else:
                pass
  
            #pass
    except Exception as e:
       
        print("i except : " , e)
    #print(i)
