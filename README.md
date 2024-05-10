# R11921098_THESIS
Bandwidth-Efficient Inferencing at the Edge -- An Experimental Approach to Analyze the Effect of VSR on Compressed Video

### Setup
---

Clone this repo
```
git clone https://github.com/b06901089/R11921098_THESIS.git
cd R11921098_THESIS/
```

Clone [mAP](<https://github.com/Cartucho/mAP>) inside the repo
```
git clone https://github.com/Cartucho/mAP
```

Clone [BasicVSR++](<https://github.com/ckkelvinchan/BasicVSR_PlusPlus>) inside the repo
```
git clone https://github.com/ckkelvinchan/BasicVSR_PlusPlus.git
```

Overwrite files
```
cp restoration_video_demo.py BasicVSR_PlusPlus/demo/
cp -r chkpts/ BasicVSR_PlusPlus/
```

### Environment
---

We are going to create two virtual environments. 
Feel free to use your own environments for the first one.
It will be fine as long as YOLOv5 and FFmpeg is working.

```
conda create --name python3.8 python=3.8
conda activate python3.8
```

Install requirement for YOLOv5.
```
pip install -r requirements.txt
```

Install FFmpeg. It might require ffmpeg>=4.4 version.
```
pip install ffmpeg
```

Next, we are going to create a virtual environments for [BasicVSR++](<https://github.com/ckkelvinchan/BasicVSR_PlusPlus>).
Since mmcv depends very heavily on the version of pytorch and cuda.
I will be using specific CUDA 11.8 and specific Pytorch versions when installing mmcv.
```
conda create --name basicvsr python=3.8
conda activate basicvsr
pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
pip install openmim
mim install mmcv-full==1.6.0
cd BasicVSR_PlusPlus
pip install -v -e .
```

### Dataset
---

We are using [Inter4K](<https://github.com/alexandrosstergiou/Inter4K>) dataset. 
Download the dataset with the link [https://tinyurl.com/inter4KUHD](<https://tinyurl.com/inter4KUHD>) from the official repository.
Unzip it at wherever you want to save it.
```
unzip Inter4K.zip -d Inter4K
```

For example, I unzip it under "Datasets/". The structure of the dataset should look like below:
```
Datasets/
  Inter4K/
    Inter4K/
      60fps/
        UHD/
          1.mp4
          2.mp4
          (1000 mp4s)
```

### Inference
---

Run the inference with the following command:

```
python run.py --cfg <config files>
```

For example,
```
python run.py --cfg config/get_ground_truth.json
```

About the parameters in the config files, please refer to `config/parameter.py` and `config/*.json` for more information.

The results will be recorded in the log files.

![plot](https://github.com/b06901089/R11921098_THESIS/blob/main/image/example.png?raw=true)

For example, in order to produce this figure above.

I will have first to run mode=Get Ground Truth 1 time.

Then, run mode=Get High Quality 11 times for 11 different CRF values to get the purple line.

Then, run mode=Get Low Quality 11 times for 11 different CRF values as well for other four lines.

Or, You can run mode=Inference in only one command.

Again, please do check `config/parameter.py` and `config/*.json` for more information.

### Code Reference

```
https://github.com/alexandrosstergiou/Inter4K
https://github.com/Lornatang/FSRCNN-PyTorch
https://github.com/Cartucho/mAP
https://github.com/ckkelvinchan/BasicVSR_PlusPlus
```

All other necessary citations can be found in the original thesis. Thank you!