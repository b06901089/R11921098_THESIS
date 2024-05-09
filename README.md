# R11921098_THESIS
Bandwidth-Efficient Inferencing at the Edge -- An Experimental Approach to Analyze the Effect of VSR on Compressed Video

## Setup

Clone this repository
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

Overwrite a file
```
cp restoration_video_demo.py BasicVSR_PlusPlus/demo/
```

### Dataset
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

