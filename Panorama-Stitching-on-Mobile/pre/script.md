第三部分我们研究mobile端的快速全景拼接算法



现在的panorama stitching approaches主要分为两大类，transition smoothing和optimal seam finding以及二者的结合

其中graph cut是现在用的比较多的方法



但是这些算法存在一些问题，比如图像颜色和光照的差别很大的图像效果非常差

Mobile也存在些自己的约束，比如memory少等等问题



我们的算法来自这篇论文，主要分为三大个模块

首先进行color correction

之后进行最优接缝的寻找和image labeling

第三步进行图像融合



颜色和光照校正的核心思想其实还是 gamma校正

主要分为两个步骤

第一步是aci也就是相邻两个图像重叠区域的一个校正因子

第二个是最优一个方程组得到的全局调整因子，这里我们用导数=0的闭式解来做



最终我们综合这两个调整因子

对原像素做一个gamma校正



这是我们的实现

首先要找到一张最优图片，这个其实偏重主观审美

我们采用的是寻找三个通道的均值极差越小越好（这个主要用在white balancing上）



第二部分我们最核心的是三个步骤

首先在颜色校正的基础上计算error surface

然后通过dynamic programming的方法一行行扫描error surface，计算一个累积的最小平方差

第三部就是通过回溯在所有可能的path中找到最优的一条接缝

这是我们每个模块的实现



最后一部分就是在接缝找到的基础上进行拼接，也就是图像融合

我们是找到两大个方法

简单线性融合，这个比较简单我们就略过了



第二种是泊松融合，其实使用的是梯度的信息

第三行公式是我们的一个离散展开



最后是我们的实现效果

这组图像的颜色差异很大，上面的是没有做颜色校正的



这组图第一个是没做颜色校正的

第二个是没做融合的，可以看到明显的锯齿接缝