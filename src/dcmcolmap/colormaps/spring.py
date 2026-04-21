"""DICOM "Spring" colormap.

SOP Instance UID: 1.2.840.10008.1.5.5
Content Label: SPRING
Reference: https://dicom.nema.org/medical/dicom/2017c/output/chtml/part06/chapter_B.html#sect_B.1.5
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

_SPRING_ANCHORS = [
    [255, 0, 255],
    [255, 255, 0],
]
_SPRING_RGB = np.array(_SPRING_ANCHORS) / 255.0

COLORMAP = LinearSegmentedColormap.from_list("DICOM_SPRING", _SPRING_RGB)
