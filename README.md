# Panorama Stitching

Computer Vision | Tongji Univ. SSE Course Project

* [Background](#background)
* [Project Structure](#project-structure)
* [Experiment](#experiment)
   * [SIFT](#sift)
   * [SURF](#surf)
   * [Fast Panorama Stitching on Mobile](#fast-panorama-stitching-on-mobile)
* [About the Author](#about-the-author)

------

## Background

Sometimes, when capturing, we can only get a partial image of the object, especially when the size of the object is extremely large. However, if the two partial images have some content overlapping, we can make use of CV algorithms to "stitch" them together to get a panorama of the scene. This is exactly the purpose of this project.

<br/>

## Project Structure

- `Experiment/`

  - [Panorama Stitching base on SIFT](https://github.com/doubleZ0108/Panorama-Stitching/tree/master/Panorama-Stitching-SIFT)
  - [Panorama Stitching SURF](https://github.com/doubleZ0108/Panorama-Stitching/tree/master/Panorama-Stitching-SURF)
  - [Panorama Stitching on Mobile](https://github.com/doubleZ0108/Panorama-Stitching/tree/master/Panorama-Stitching-on-Mobile)

  ```
  .
  ├── doc
  │   └── paper_reading.pdf
  ├── img
  │   ├── ...
  ├── paper
  │   └── ...
  ├── pre
  │   ├── pre.pdf
  │   └── script.md
  └── src
      └── ...
  ```

- `document/`

  - 📝[report](https://github.com/doubleZ0108/Panorama-Stitching/blob/master/doc/report.pdf)
  - 🎙[presentation slides](https://github.com/doubleZ0108/Panorama-Stitching/blob/master/doc/presentation.pdf)

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

| Item            | Name            | Email                    |
| --------------- | --------------- | ------------------------ |
| **Team Leader** | Zhe ZHANG       | dbzdbz@tongji.edu.cn     |
| **Team Member** | Kaixin CHEN     | 1753188@tongji.edu.cn    |
| **Team Member** | Yunxin SUN      | 1551534@tongji.edu.cn    |
| **Advisor**     | Prof. Lin ZHANG | cslinzhang@tongji.edu.cn |
