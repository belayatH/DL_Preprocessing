import xml.etree.ElementTree as ET
# Element type is a flexible container object, designed to store hierarchical
# data structures in memory. 
# It supports X Path expression language to locate elements in tree  
import sys # 
import os #  use to interact with os, make folder, file name access etc
import glob # glob module finds all the pathnames matching


full_path = '/home/dataset/images/*.xml' # local path
#docker_path = '/root/keras-yolo3/train_tools_label/*.xml'  # docker path 
class_file = '/home/datast/LST_classes.txt'
train_file = '/home/dataset/images/train_m2c.txt'


all_files = glob.glob(full_path)
#print(all_files)


train = []
class_label = 0

for i in all_files:
    FILE = i
    # print(i)

    # # Import xml file from disk 
    file = open(FILE)
    tree = ET.parse(file) # pass file; tree = ET.parse('country_data.xml')
    root = tree.getroot() # Returns the root element for this tree 


    order = i.split(".xml")[0]  
    
    img_basepath = '/root/keras-yolo3/train_m2c/'
    img_name = root.find('filename').text # Obtain image filename
    img_path = img_basepath + img_name 
    print(img_path)


    for obj in root.iter('object'):
        cls = obj.find('name').text
        #print(cls)
        txt = open(class_file)

        line = txt.readlines()

        for i,x in enumerate(line):
            #print(i,x.strip('\n'))
            if x.strip('\n') == cls:
               class_label = i

	xmlbox = obj.find('bndbox')
        b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),int(xmlbox.find('xmax').text),int(xmlbox.find('ymax').text)]
        train.append([img_path]+b+[class_label])

    with open(train_file,'w') as f:
        for i in train:
            f.write(str(i).strip('[').strip(']').replace("'","").replace(" ","").replace(","," ",1))
            f.write('\n')  
if __name__ == '__main__':
	
	
