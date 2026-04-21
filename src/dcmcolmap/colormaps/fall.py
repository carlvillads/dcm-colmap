"""DICOM "Fall" colormap.

SOP Instance UID: 1.2.840.10008.1.5.7
Content Label: FALL
Reference: https://dicom.nema.org/medical/dicom/2017c/output/chtml/part06/chapter_B.html#sect_B.1.7
"""

import numpy as np
from matplotlib.colors import LinearSegmentedColormap

_FALL_ANCHORS = [[255, 255, 0], [255, 0, 0]]
_FALL_RGB = np.array(_FALL_ANCHORS) / 255.0

COLORMAP = LinearSegmentedColormap.from_list("DICOM_FALL", _FALL_RGB)
