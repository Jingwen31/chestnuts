import cv2
import torch
import random
import matplotlib
import numpy as np
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt


def plot_one_box(box, img, color=None, label=None, line_thickness=None):
    """
    Plots one bounding box on the image

    Parameters:
    -----------
    box: the box coordinates x1, y1, x2, y2 of the top-left and bottom-right point.
    img: array-like image.
    label: the name of the object in the bounding box.

    """
    tl = (
        line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1
    )  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1)  # filled
        cv2.putText(
            img,
            label,
            (c1[0], c1[1] - 2),
            0,
            tl / 3,
            [225, 255, 255],
            thickness=tf,
            lineType=cv2.LINE_AA,
        )


def display_image(img):
    """
    Display the image in its original size.

    Parameters:
    -----------
    img: array-like image
    """

#     dpi = matplotlib.rcParams["figure.dpi"]
    dpi = 400
    height, width, depth = img.shape

    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis("off")

    # Display the image.
    ax.imshow(img)

    plt.show()


def show_image_with_bounding_boxes(img_path, boxes, labels=None):
    img = cv2.imread(str(img_path))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for i in range(len(boxes)):
        plot_one_box(boxes[i], img, label=labels[i])

    display_image(img)