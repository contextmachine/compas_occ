from math import radians

from compas.geometry import Box
from compas.geometry import Plane
from compas.geometry import Rotation
from compas_viewer import Viewer

box = Box(1).to_brep()

R = Rotation.from_axis_and_angle([0, 1, 0], radians(30))
plane = Plane.worldXY()
plane.transform(R)

trimmed = box.trimmed(plane)

# =============================================================================
# Visualization
# =============================================================================

viewer = Viewer()

# viewer.view.camera.position = [2, -4, 1]
# viewer.view.camera.look_at([0, 0, 0])

# viewer.scene.add(plane, opacity=0.5)
# viewer.scene.add(trimmed, linewidth=2)
# viewer.scene.add(box, linewidth=1, show_faces=False)

viewer.show()
