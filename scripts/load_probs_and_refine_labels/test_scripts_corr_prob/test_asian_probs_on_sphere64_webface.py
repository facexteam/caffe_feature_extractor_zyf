#!/usr/bin/env python
import _init_paths
from load_probs_and_refine_labels import load_probs_and_refine_labels
import os.path as osp
import numpy as np

if __name__ == '__main__':

    prob_threshs = [0.4, 0.85, 0.5]
    first_new_id = 10572
    max_orig_label = 10244


    # image path: osp.join(image_dir, <each line in image_list_file>)
    prob_dir = r'/home/asian_probs_on_sphere64_webface/corr_prob'
    image_list_file = r'/disk2/zhaoyafei/face-recog-train/train-val-lists/asian/face_asian_train_list_noval_10245-ids_540735-objs_170818-225846-norootdir.txt'

    # save_dir = None
    save_dir = '../../prob-results/asian_probs_on_sphere64_webface/corr_prob_threshed_results'

    num_images = -1  # <0, means all images
    mirror_input = False

    for thresh in prob_threshs:
        load_probs_and_refine_labels(prob_dir, thresh,
                                     first_new_id, max_orig_label,
                                     image_list_file, num_images,
                                     save_dir)
