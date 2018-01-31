#! /usr/bin/env python
from extract_features import extract_features


if __name__ == '__main__':
    config_json = './extractor_config_sphere64_pod.json'
    save_dir = 'megaface-features-sphereface-64'
    gpu_id = None

    # image path: osp.join(image_dir, <each line in image_list_file>)
    image_dir = r'/workspace/code/mtcnn-caffe-zyf/scripts/face_aligner/megaface_mtcnn_aligned_dan/aligned_imgs'
    image_list_file = r'/workspace/data/__face_datasets__/MegaFace/MegaFace_dataset/megaface-img-list.txt'
    extract_features(config_json, save_dir, image_list_file, image_dir, gpu_id)