﻿/*
OpenCv版本 opencv-4.5.5-vc14_vc15
内容：SURF/SIFT特征点检测
博客：http://www.bilibili996.com/Course?id=2848892000230
作者：高仁宝
时间：2023.11
*/

#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/features2d.hpp>
#include <opencv2/features2d/features2d.hpp>

using namespace cv;
using namespace std;

int main()
{
    //【1】载入图像
    Mat srcImage1 = imread("../images/book2.jpg");
    Mat srcImage2 = imread("../images/book3.jpg");

    //【2】定义SIFT中的hessian阈值特征点检测算子
    int minHessian = 400;
    Ptr<SIFT> siftDetector = SIFT::create(minHessian);
    vector<KeyPoint> keypoints_1, keypoints_2;

    //【3】调用detect函数检测出SIFT特征关键点，保存在vector容器中
    siftDetector->detect(srcImage1, keypoints_1);
    siftDetector->detect(srcImage2, keypoints_2);

    //【4】绘制特征关键点
    Mat img_keypoints_1;
    Mat img_keypoints_2;
    drawKeypoints(srcImage1, keypoints_1, img_keypoints_1, Scalar(0, 255, 0), DrawMatchesFlags::DEFAULT);
    drawKeypoints(srcImage2, keypoints_2, img_keypoints_2, Scalar(0, 255, 0), DrawMatchesFlags::DEFAULT);

    //【5】显示效果图
    imshow("特征点检测效果图1", img_keypoints_1);
    imshow("特征点检测效果图2", img_keypoints_2);

    waitKey(0);
    return 0;
}