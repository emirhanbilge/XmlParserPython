# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:59:01 2021

@author: EBB
"""


class Attribute:

    def __init__(self , key , val):
        self.val = []
        self.val.append(key)
        self.val.append(val)
    def getAttribute(self):
        return self.val


class Element:
    tag = ""
    innerText =""
    parent = ""
    def __init__(self , tag):
        self.children = []
        self.attributes = []
        self.tag = tag
        
        
    
    
    def setInnerText(self , text):
        self.innerText = text
        
    def addAttributes(self , attr):
        self.attributes.append(attr)
    
    def addChildren(self , child):
        self.attributes.append(child)
    
    def getElementTag(self):
        return self.tag
    
    def getAttributes(self):
        att = ""
        for i in self.attributes:
            att += "name : " + i.val[0] +" value : " + i.val[1] +" \n"
        return att
        


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
    


class XmlParser():



    def __init__(self):
        self.lines = []
        self.xmlParserStack = []
        self.XmlTreeObject = XmlTree()

    def loadParser(self , file ):

        try:
            f = open(file,"r")
        except:
            print("File not found !!!")
            return 
        lines = f.read().strip().replace("\n","").replace("\t","")
    
        self.lines = lines.split("<")
        f.close()
        self.creator()
        return self.XmlTreeObject

   
    def clear(self , str_list):
        while '' in str_list:
            str_list.remove('')
        return str_list
    
    def pureElement(self , line):

        getElemenent = 0
        currentCursor = 0
        elemName = True
           
        for j in line : 
            if j != " ":
                currentCursor +=1
            if j == " " and elemName :
                e = Element(line[getElemenent : currentCursor])
                self.xmlParserStack.append(e)
                self.XmlTreeObject.addElement(e)
                elemName = False
                break
       
        i = (line[currentCursor:len(line)-1]).strip()
        tempArr = i.split("=")
          
        if len(tempArr) == 2 :

            tempAttribute = Attribute(tempArr[0],tempArr[1].replace("\"","").replace("'",""))
            self.XmlTreeObject.getElements()[-1].addAttributes(tempAttribute)
     
        elif len(tempArr) > 2:
            cleanVersion = []
            for m in range(len(tempArr)):
                if m == 0 or m == len(tempArr)-1:
                    pass
                else:
                    abe = (tempArr[m].split("\""))
                    abe = self.clear(abe)
                        
                    cleanVersion.append(tempArr[0])
                    for d in abe:
                        cleanVersion.append(d)
                    cleanVersion.append(tempArr[-1])
            rlenght = len(cleanVersion)-1
               
            for q in range(rlenght):
                tempAttribute = Attribute(cleanVersion[q],cleanVersion[q+1].replace("\"","").replace("'",""))
                self.XmlTreeObject.getElements()[-1].addAttributes(tempAttribute)

    def endofElement(self , line):
        line = line.replace("/","").replace(">","")
        # print(" i : " , i ,"  LastElement : " ,  xmlParserStack[-1].getElementTag())
        
        try:    
            print(self.xmlParserStack[-1].getElementTag().strip() ,"  *** " , line)
            if self.xmlParserStack[-1].getElementTag().strip() == line.strip() :
                self.xmlParserStack.pop()
            else:
                print("Hatalı Veri")
        except Exception as e:
            if len(self.xmlParserStack)==0 :
                print("başarılı")
            else:
                print("Tag kapanmasında sorun var" , e )
                return 
       
    def textElement(self,line):
        tempA = line.split(">")
        
        if len(tempA[0].split(" ")) == 1:
            elem = Element(tempA[0])
            self.xmlParserStack.append(elem)
            self.XmlTreeObject.addElement(elem)
        else:
            self.pureElement(tempA[0])
            self.XmlTreeObject.getElements()[-1].setInnerText(tempA[1])

        

    def xmlChecker(self):
        pass

    def creator(self):

        for i in self.lines:
            i = i.strip()
            try:
                if i[-1] == ">" and i[0] != "/":
                    self.pureElement(i)

                elif i[-1] == ">" and i[0] == "/": # element kapanması olduğu garanti
                    self.endofElement(i)
                elif i[-1] != ">": # içinde inner html var ve yeni bir element
                    self.textElement(i)
                else:
                    i = i.replace(">")
                    self.XmlTreeObject.Root = i
                    
            except Exception as e:
                print(e)


parser = XmlParser()

tree = parser.loadParser("read.xml")

"""
for i in tree.getElements():
    
    print("Element : " , i.tag ," \n" , i.getAttributes())
"""