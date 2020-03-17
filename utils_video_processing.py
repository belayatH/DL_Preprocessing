"""
Belayat, AMEC, U Hyogo, 17/3/2020
Purpose: fast processing of creating training data set from video
Usage: To extract video frame by taking frame index from a label text file (accept YOLOv3-keras format only)
        and export to class directory (cat, dog) based on class label

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


def extract_defined_frame_video(base_dir, label_file_name, video_name):
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
    # [TO DO Later] need to extend this function by reading class file
    # class_file = "class.txt"

    read_text_file(base_dir, label_file_name)
    video_dir_name = video_name.split(".")[0]
    try:
        img_dir = os.path.join(base_dir, video_dir_name)
        img_dir_subdir1 = os.path.join(img_dir, "hand")
        img_dir_subdir2 = os.path.join(img_dir, "nohand")
        img_dir_subdir3 = os.path.join(img_dir, "nonsurgery")
        os.mkdir(img_dir), os.mkdir(img_dir_subdir1), os.mkdir(img_dir_subdir2), os.mkdir(img_dir_subdir3)
        extract_defined_frame_video(base_dir, label_file_name, video_name)

    except:
        print("[INFO...:] Delete all class directory which are named by video name")


if __name__ == '__main__':

    # ========================== Set directory/ file name here ======================
    # base directory where video, annotation file, image- are stored/to be stored
    base_dir = "//QNAP3/data/j3tera3/working/Belayat/rawdata/handaction/ukavideos/"
    label_file_name = "UKA_1_hand.txt"  # video file name
    video_name = "UKA_1_hand.mp4"   # annotation file name
    # class_file = "class.txt"
    # ===============================================================================

    img_dir = make_dir(base_dir, video_name)


