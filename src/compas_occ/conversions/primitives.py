from typing import Type

from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Line
from compas.geometry import Frame

from OCC.Core.gp import gp_Ax3
from OCC.Core.gp import gp_Pnt
from OCC.Core.gp import gp_Vec
from OCC.Core.gp import gp_Dir
from OCC.Core.gp import gp_Lin


def compas_point_to_occ_point(self: Point) -> gp_Pnt:
    """Convert a COMPAS point to an OCC point.

    Parameters
    ----------
    self : :class:`compas.geometry.Point`
        The COMPAS point to convert.

    Returns
    -------
    gp_Pnt

    """
    return gp_Pnt(* self)


def compas_point_from_occ_point(cls: Type[Point], point: gp_Pnt) -> Point:
    """Construct a COMPAS point from an OCC point.

    Parameters
    ----------
    cls : Type[:class:`compas.geometry.Point`]
        The type of COMPAS point.
    point : gp_Pnt
        The OCC point.

    Returns
    -------
    :class:`compas.geometry.Point`

    """
    return cls(point.X(), point.Y(), point.Z())


def compas_vector_to_occ_vector(self: Vector) -> gp_Vec:
    """Convert a COMPAS vector to an OCC vector.

    Parameters
    ----------
    self : :class:`compas.geometry.Vector`
        The COMPAS vector to convert.

    Returns
    -------
    gp_Vec

    """
    return gp_Vec(* self)


def compas_vector_from_occ_vector(cls: Type[Vector], vector: gp_Vec) -> Vector:
    """Construct a COMPAS vector from an OCC vector.

    Parameters
    ----------
    cls : Type[:class:`compas.geometry.Vector`]
        The type of COMPAS vector.
    vector : gp_Vec
        The OCC vector.

    Returns
    -------
    :class:`compas.geometry.Vector`

    """
    return cls(vector.X(), vector.Y(), vector.Z())


def compas_vector_to_occ_direction(self: Vector) -> gp_Dir:
    """Convert a COMPAS vector to an OCC direction.

    Parameters
    ----------
    self : :class:`compas.geometry.Vector`
        The COMPAS vector to convert.

    Returns
    -------
    gp_Dir

    """
    return gp_Dir(* self)


def compas_vector_from_occ_direction(cls: Type[Vector], vector: gp_Dir) -> Vector:
    """Construct a COMPAS vector from an OCC direction.

    Parameters
    ----------
    cls : Type[:class:`compas.geometry.Vector`]
        The type of COMPAS vector.
    vector : gp_Dir
        The OCC direction.

    Returns
    -------
    :class:`compas.geometry.Vector`

    """
    return cls(vector.X(), vector.Y(), vector.Z())


def compas_line_to_occ_line(self: Line) -> gp_Lin:
    """Convert a COMPAS line to an OCC line.

    Parameters
    ----------
    self : :class:`compas.geometry.Line`
        The COMPAS line to convert.

    Returns
    -------
    gp_Lin

    """
    return gp_Lin(compas_point_to_occ_point(self.start), compas_vector_to_occ_direction(self.direction))


def compas_frame_from_occ_position(cls: Type[Frame], position: gp_Ax3) -> Frame:
    """Construct a COMPAS frame from an OCC position.

    Parameters
    ----------
    cls : Type[:class:`compas.geometry.Frame`]
        The type of COMPAS frame.
    position : gp_Ax3
        The OCC position.

    Returns
    -------
    :class:`compas.geometry.Frame`

    """
    return cls(
        compas_point_from_occ_point(Point, position.Location()),
        compas_vector_from_occ_direction(Vector, position.XDirection()),
        compas_vector_from_occ_direction(Vector, position.YDirection())
    )
