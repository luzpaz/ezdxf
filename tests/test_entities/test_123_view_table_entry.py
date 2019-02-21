# Created: 16.03.2011, 2018 rewritten for pytest
# Copyright (C) 2011-2018, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
import pytest
from ezdxf.entities.view import View


@pytest.fixture
def view():
    return View.new('FFFF', dxfattribs={
        'name': 'VIEW1',
        'flags': 0,
        'height': 1.0,
        'width': 1.0,
        'center': (0, 0),
        'direction': (0, 0, 0),
        'target': (0, 0, 0),
        'focal_length': 1.0,
        'front_clipping': 0.0,
        'back_clipping': 0.0,
        'view_twist': 0.0,
        'view_mode': 0,
    })


def test_view_attribute_access(view):
    assert view.dxf.name == 'VIEW1'
    assert view.dxf.flags == 0
    assert view.dxf.height == 1.0
    assert view.dxf.width == 1.0
    assert view.dxf.center == (0, 0)
    assert view.dxf.direction == (0, 0, 0)
    assert view.dxf.target == (0, 0, 0)
    assert view.dxf.focal_length == 1.0
    assert view.dxf.front_clipping == 0
    assert view.dxf.back_clipping == 0
    assert view.dxf.view_twist == 0
    assert view.dxf.view_mode == 0