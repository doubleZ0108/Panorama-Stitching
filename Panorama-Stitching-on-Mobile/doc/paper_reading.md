# Fast Panorama Stitching for High-Quality Panoramic Images on Mobile Phones

[toc]

------

## 2 main categories of current image stiching approaches

- **transition smoothing**: reduce color differences between source images to make seams invisible and remove stitching artifacts
  - **Alpha blending**: fast transition smoothing approach, but it cannot avoid ghosting problems caused by object motion and small spatial alignment errors
  - **Gradiend Domain Image Blending approaches**: can reduce color differences and smooth color transitions using gradient domain operations, producing high-quality composite images
- **optimal seam finding**: search for seams in overlapping areas along paths where differences between source images are minimal
- **combination**: optimal seams first, if seams and stitching artifacts are visible, transition smoothing to reduce color differences to hide the artifacts then
  - graph cut -> find optimal seams
  - poisson blending -> smoothing color transitions

**Problem**

- computational and memory costs are high
- pixels are easy saturated in color correction
- don't work well for source images in very different colors and luminance
- linear blending, moving objects on the overlapping areas will cause ghosting artifacts



## Basic Steps

- Color Correction
  - color correction for all source images to reduce color differences
  - smoothen remaining color transitions between adjacent images
- Image Labeling
  - error surface is constructed with squared differences between overlapping images
  - low-cost path is found through the error surface by dunamic programming and used as an optimal seam to create labeling
- Image Blending Operations
  - linear blending -> source images are similar in color and luminance
  - poisson blending -> colors remain too different



## Summary

![image-20200703213150950](paper_reading.assets/image-20200703213150950.png)

- dont't need to keep all source images in memory due to the sequential stitching
- dynamiic programming for optimal seam finding allowing image labeling mush faster than using graph cut
- combination of color correction and image blending allow to construct high-quality panoramic image



## Algorithm

### Color and Luminance Compensation

- images captured in paper: automated setting s for focus, exposure, and white balance

- compute light averages in the overlap area by linearizing the gamma-corrected RGB values

- <img src="paper_reading.assets/image-20200703234621857.png" alt="image-20200703234621857" style="zoom:50%;" />

- global adjustment in the whole image sequence $g_c$ for each color channel $c$

- <img src="paper_reading.assets/image-20200703235635308.png" alt="image-20200703235635308" style="zoom:50%;" />

- <img src="paper_reading.assets/image-20200704000206246.png" alt="image-20200704000206246" style="zoom:50%;" />

  > 【gamma corrected】
  >
  > https://blog.csdn.net/candycat1992/article/details/46228771
  >
  > https://www.cnblogs.com/qiqibaby/p/5325193.html

- choosing the best image: callesthetic judgment

  - in paper: select the image with most similar means in the R,G, and B chnnels(gray world assumption ofter used in white balancing)

- advantages

  <img src="paper_reading.assets/image-20200704001828063.png" alt="image-20200704001828063" style="zoom:50%;" />