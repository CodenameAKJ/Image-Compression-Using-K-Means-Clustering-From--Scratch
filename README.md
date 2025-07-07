# Image-Compression-Using-K-Means-Clustering from Scratch

Using unsupervised learning techniques to compress the image file size with less compromise in overall quality.

## Overview

This project demonstrates the application of K-Means clustering, a prominent unsupervised machine learning algorithm, to the task of image compression. The primary goal is to significantly reduce the file size of images by quantizing colors, while maintaining a visually acceptable level of quality. This showcases a practical application of clustering for dimensionality reduction and data representation in image processing.

## Problem Statement

Digital images often contain a vast number of distinct colors, leading to large file sizes. For applications requiring efficient storage, faster transmission, or reduced memory footprint, compressing these images is crucial. Traditional compression methods exist, but this project explores how a machine learning approach like K-Means can effectively achieve this by intelligently reducing the color palette of an image.

## Methodology

The core idea behind this image compression technique is to treat each pixel's color (represented by its RGB values) as a data point. K-Means clustering then groups these data points into a predefined number of clusters (K), where each cluster represents a new, dominant color.

The process involves the following key steps, implemented from scratch:

1.  **Image Loading:** The input image is read and its pixel data is extracted. Each pixel, with its Red, Green, and Blue (RGB) components, forms a 3-dimensional data point.
2.  **Data Reshaping:** The image's 2D pixel grid (height x width) is reshaped into a 1D array of individual pixels, each being an RGB vector. This transformed data serves as the input `X` for the K-Means algorithm.
3.  **Random Initialization of Centroids:** K initial centroids (representing `K` distinct colors) are randomly selected from the image's pixel data.
4.  **`find_closest_centroids(X, centroids)`:** This function iterates through each pixel in the image (`X`) and assigns it to the closest centroid based on Euclidean distance. This determines which of the `K` new colors each original pixel will take on.
5.  **`compute_centroids(X, idx, K)`:** After all pixels are assigned, this function recomputes the new positions of the `K` centroids. Each new centroid is the mean of all pixel data points assigned to its cluster.
6.  **`run_kMeans(X, initial_centroids, max_iters)`:** This function iteratively runs the `find_closest_centroids` and `compute_centroids` functions for a specified number of `max_iters` (e.g., 10 iterations), allowing the centroids to converge to optimal color representations.
7.  **Image Reconstruction:** Once the K-Means algorithm converges and the final `K` centroids (colors) are determined, the original image is reconstructed. Each pixel is replaced by the color of the centroid it was assigned to, effectively quantizing the image's color palette.
8.  **Display and Comparison:** The original image and the compressed image are displayed side-by-side to visually assess the quality retention and the effect of compression.

## Tools Used

* `Python`
* `NumPy` (for numerical operations and array manipulation)
* `Matplotlib` (for image loading and visualization)
* `PIL (Pillow)` (implicitly used by `matplotlib.pyplot.imread` for image handling)

## Key Results / Insights

This project successfully demonstrates that K-Means clustering can be a highly effective method for image compression. By reducing the number of distinct colors in an image to a user-defined `K`, significant file size reduction can be achieved with minimal perceptual loss of quality, especially when `K` is chosen appropriately.

![Original](images/Original_image.jpg)
![Compressed](images/Reconstructed_image.jpg)


