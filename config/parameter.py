# resolution_map = {
#     '4K':   [3840, 2160],
#     '2K':   [2560, 1440],
#     '1080p':[1920, 1080],
#     '720p': [1280, 720],
#     '540p': [960, 540],
#     '360p': [640, 360],
#     '270p': [480, 270],
#     '180p': [320, 180],
# }

p = {

    'mode':     'Get Ground Truth',
    'log':      './My_log',
    # Usage: Folder path to saved logs
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    # Usage: Path to conda.sh
    'start':    1,
    'end':      1,
    'crf':      0,
    # Set to '-1' if you want to use CQP, otherwise, set CRF to 0~51
    'qp':       -1,
    # Set to '-1' if you want to use CRF, otherwise, set CQP to 0~51
    'inter':    '../../Datasets/Inter4K',
    # Usage: Path to Root Inter4K folder
    # The structure of the folder should look like this
    # Inter4K/
    #   Inter4K/
    #       60fps/
    #           UHD/
    #   Inter4K_frame/
    #       60fps/
    # Please do not add '/' at the end of the string!
    # Ex: '../../Datasets/Inter4K'
    # Not: '../../Datasets/Inter4K/'
    'res':      '1080p',
    # Usage: Target resolution, please reference dictionary 'resolution_map' for more options
    # Ex: 4K, 2K, 1080p, 720p
    'name':     '1080p',
    # Folder name of the transcode videos and video frames, recommend to use the same name as paramter 'res'
    # Ex: 2K, 720p

}

p = {

    'mode':     'Get Low Quality',
    'log':      './My_log',
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      30,
    'qp':       -1,
    'inter':    '../../Datasets/Inter4K',
    'res':      '270p',
    'name':     '270p',
    'GT_name':  '1080p',
    # Folder name of the ground truth videos, the resolution should be 4x of the low quality videos
    # "GT_name" should not be the same as "name"

}

p = {

    'mode':     'Get High Quality',
    'log':      './My_log',
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      30,
    'qp':       -1,
    'inter':    '../../Datasets/Inter4K',
    'res':      '1080p',
    'name':     '1080p_CRF30',
    # In 'Get High Quality' mode, add notation to prevent having the same name as GT folder
    # Ex: 720p_CRF30
    'GT_name':  '1080p',

}