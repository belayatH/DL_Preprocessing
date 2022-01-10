import shutil
import os
from csv import reader


def csv2list(csv_fname):
    ''' Store all rows to a list'''
    csv_lines = []
    with open(csv_fname, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        if header != None:  # skip header
            for row in csv_reader:
                csv_lines.append(row)
    return csv_lines

# def writeTXT(txt, fdir, fname):
#     '''Open a txt file and write / append new labels'''
#     fpath = os.path.join(fdir, fname)
#     print('txt   wr', txt)
#     f = open(fpath, "w")
#     f.write(txt)
#     f.close()

def csvRow2txtline(fdir, line):
    ''' convert format: csv row into a line for text file'''
    print( 'Processing:', line)
    fname, box, sc, label = line[0], line[1], line[2], line[3]
    # print(fname, box, sc, label)
    box = box.split(";")
    sc = sc.split(";")
    label = label.split(";")
    # label = "".join(label)

    fpath = os.path.join(fdir, fname)
    # print(fpath)
    with open(fpath, "w") as fp:
        for idx, bb in enumerate(box):
            bb = bb.replace(",", " ")
            ln = label[idx] + ' ' + sc[idx] + ' ' + bb
            fp.write(str(ln))
            fp.write("\n")


if __name__ == "__main__":

    # Input csv dir
    csvFile = 'morpholocal_opening_MA.csv'
    # os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fcsv_path = os.path.join(os.getcwd(), csvFile)

    # Export directory for txt files
    txt_dir = os.path.join(os.getcwd(), 'Results2', 'yolov5m4', 'labels')
    if os.path.exists(txt_dir):
        # reset the output directory
        shutil.rmtree(txt_dir)
    os.makedirs(txt_dir)

    # read csv label file
    csv_lines = csv2list(csvFile)
    # Export txt label files
    for row_idx in csv_lines:#range(len(csv_lines)):
        # csvRow2txtline(txt_dir, csv_lines[row_idx])
        csvRow2txtline(txt_dir, row_idx)
        # print(row_idx)
    print("Done! ")


