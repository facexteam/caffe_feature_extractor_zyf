#!/usr/bin/env python

from load_prob_stats_and_calc_hist_thresh import load_prob_stats_and_calc_hist_thresh

if __name__ == '__main__':
    stats_fn_list = [
        r'C:\zyf\dnn_models\face_models\face-datasets-merge\stats-max-label-info-webface-msceleb-corr.txt',
        r'C:\zyf\dnn_models\face_models\face-datasets-merge\stats-max-label-info-asian-msceleb-corr.txt',
        r'C:\zyf\dnn_models\face_models\face-datasets-merge\corr_prob-stats-max-label-info-vggface-msceleb.txt',
        r'C:\zyf\dnn_models\face_models\face-datasets-merge\corr_prob-stats-max-label-info-vggface2-msceleb.txt',
        r'C:\zyf\dnn_models\face_models\face-datasets-merge\corr_prob-stats-max-label-info-vggface2-msceleb.txt'
    ]
    num_ids_list = [10572, 10245, 2564, 8631, 78771]
    num_images_list = None


#    only_after_bin_val = False
    only_after_bin_val = 0.55
#    only_after_bin_val = 0.7

    show_hist = False

    num_fns = len(stats_fn_list)

    for i, stats_fn in enumerate(stats_fn_list):
        for j in range(i, num_fns):
            num_images1 = -1
            num_images2 = -1
            if num_ids_list:
                num_images1 = num_ids_list[i]
                num_images2 = num_ids_list[i]
            load_prob_stats_and_calc_hist_thresh(stats_fn_list[i], num_ids_list[i], num_images1,
                                                 stats_fn_list[j], num_ids_list[j], num_images2,
                                                 only_after_bin_val, show_hist)
