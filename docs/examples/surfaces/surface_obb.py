from math import radians

from compas.colors import Color
from compas.geometry import NurbsSurface
from compas.geometry import Point
from compas.geometry import Polyline
from compas.geometry import Rotation
from compas.geometry import Translation
from compas_viewer import Viewer

points = [
    [Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0), Point(4, 0, 0)],
    [Point(0, 1, 0), Point(1, 1, 2), Point(2, 1, 2), Point(3, 1, 0), Point(4, 1, 0)],
    [Point(0, 2, 0), Point(1, 2, 2), Point(2, 2, 2), Point(3, 2, 0), Point(4, 2, 0)],
    [Point(0, 3, 0), Point(1, 3, 0), Point(2, 3, 0), Point(3, 3, 0), Point(4, 3, 0)],
]

surface = NurbsSurface.from_points(points=points)

T = Translation.from_vector([0, -1.5, 0])
R = Rotation.from_axis_and_angle([0, 0, 1], radians(45))

surface.transform(R * T)

# ==============================================================================
# OBB
# ==============================================================================

box = surface.obb()

# ==============================================================================
# Visualisation
# ==============================================================================

viewer = Viewer()

viewer.scene.add(surface)
viewer.scene.add(box, show_faces=False)

# control polygon

points = list(surface.points)
viewer.scene.add([Polyline(row) for row in points], linewidth=1, linecolor=Color(0.3, 0.3, 0.3))
viewer.scene.add([Polyline(col) for col in zip(*points)], linewidth=1, linecolor=Color(0.3, 0.3, 0.3))
viewer.scene.add(points, pointsize=10)

# isocurves

u_curves = []
for u in surface.space_u(7):  # type: ignore
    u_curves.append(surface.isocurve_u(u).to_polyline())

v_curves = []
for v in surface.space_v(7):  # type: ignore
    v_curves.append(surface.isocurve_v(v).to_polyline())

viewer.scene.add(u_curves, linecolor=Color(0.8, 0.8, 0.8), linewidth=3)
viewer.scene.add(v_curves, linecolor=Color(0.8, 0.8, 0.8), linewidth=3)

viewer.show()
