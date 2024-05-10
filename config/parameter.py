# Detail explanation of other example json files
# Only 4x SR ratio is supported
# i.e. (4K, 540p), (2K, 360p), (1080p, 270p), (720p, 180p)

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
    'GT_res':   '',
    # Not used in this mode
    'pyenv':    'python3.8',
    # Conda env name for YOLOv5 and FFmpeg
    'vsrenv':   'basicvsr',
    # Conda env name for BasicVSR++
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
    'GT_res':   '1080p',
    # Resolution of ground truth, the resolution should be 4x of the low quality videos
    # (i.e. 'GT_res' should equal to 'res' in 'Get Ground Truth')
    'pyenv':    'python3.8',
    'vsrenv':   'basicvsr',
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
    'GT_res':   '1080p',
    'pyenv':    'python3.8',
    'vsrenv':   'basicvsr',
}

# Inference
p = {

    'mode':     'Inference',
    'log':      './My_log',
    # All logs of a single 'mode'='Inference' run will be stored in an indivisual folder inside 'log' folder
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      [0,2,5,7,10,15,20,25,30,35,40],
    # All the CRF value you want to run in a complete experiment
    'qp':       -1,
    # Or All the CQP value you want to run in a complete experiment
    'inter':    '../../Datasets/Inter4K',
    'res':      '270p',
    'GT_res':   '1080p',
    'pyenv':    'python3.8',
    'vsrenv':   'basicvsr',
}