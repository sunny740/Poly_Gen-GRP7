import numpy as np
import trimesh
import xatlas
def uv_unwrap(mesh):
  vmapping, indices, uvs = xatlas.parametrize(
    np.asarray(mesh.vertices, dtype=np.float32),
    np.asarray(mesh.faces, dtype=np.uint32),
  )
  vertices = np.asarray(mesh.vertices)[vmapping]
  out = trimesh.Trimesh(vertices=vertices, faces=indices, process=False)
  out.visual = trimesh.visual.TextureVisuals(uv=uvs)
  return out
