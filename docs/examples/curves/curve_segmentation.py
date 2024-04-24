from compas.geometry import NurbsCurve
from compas.geometry import Point
from compas_viewer import Viewer

pointsA = [Point(0, 0, 0), Point(3, 6, 0), Point(6, -3, 3), Point(10, 0, 0)]
curveA = NurbsCurve.from_points(pointsA)

curveA.segment(u=0.2, v=0.5)

print(curveA.domain)

pointsB = [Point(0, -1, 0), Point(3, 5, 0), Point(6, -4, 3), Point(10, -1, 0)]
curveB = NurbsCurve.from_points(pointsB)

segment = curveB.segmented(u=0.2, v=0.5)

print(curveB.domain)
print(segment.domain)

# ==============================================================================
# Visualisation
# ==============================================================================

viewer = Viewer()

viewer.scene.add(curveA.to_polyline(), linewidth=4, linecolor=(1, 0, 0))
viewer.scene.add(curveB.to_polyline(), linewidth=1, linecolor=(0, 0, 0))
viewer.scene.add(segment.to_polyline(), linewidth=4, linecolor=(0, 1, 0))

viewer.show()
