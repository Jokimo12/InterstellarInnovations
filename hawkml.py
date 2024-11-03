import pandas as pd
import xml.etree.ElementTree as ET
from googletrans import Translator
import xml.etree.ElementTree as ETree
import pandas as pd
import csv

#csv to xml
df= pd.read_csv('LLM_DF.csv')
with open('outputf.xml', 'w') as myfile: 
  myfile.write(df.to_xml())


tree = ET.parse('outputf.xml')
for elem in tree.iter():
    #print(elem.tag, elem.text)
    if(elem.text):
      translator=Translator()
      translation=translator.translate(elem.text,dest="fr").text
      #elem.text.replace(elem.text,translation)
      elem.text=translation
      #print(elem.text)
tree.write('outputfr.xml', xml_declaration=True, method='xml', encoding="utf8")


xmlp = ETree.XMLParser(encoding="utf-8")
Tree = ETree.parse('outputf.xml',parser=xmlp)
#Hit and trial methods
#xml='/content/output.xml'
#xmltest = ET.fromstring(xml.encode("utf-8"))
#Tree = ETree.parse(xmltest)
#Tree = ETree.parse('/content/outputfr.xml')

root = Tree.getroot()
A=[]
for ele in root:
  B = {}
  for i in list(ele):
    B.update({i.tag: i.text})
    A.append(B)
df = pd.DataFrame(A)
df.drop_duplicates(keep='first', inplace=True)
df.reset_index(drop=True, inplace=True)
writer = csv.writer(open('600.csv', 'w'))
df.to_csv('600.csv')

print("XML FILE CONVERTED SUCESSFULLY")