#!/usr/bin/env python
from extract_probs_and_refine_labels import extract_probs_and_refine_labels

if __name__ == '__main__':

    config_json = './extractor_config_sphere64_webface.json'

    prob_thresh = 0.7
    first_new_id = 10572
    max_orig_label = 2

    # image path: osp.join(image_dir, <each line in image_list_file>)
    image_dir = r'../../test_data/face_chips'
    image_list_file = r'../../test_data/face_chips_list_with_label.txt'

    save_dir = 'rlt_probs_and_refined_labels'
    num_images = -1 # <0, means all images
    mirror_input = False

    extract_probs_and_refine_labels(config_json, prob_thresh,
                                    first_new_id, max_orig_label,
                                    image_list_file, image_dir,
                                    save_dir, num_images, mirror_input)
