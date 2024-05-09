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

# Get Ground Truth
p = {

    'mode':     'Get Ground Truth',
    # There are mainly three modes
    'log':      './My_log',
    # Folder path to saved logs
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    # Path to conda.sh
    'start':    1,
    # Start index of inference videos (1~1000)
    'end':      1,
    # End (include) index of inference videos (1~1000), End >= Start
    'crf':      0,
    # Set CRF to 0~51, otherwise set to '-1' if you want to use CQP. Should be Set to 0 when getting ground truth. 
    'qp':       -1,
    # Set CQP to 0~51, otherwise set to '-1' if you want to use CRF. Should be Set to 0 when getting ground truth.
    'inter':    '../../Datasets/Inter4K',
    # Usage: Path to Root Inter4K folder
    # The structure of the folder should look like this
    # Inter4K/
    #   Inter4K/
    #       60fps/
    #           UHD/
    # Please do not add '/' at the end of the string! Thank you!
    # Ex: '../../Datasets/Inter4K'
    # Not: '../../Datasets/Inter4K/'
    'res':      '1080p',
    # Usage: Target resolution, please refer to 'resolution_map' for more options
    # 4K, 2K, 1080p, 720p, 540p, 360p, 270p, 180p
    'name':     '1080p',
    # Folder name of the transcode videos and video frames, recommend to just use the same name as paramter 'res' when getting ground truth.
    'GT_name':  '',
    # Not used in this mode
}

# Get Low Quality
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
    # "GT_name" should be set to the folder name of the ground truth (i.e. 'name' in 'Get Ground Truth')

}

# Get High Quality
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
    'name':     '1080pHQ',
    # In 'Get High Quality' mode, add notation to prevent having the same name as GT folder
    'GT_name':  '1080p',

}