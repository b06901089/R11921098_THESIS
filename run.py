### Stop the running bash shell script by using
### Ctrl-Z
### kill %%
### See Ref: https://unix.stackexchange.com/questions/48425/how-to-stop-the-loop-bash-script-in-terminal/48432#48432

import os
import json
import argparse
import pathlib

from datetime import datetime

# resolutions = { 'UHD':[3840, 2160],
#                 'QHD':[2560,1440],
#                 'FHD':[1920,1080],
#                 'HD':[1280,720],
#                 'qHD':[960,540],
#                 'nHD':[640,360]
# }

def set_log(p):

    c = datetime.now()
    log_name = str(c.year) + '_' + str(c.month) + '_' + str(c.day) + '_' + str(c.hour) + '_' + str(c.minute) + '_' + str(c.second) + '_log.txt'
    log_path = os.path.join(p['log'], log_name)
    p['log_name'] = log_path
    with open(log_path, 'a') as f:
        f.write('Parameters:\n\n')
        f.write('##########\n')
        for key in p.keys():
            f.write('{}: {}\n'.format(key, p[key]))
        f.write('##########\n\n')

def get_data(p):

    if p['crf'] >= 0 and p['crf'] <= 51:
        os.system('bash inf_get_data.sh {} {} {} {} {} {} {} {} {} {}'.format(
            p['source'], 
            p['start'], 
            p['end'], 
            'crf', 
            p['crf'],
            p['inter'],
            p['res'],
            p['name'],
            p['log_name'],
            p['pyenv'],
        ))
    elif p['qp'] >= 0 and p['qp'] <= 51:
        os.system('bash inf_get_data.sh {} {} {} {} {} {} {} {} {} {}'.format(
            p['source'], 
            p['start'], 
            p['end'], 
            'qp', 
            p['qp'],
            p['inter'],
            p['res'],
            p['name'],
            p['log_name'],
            p['pyenv'],
        ))
    else:
        print('Error: Incorrect Parameter (CRF/QP) Settings!')
        with open(p['log_name'], 'a') as f:
            f.write('Error: Incorrect Parameter (CRF/QP) Settings!\n')

def get_bitrate(p):

    os.system('bash inf_get_bitrate.sh {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['log_name'],
        p['pyenv'],
    ))

def get_BI(p):

    os.system('bash inf_get_BI.sh {} {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['GT_res'],
        p['log_name'],
        p['pyenv'],
    ))

def get_FSRCNN(p):

    os.system('bash inf_get_FSRCNN.sh {} {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['GT_res'],
        p['log_name'],
        p['pyenv'],
    ))

def get_BasicVSR(p):

    os.system('bash inf_get_BasicVSR.sh {} {} {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['GT_res'],
        p['log_name'],
        p['pyenv'],
        p['vsrenv'],
    ))

def get_inference(p):

    os.system('bash inference.sh {} {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['GT_res'],
        p['log_name'],
        p['pyenv'],
    ))

def get_HQ(p):

    os.system('bash inf_get_HQ.sh {} {} {} {} {} {} {} {}'.format(
        p['source'], 
        p['start'], 
        p['end'], 
        p['inter'],
        p['name'],
        p['GT_res'],
        p['log_name'],
        p['pyenv'],
    ))

def Get_Ground_Truth(p):
    p['name'] = p['res']
    set_log(p) 
    get_data(p)
    get_bitrate(p)

def Get_Low_Quality(p):
    p['name'] = p['res']
    set_log(p)     
    get_data(p)
    get_bitrate(p)
    get_BI(p)
    get_FSRCNN(p)
    get_BasicVSR(p)
    get_inference(p)

def Get_High_Quality(p):
    p['name'] = p['res'] + '_cp'
    set_log(p)
    get_data(p)
    get_bitrate(p)
    get_HQ(p)
    get_inference(p)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str)
    args = parser.parse_args()

    with open(args.cfg, 'r') as f:
        p = json.load(f)

    pathlib.Path(p['log']).mkdir(parents=True, exist_ok=True)
    pathlib.Path('./My_output').mkdir(parents=True, exist_ok=True)
    pathlib.Path(os.path.join(p['inter'], 'Inter_frame/60fps')).mkdir(parents=True, exist_ok=True)


    if p['mode'] == 'Get Ground Truth':
        Get_Ground_Truth(p)

    elif p['mode'] == 'Get Low Quality':
        Get_Low_Quality(p)

    elif p['mode'] == 'Get High Quality':
        Get_High_Quality(p)

    elif p['mode'] == 'Inference':
        tmp_crf = p['crf']
        tmp_qp = p['qp']
        tmp_res = p['res']
        tmp_GT = p['GT_res']

        # Log Naming
        run_idx = 0
        while os.path.isdir(os.path.join(p['log'], f'run{run_idx}')):
            run_idx += 1
        p['log'] = os.path.join(p['log'], f'run{run_idx}')
        pathlib.Path(p['log']).mkdir(parents=True, exist_ok=True)

        # CRF
        if p['crf'] != -1:

            p['mode'] = 'Get Ground Truth'
            p['res'] = tmp_GT
            p['crf'] = 0
            Get_Ground_Truth(p)

            p['mode'] = 'Get Low Quality'
            p['res'] = tmp_res
            p['GT_res'] = tmp_GT
            
            for crf in tmp_crf:
                p['crf'] = crf
                Get_Low_Quality(p)

            p['mode'] = 'Get High Quality'
            p['res'] = tmp_GT

            for crf in tmp_crf:
                # CRF = 0 is ground truth
                if crf != 0:
                    p['crf'] = crf
                    Get_High_Quality(p)

        # CQP
        elif p['qp'] != -1:

            p['mode'] = 'Get Ground Truth'
            p['res'] = tmp_GT
            p['qp'] = 0
            Get_Ground_Truth(p)

            p['mode'] = 'Get Low Quality'
            p['res'] = tmp_res
            p['GT_res'] = tmp_GT
            
            for qp in tmp_qp:
                p['qp'] = qp
                Get_Low_Quality(p)

            p['mode'] = 'Get High Quality'
            p['res'] = tmp_GT

            for qp in tmp_crf:
                # CQP = 0 is ground truth
                if qp != 0:
                    p['qp'] = qp
                    Get_High_Quality(p)