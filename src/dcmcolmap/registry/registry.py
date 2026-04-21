from __future__ import annotations

from importlib import import_module

import matplotlib as mpl
from matplotlib.colors import Colormap

from dcmcolmap import colormaps as _colormaps_pkg

_COLORMAP_MODULES: dict[str, str] = {
    name: f"{_colormaps_pkg.__name__}.{name}" for name in _colormaps_pkg.__all__
}
_cache: dict[str, Colormap] = {}


def _extract_colormap(module_path: str) -> Colormap:
    module = import_module(module_path)
    cmap = getattr(module, "COLORMAP", None)
    if not isinstance(cmap, Colormap):
        raise RuntimeError(
            f"Module '{module_path}' must define a COLORMAP attribute "
            "of type matplotlib.colors.Colormap."
        )
    return cmap


def list_colormaps() -> list[str]:
    """List all available colormap names.

    Returns
    -------
    list of str
    """
    return sorted(_COLORMAP_MODULES.keys())


def get_colormap(name: str) -> Colormap:
    """Return a matplotlib Colormap by name.

    Parameters
    ----------
    name : str
        Case-insensitive colormap name. Call :func:`list_colormaps`
        for the full list of available names.

    Returns
    -------
    matplotlib.colors.Colormap

    Note
    ----
    The colormap is loaded lazily on first access and cached for
    subsequent calls.
    """
    key = name.strip().lower()
    if key not in _COLORMAP_MODULES:
        available = ", ".join(list_colormaps())
        raise KeyError(f"Unknown colormap '{name}'. Available: {available}")

    if key not in _cache:
        _cache[key] = _extract_colormap(_COLORMAP_MODULES[key])

    return _cache[key]


def register(name: str, *, prefix: str = "dicom_", force: bool = False) -> str:
    """Register a single colormap with matplotlib.

    Parameters
    ----------
    name : str
        Name of the colormap to register.
    prefix : str, optional
        Default: ``"dicom_"``.
    force : bool, optional
        If ``True``, overwrite an existing matplotlib colormap with the
        same registered name.

    Returns
    -------
    str
        The name which the colormap was registered with.
    """
    cmap = get_colormap(name)
    registered_name = f"{prefix}{name.strip().lower()}"

    if not force and registered_name in mpl.colormaps:
        raise ValueError(f"Colormap '{registered_name}' already exists.")

    mpl.colormaps.register(cmap, name=registered_name, force=force)
    return registered_name


def register_all(*, prefix: str = "dicom_", force: bool = False) -> list[str]:
    """Register all available colormaps with matplotlib.

    Convenience wrapper that calls :func:`register` for every name
    returned by :func:`list_colormaps`.

    Parameters
    ----------
    prefix : str, optional
        Default ``"dicom_"``.
    force : bool, optional
        If ``True``, overwrite any existing matplotlib colormaps with
        conflicting names.

    Returns
    -------
    list of str
        Registered names of all colormaps.
    """
    registered: list[str] = []
    for name in list_colormaps():
        registered.append(register(name, prefix=prefix, force=force))
    return registered
