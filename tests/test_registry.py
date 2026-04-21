from __future__ import annotations

import uuid

import matplotlib as mpl
import numpy as np
import pytest
from matplotlib.colors import Colormap

from dcmcolmap import (
    get_colormap,
    list_colormaps,
    register,
    register_all,
)

ALL_NAMES = list_colormaps()


def test_list_colormaps_contains_expected():
    names = list_colormaps()
    assert "hotiron" in names
    assert "pet" in names
    assert "fall" in names
    assert "hotmetalblue" in names
    assert "pet20step" in names
    assert names == sorted(names)


@pytest.mark.parametrize("name", ALL_NAMES)
def test_get_colormap_returns_colormap(name):
    cmap = get_colormap(name)
    assert isinstance(cmap, Colormap)


@pytest.mark.parametrize("name", ALL_NAMES)
def test_colormap_values_in_unit_range(name):
    cmap = get_colormap(name)
    samples = cmap(np.linspace(0.0, 1.0, 32))
    assert samples.shape == (32, 4)
    assert np.all(samples >= 0.0) and np.all(samples <= 1.0)


def test_get_colormap_is_cached():
    assert get_colormap("pet") is get_colormap("pet")


@pytest.mark.parametrize("raw", ["PET", " pet ", "Pet", "\tPET\n"])
def test_get_colormap_is_case_and_whitespace_insensitive(raw):
    assert get_colormap(raw) is get_colormap("pet")


def test_get_colormap_invalid_name_raises():
    with pytest.raises(KeyError):
        get_colormap("not-a-real-map")


def test_register_single():
    prefix = f"test_dicom_{uuid.uuid4().hex[:8]}_"
    registered_name = register("pet", prefix=prefix)
    assert registered_name in mpl.colormaps


def test_register_collision_without_force_raises():
    prefix = f"test_dicom_{uuid.uuid4().hex[:8]}_"
    register("pet", prefix=prefix)
    with pytest.raises(ValueError):
        register("pet", prefix=prefix, force=False)


def test_register_with_force_overwrites():
    prefix = f"test_dicom_{uuid.uuid4().hex[:8]}_"
    first = register("pet", prefix=prefix)
    second = register("pet", prefix=prefix, force=True)
    assert first == second
    assert second in mpl.colormaps


def test_register_all_registers_everything():
    prefix = f"test_dicom_{uuid.uuid4().hex[:8]}_"
    names = register_all(prefix=prefix)
    assert len(names) == len(list_colormaps())
    assert all(name in mpl.colormaps for name in names)
