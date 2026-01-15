# Projekt-inzynierski / Engineering-thesis 2024

# Box-Counting Dimension for Image Analysis

## 1. Overview
This project focuses on the implementation of a tool for estimating the box-counting (fractal) dimension of objects present in digital images.
The box-counting dimension is a quantitative measure of geometric complexity and self-similarity, commonly used in image analysis and pattern characterization.

The project was developed as part of an engineering thesis and emphasizes algorithmic image analysis rather than machine learning approaches.

## 2. Problem Statement
The objective of the project was to:

- design and implement an algorithm for computing the box-counting dimension,

- adapt the method for use with digital images,

- build a reusable and configurable Python-based analytical tool.

A key challenge was ensuring robustness of the dimension estimation with respect to image resolution, noise, and preprocessing choices.

## 3. Input Data
The tool operates on:
- binary images,
- grayscale images after thresholding.
  
Test data included:
- synthetic images with known fractal properties,
- real images used to evaluate stability and correctness of the algorithm.
  
## 4. Methodology
The implemented box-counting procedure consists of the following steps:
1. Image preprocessing (binarization, normalization).
2. Overlaying grids of different box sizes onto the image.
3. Counting the number of boxes containing at least one pixel belonging to the object.
4. Estimating the box-counting dimension as the slope of the linear regression in a log–log plot:
 
 <p align="center">  
  $D = -\lim_{\varepsilon \to 0} \frac{\log N(\varepsilon)}{\log \varepsilon}$
  </p>

The implementation allows experimenting with different grid resolutions and preprocessing parameters.

## 5. Implementation Details
**Language:** Python

**Libraries:** NumPy, image processing utilities

**Architecture:** modular design separating preprocessing, counting logic, and result visualization

The code structure enables:
- easy extension of the algorithm,
- testing on different image datasets,
- integration with other image analysis pipelines.

## 6. Results
The tool was validated by:
- applying it to synthetic images with known fractal dimensions,
- analyzing the influence of image resolution and thresholding on the estimated dimension.

Example visualizations:
  
<img width="431" height="286" alt="image" src="https://github.com/user-attachments/assets/45b2efe7-68ae-43dc-a4d7-4ce8778e2b5e" />
<img width="303" height="397" alt="image" src="https://github.com/user-attachments/assets/110641e9-db05-4116-a415-6afd43f8ed19" />
<img width="450" height="267" alt="image" src="https://github.com/user-attachments/assets/f122f349-565d-4dca-97ed-ecc7ad8c6b1d" />
<img width="283" height="362" alt="image" src="https://github.com/user-attachments/assets/586e2928-556c-4486-9fd0-a381cfae73b6" />
<br><br>

The results demonstrate that:
- the method provides stable estimates within a reasonable range of parameters,
- preprocessing quality significantly impacts the final dimension value.


## 7. Limitations
- sensitivity to image binarization quality,
- dependence on image resolution,
- limited robustness for highly noisy images.
  
These limitations highlight potential areas for improvement.

## 8. Possible Extensions
- automatic image segmentation prior to analysis,
- noise reduction techniques,
- combination with machine learning models for adaptive preprocessing,
- batch processing of large image datasets.

## 9. Academic Reference
This project was developed as part of an engineering thesis.

Full thesis (PDF):

https://drive.google.com/file/d/1EK3izzA2Eus53hDJW_peHnIarD7pcm9x/view?usp=sharing
