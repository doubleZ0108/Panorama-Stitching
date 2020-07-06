# Panorama Stitching

Computer Vision | Tongji Univ. SSE Course Project

📝[REPORT](https://github.com/doubleZ0108/Panorama-Stitching/blob/master/report.pdf)

🎙[PRESENTATION](https://github.com/doubleZ0108/Panorama-Stitching/blob/master/presentation.pdf)

[toc]

------

## Background

Sometimes, when capturing, we can only get a partial image of the object, especially when the size of the object is extremely large. However, if the two partial images have some content overlapping, we can make use of CV algorithms to "stitch" them together to get a panorama of the scene. This is exactly the purpose of this project.

<br/>

## Experiment

### SIFT

- Scale Space and Image Pyramids
- Localizing Extrema
- Generating Orientations and Descriptors

<img src="https://upload-images.jianshu.io/upload_images/12014150-c90818606cbbc5d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" width="50%;" />

<br/>

### SURF

- Hessian Detector
- Math Behind Hessian Matrix
- Construction of feature vector
- Comparision between SIFT and SURF
- Results

<img src="https://upload-images.jianshu.io/upload_images/12014150-d265a2ff27e13b88.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="image.png" width="67%;" />

<br/>

### Fast Panorama Stitching on Mobile

- Current Approaches
- Summary
- Color and Luminance Compensation
- Optimal Seam Finding and Image Labeling
- Image Blending
- Results

![image.png](https://upload-images.jianshu.io/upload_images/12014150-2ead0cb7846e8f24.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

<br/>

## About the Author

|                 |                 |                       |
| --------------- | --------------- | --------------------- |
| **Team Leader** | Zhe ZHANG       | dbzdbz@tongji.edu.cn  |
| **Team Member** | Kaixin CHEN     | 1753188@tongji.edu.cn |
| **Team Member** | Yunxin SUN      | 1551534@tongji.edu.cn |
| **Advisor**     | Prof. Lin ZHANG | cs                    |

<br/>

## Project Structure

```
.
├── Panorama-Stitching-SURF
│   ├── paper
│   │   └── SURF_original_paper.pdf
│   ├── pre
│   │   ├── README.md
│   │   └── script.md
│   └── src
│       ├── main.py
│       └── requirement.txt
├── Panorama-Stitching-base-on-SIFT
│   ├── doc
│   │   └── SIFT精简流程.pdf
│   ├── paper
│   │   └── sift.pdf
│   ├── pre
│   │   ├── SIFT.pptx
│   │   └── script.md
│   └── src
│       ├── README.md
│       ├── main.py
│       └── siftPy.py
├── Panorama-Stitching-on-Mobile
│   ├── doc
│   │   └── paper_reading.pdf
│   ├── img
│   ├── paper
│   │   └── Fast Panorama Stitching for High-Quality Panoramic Images on Mobile Phones.pdf
│   ├── pre
│   │   ├── pre.pptx
│   │   └── script.md
│   └── src
│       └── fast-panorama-stitching-mobile.ipynb
├── README.md
├── presentation.pdf
└── report.pdf
```

