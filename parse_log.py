import os 
import csv
import shutil
# open and store the csv file

id = list()
with open('log','r') as csvfile:
    timeReader = csv.reader(csvfile, delimiter = ',')
    # build dictionary with associated IDs
    for row in timeReader:
        try:
            pwd = row[0].split('Found no face.')[1]
            file_name = row[0].split('Found no face.')[1].split('/')[-1]
            file_dir = row[0].split('Found no face.')[1].split('/')[-2]
            if file_dir not in id:
                id.append(file_dir)
                #shutil.copytree('/home/infor/InsightFace_Pytorch/data/faces_emore/imgs/'+file_dir,'/home/infor/InsightFace_Pytorch/data/faces_emore/imgs_p/'+file_dir)
                #shutil.rmtree('/home/infor/InsightFace_Pytorch/data/faces_emore/imgs_/'+file_dir)
            print(len(id))
            #print(file_dir)
            #print(file_name)
        except Exception as E:
            print(pwd)
            print('Handle::',E)



