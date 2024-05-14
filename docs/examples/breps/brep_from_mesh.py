import compas
from compas.datastructures import Mesh
from compas.geometry import Brep
from compas_viewer import Viewer

# Construct a mesh from an OBJ file
# and convert to a brep

mesh: Mesh = Mesh.from_obj(compas.get("tubemesh.obj"))
brep = Brep.from_mesh(mesh)

# =============================================================================
# Visualization
# =============================================================================

viewer = Viewer()

viewer.renderer.camera.target = [1, 1, 1]
viewer.renderer.camera.position = [1, -6, 2]

viewer.scene.add(brep, lineswidth=2, show_points=False)

viewer.show()
