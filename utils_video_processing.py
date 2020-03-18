"""
Author- Belayat Hossain, 17/3/2020, Advanced Medical Engineering Center, U of Hyogo
Purpose: fast processing of creating training data set from video
Usage: To extract video frame by taking frame index and label from a annotation text file (accept YOLOv3-keras format)
        and export to class directory (cat, dog) based on class label.
        Annotation format, <frameIndex>,<integer>,<box-topleft1>,<box-topleft2>,<box-bottomright1>,<box-bottomright2>,<class_label>
                           10,1,680,259,350,242,cat
            
Run: python utils_video_processing.py
"""


import os, sys
import cv2


def read_text_file(base_dir, label_file_name):
    input_text_file_dir = base_dir + label_file_name
    with open(input_text_file_dir) as f:
        lines = f.read().splitlines()
    return lines


def write_text_file(base_dir, label_file_name, np_str_data):
    out_file_name = base_dir + "sorted_" + label_file_name
    with open(out_file_name, "w") as fp:
        for i in np_str_data:
            fp.write(str(i))
            fp.write("\n")


def extract_defined_video_frame(base_dir, label_file_name, video_name):
    video_path = base_dir + video_name
    video_dir_name = video_name.split(".")[0]
    video_dir = os.path.join(base_dir, video_dir_name)

    cap = cv2.VideoCapture(video_path)  # video_name is the video being called
    lines = read_text_file(base_dir, label_file_name)

    for line in range(len(lines)):
        frame_index = lines[line].split(",")[0]
        frame_label = lines[line].split(",")[-1]
        print("{}no, {}".format(frame_index, frame_label))
        cap.set(1, int(frame_index))
        ret, frame = cap.read()  # Read the frame
        class_dir = os.path.join(video_dir, frame_label)
        cv2.imwrite(os.path.join(class_dir, video_dir_name + "_" + str(frame_index) + '.jpg'), frame)


def export_frame_index_and_label(base_dir, label_file_name):
    """
    Note: OPTIONAL FUNCTION
    INPUT: label text file format, <frameIndex> <boxtrial>, <box>, <class_label>
            10 1 12 78 13 54 cat
            11 1 12 78 13 54 dog
    OUTPUR: <frameIndex> <class_label>
            10 cat
            11 dog
            ......
    """
    input_text_file_dir = base_dir + label_file_name
    fr_no_and_labels = []
    with open(input_text_file_dir) as f:
        lines = f.read().splitlines()
        # print("totla ",len(lines))
        for line in range(len(lines)):
            frame_no = lines[line].split(",")[0]
            frame_label = lines[line].split(",")[-1]
            fr_no_and_label = str(frame_no)+" " + str(frame_label)
            fr_no_and_labels.append(fr_no_and_label) # To export frame index and label
    return fr_no_and_labels


def make_dir(base_dir, video_name):
    # make directory (with class subdirectory) for each video file name
    video_dir_name = video_name.split(".")[0]

    # using class file
    try:
        img_dir = os.path.join(base_dir, video_dir_name)
        os.mkdir(img_dir)
        lines = read_text_file(base_dir, class_file)
        for id, cl_name in enumerate(lines):
            # print(cl_name)
            new_sub_dir = os.path.join(img_dir, cl_name)
            os.mkdir(new_sub_dir)
        extract_defined_video_frame(base_dir, label_file_name, video_name)
        
    except:
        print("[INFO...:] Delete all class directories which are named by video name")

    """
    try:
        img_dir = os.path.join(base_dir, video_dir_name)
        img_dir_subdir1 = os.path.join(img_dir, "cat")
        img_dir_subdir2 = os.path.join(img_dir, "dog")
        img_dir_subdir3 = os.path.join(img_dir, "rat")
        os.mkdir(img_dir), os.mkdir(img_dir_subdir1), os.mkdir(img_dir_subdir2), os.mkdir(img_dir_subdir3)
        extract_defined_frame_video(base_dir, label_file_name, video_name)

    except:
        print("[INFO...:] Delete all class directory which are named by video name")
    """


if __name__ == '__main__':

    # ========================== Set directory/ file name here ======================
    # base directory where video, annotation file, image- are stored/to be stored
    base_dir = "//HDD2/videos/"
    label_file_name = "video_1_hand.txt"  # video file name
    video_name = "video_1_hand.mp4"   # annotation file name
    class_file = "class.txt"
    # ===============================================================================

    img_dir = make_dir(base_dir, video_name)






