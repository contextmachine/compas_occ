from compas.geometry import Ellipse
from compas.geometry import Line
from compas.geometry import NurbsCurve
from compas.itertools import pairwise
from compas_viewer import Viewer

ellipse = Ellipse(2.0, 1.0)
curve = NurbsCurve.from_ellipse(ellipse)

# ==============================================================================
# Visualisation
# ==============================================================================

viewer = Viewer()

viewer.scene.add(curve.to_polyline(), linewidth=3)
# viewer.scene.add(Collection(curve.points), pointsize=20, pointcolor=(1, 0, 0))

for a, b in pairwise(curve.points):
    viewer.scene.add(Line(a, b), linewidth=1, linecolor=(0.3, 0.3, 0.3))

viewer.show()
