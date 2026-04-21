"""DICOM "Winter" colormap.

SOP Instance UID: 1.2.840.10008.1.5.8
Content Label: WINTER
Reference: https://dicom.nema.org/medical/dicom/2017c/output/chtml/part06/chapter_B.html#sect_B.1.8
"""

from matplotlib.colors import LinearSegmentedColormap

_cdict_winter = {
    "red": [
        (0.0, 0.0, 0.0),
        (127 / 255.0, 0.0, 0.0),
        (1.0, 127 / 255.0, 127 / 255.0),
    ],
    "green": [(0.0, 0.0, 0.0), (1.0, 255 / 255.0, 255 / 255.0)],
    "blue": [(0.0, 255 / 255.0, 255 / 255.0), (1.0, 128 / 255.0, 128 / 255.0)],
}

COLORMAP = LinearSegmentedColormap("DICOM_WINTER", _cdict_winter)  # type: ignore[arg-type]
