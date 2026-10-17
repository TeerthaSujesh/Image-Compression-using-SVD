SVD Image Compression Using Python

Overview

This project demonstrates image compression using Singular Value Decomposition (SVD), a linear algebra technique used to represent a matrix using its most significant components.

A grayscale image is represented as a matrix of pixel intensity values. SVD decomposes this matrix into three components, allowing us to reconstruct an approximation of the original image using only the first k singular values and their corresponding vectors.

By experimenting with different values of k, we can observe the trade-off between image quality and theoretical storage requirements.

Objectives

Understand how a grayscale image can be represented as a matrix.

Apply Singular Value Decomposition to an image matrix.

Visualize the distribution of singular values.

Reconstruct images using different numbers of singular values.

Compare image quality and estimate storage reduction.

Apply linear algebra concepts to a practical image-processing problem.

Technologies Used

Python

NumPy - Matrix operations and SVD computation

OpenCV - Image loading and grayscale conversion

Matplotlib - Graph plotting and image visualization

Tkinter - Interactive image file selection

Mathematical Background

1. Matrix Representation

A grayscale image is represented as a matrix A, where each element corresponds to a pixel's intensity.

For an 8-bit grayscale image, pixel intensities typically range from 0 (black) to 255 (white).

2. Singular Value Decomposition (SVD)

SVD decomposes the image matrix into three components:

$$
A = U \Sigma V^T
$$

Where:

U contains the left singular vectors.

Σ is a diagonal matrix containing singular values in decreasing order.

V^T contains the transposed right singular vectors.

The singular values indicate the relative magnitude of the corresponding components.

3. Low-Rank Approximation

Instead of retaining all singular values, we retain only the first k values and their corresponding vectors.

The reconstructed approximation is:

$$
A_k = U_k \Sigma_k V_k^T
$$

A smaller value of k generally results in greater information loss but requires fewer stored numerical values. A larger value of k preserves more image detail but requires more storage.

4. Estimated Storage Reduction

For an image matrix with m rows and n columns:

Original representation: m × n numerical values

Reduced SVD representation: m × k + k + k × n numerical values

The estimated percentage reduction is calculated as:

$$
\text{Reduction} =
\left(1 - \frac{mk + k + kn}{mn}\right) \times 100
$$

This estimates the reduction in the number of stored numerical values, assuming comparable storage costs per value. It is not a measurement of actual compressed file size.

Project Workflow

Select an image: Choose an image using the file picker.

Preprocess the image: Convert it to grayscale and floating-point format.

Apply SVD: Decompose the image matrix into U, singular values, and V^T.

Visualize singular values: Plot the singular values to observe how their magnitudes decrease.

Choose k: Enter one or more values, such as 10,60,300.

Reconstruct images: Use the first k singular values and corresponding vectors to generate approximations.

Compare results: Display the original and reconstructed images alongside the estimated storage reduction.

Linear Algebra Concepts Demonstrated

Matrix representation of image data

Singular Value Decomposition

Singular values and their significance

Orthonormal bases

Low-rank matrix approximation

Matrix multiplication and reconstruction

Numerical representation and storage comparison

Limitations

The current implementation displays reconstructed images but does not save compressed image files.

The reported storage reduction is based on numerical-value counts, not actual file sizes or encoded image sizes.

Smaller values of k can cause noticeable loss of image detail.

The script performs reduced SVD, which may be computationally expensive for very large images.

Future Improvements

Save reconstructed images to disk.

Compare reconstruction error for different values of k.

Calculate actual storage usage for a saved factorized representation.

Allow users to select k using a slider.

Explore automatic selection of k based on reconstruction quality.

Extend the method to color images by processing individual color channels.

Conclusion

This project demonstrates how Singular Value Decomposition can be applied to image compression through low-rank approximation. By retaining only selected singular-value components, we can reconstruct visually meaningful approximations of an image while reducing the number of numerical values required for its representation.

The experiment illustrates a fundamental application of linear algebra: using matrix decomposition to balance representation size and reconstruction accuracy.



