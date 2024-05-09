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
Feel free to use your own environments.
It will be fine as long as YOLOv5 is working.

```
conda create --name python3.8 python=3.8
conda activate python3.8
```

Install requirement for YOLOv5.
```
pip install -r requirements.txt
```

Install FFmpeg.
```
pip install ffmpeg
```

Next, we are going to create a virtual environments for BasicVSR.
Since mmcv depends on the version of pytorch and cuda very heavily.
I will be using specific CUDA 11.8 when installing mmcv.
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