# dcm-colmap

Matplotlib implementation of the DICOM colormaps defined in [NEMA DICOM PS3.6, Annex B](https://dicom.nema.org/medical/dicom/2017c/output/chtml/part06/chapter_B.html)

## Available colormaps

`fall`, `hotiron`, `hotmetalblue`, `pet`, `pet20step`, `spring`, `summer`, `winter`

## Install

```bash
pip install dcm-colmap
```

## Usage

Get a `Colormap` instance directly:

```python
import matplotlib.pyplot as plt
import numpy as np
from dcmcolmap import get_colormap

gradient = np.linspace(0, 1, 256).reshape(1, -1)
plt.imshow(gradient, aspect="auto", cmap=get_colormap("pet"))
plt.show()
```

Or register every colormap with matplotlib under a `dicom_` prefix so you can reference them by string name in matplotlib plots:

```python
import matplotlib.pyplot as plt
import numpy as np
from dcmcolmap import register_all

register_all()

gradient = np.linspace(0, 1, 256).reshape(1, -1)
plt.imshow(gradient, aspect="auto", cmap="dicom_hotiron")
plt.show()
```
