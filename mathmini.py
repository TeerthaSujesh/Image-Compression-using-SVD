
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog


# -----------------------------
# SELECT IMAGE FILE
# -----------------------------

root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

if image_path == "":
    print("No image selected.")
    raise SystemExit


# -----------------------------
# LOAD THE IMAGE
# -----------------------------

ImJPG = cv2.imread(
    image_path,
    cv2.IMREAD_GRAYSCALE
)

if ImJPG is None:
    print("Error: Could not load the selected image.")
    raise SystemExit

# Convert image to floating point
ImJPG = ImJPG.astype(np.float64)


# -----------------------------
# PERFORM SVD
# -----------------------------

UIm, SIm, VIm = np.linalg.svd(
    ImJPG,
    full_matrices=False
)


# -----------------------------
# GET K VALUES FROM USER
# -----------------------------

k_input = input(
    "Enter k values separated by commas (example: 50,100,150): "
)

k_values = [
    int(k.strip())
    for k in k_input.split(",")
]


# -----------------------------
# CHECK VALID K VALUES
# -----------------------------

max_k = min(ImJPG.shape)

for k in k_values:

    if k <= 0 or k > max_k:

        print(f"Invalid k value: {k}")
        print(f"k must be between 1 and {max_k}.")

        raise SystemExit


# -----------------------------
# CREATE ONE WINDOW
# -----------------------------

num_images = len(k_values) + 1

fig = plt.figure(
    figsize=(5 * num_images, 9)
)

# Two rows:
# Row 1 -> Singular value graph
# Row 2 -> Original + compressed images

gs = fig.add_gridspec(
    2,
    num_images,
    height_ratios=[1, 2]
)


# -----------------------------
# SINGULAR VALUES GRAPH
# -----------------------------

ax_graph = fig.add_subplot(
    gs[0, :]
)

ax_graph.plot(
    np.arange(len(SIm)),
    SIm
)

ax_graph.set_title(
    "Singular Values"
)

ax_graph.set_xlabel(
    "Singular Value Index"
)

ax_graph.set_ylabel(
    "Singular Value"
)

ax_graph.grid()


# -----------------------------
# ORIGINAL IMAGE
# -----------------------------

ax_original = fig.add_subplot(
    gs[1, 0]
)

ax_original.imshow(
    ImJPG,
    cmap="gray"
)

ax_original.set_title(
    "Original Image"
)

ax_original.axis("off")


# -----------------------------
# COMPRESS FOR EACH K
# -----------------------------

m, n = ImJPG.shape

for i, k in enumerate(k_values):

    # Take first k columns of U
    U_k = UIm[:, :k]

    # Take first k singular values
    S_k = SIm[:k]

    # Take first k rows of V
    V_k = VIm[:k, :]

    # Create diagonal matrix of singular values
    S_matrix = np.diag(S_k)

    # Reconstruct compressed image
    ImJPG_comp = np.dot(
        U_k,
        np.dot(S_matrix, V_k)
    )


    # -----------------------------
    # COMPRESSION PERCENTAGE
    # -----------------------------

    # Original image:
    # m * n values

    # SVD representation:
    # U -> m * k
    # S -> k
    # V -> k * n

    compressed_size = (
        m * k
        + k
        + k * n
    )

    original_size = m * n

    compression_percentage = (
        1 - compressed_size / original_size
    ) * 100


    # -----------------------------
    # DISPLAY COMPRESSED IMAGE
    # -----------------------------

    ax = fig.add_subplot(
        gs[1, i + 1]
    )

    ax.imshow(
        ImJPG_comp,
        cmap="gray"
    )

    ax.set_title(
        f"Compressed Image\n"
        f"k = {k}\n"
        f"Compression = {compression_percentage:.2f}%"
    )

    ax.axis("off")


    # Print in console as well
    print(
        f"Compression percentage for {k} "
        f"singular values: "
        f"{compression_percentage:.2f}%"
    )


# -----------------------------
# SHOW EVERYTHING
# -----------------------------

fig.suptitle(
    "SVD Image Compression",
    fontsize=16
)

plt.tight_layout()

plt.show()
