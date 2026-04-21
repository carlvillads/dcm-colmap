"""DICOM "Summer" colormap.

SOP Instance UID: 1.2.840.10008.1.5.6
Content Label: SUMMER
Reference: https://dicom.nema.org/medical/dicom/2017c/output/chtml/part06/chapter_B.html#sect_B.1.6
"""

from matplotlib.colors import LinearSegmentedColormap

_cdict_summer = {
    "red": [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0)],
    "green": [(0.0, 255 / 255.0, 255 / 255.0), (1.0, 128 / 255.0, 128 / 255.0)],
    "blue": [
        (0.0, 0.0, 0.0),
        (127 / 255.0, 0.0, 0.0),
        (1.0, 254 / 255.0, 254 / 255.0),
    ],
}

COLORMAP = LinearSegmentedColormap("DICOM_SUMMER", _cdict_summer)  # type: ignore[arg-type]
