import xml.etree.ElementTree as ET
# Element type is a flexible container object, designed to store hierarchical
# data structures in memory. 
# It supports X Path expression language to locate elements in tree  
import sys # 
import os #  use to interact with os, make folder, file name access etc
import glob # glob module finds all the pathnames matching


full_path = '/home/belayat/LST_detector/Annotations/*.xml' # local path
#docker_path = '/root/keras-yolo3/train_tools_label/*.xml'  # docker path 

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


    order = i.split(".xml")[0]  # '1+2+3'.split('+')[0] >> 1; '1+2+3'.split('+') >>['1', '2', '3']; 
    #print('xml file path: {}'.format(order)+ "\n")
    #print(order)    
    #order = order.split("/")[6].split("_")[2]
    #print(order)


    #img_path = root.find('path').text #Obtain image filename
    #print(img_path)
    
    img_basepath = '/root/keras-yolo3/train_m2c/'
    img_name = root.find('filename').text #Obtain image filename
    img_path = img_basepath + img_name 
    #img_path = img_path.replace(r'','/root/keras-yolo3/train_m2c/')
    print(img_path)
    #img_path = img_path.split("\\")[0]
    
    
    #img_path = img_path.replace("\\","")
    #print(img_path)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        #print(cls)
        txt = open('/home/belayat/LST_detector/Annotations/LST_classes.txt')
        #txt = open('/root/keras-yolo3/model_data/classes.txt')
        line = txt.readlines()

        for i,x in enumerate(line):
            #print(i,x.strip('\n'))
            if x.strip('\n') == cls:
               class_label = i
               #print(i)
        
	#img_path = img_path 

	     
        #img_path = img_path + "toolOutsideofSurgery_" + order

        xmlbox = obj.find('bndbox')
        b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),int(xmlbox.find('xmax').text),int(xmlbox.find('ymax').text)]
        train.append([img_path]+b+[class_label])

    with open('./Annotations/train_m2c.txt','w') as f:
        for i in train:
            #print(i)
            #f.write(str(i).strip('[').strip(']').replace(',',' ').replace("'",""))
            f.write(str(i).strip('[').strip(']').replace("'","").replace(" ","").replace(","," ",1))
            f.write('\n')  	                                     
