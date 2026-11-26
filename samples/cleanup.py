import trimesh
def cleanup(mesh, min_ratio=0.02):
  parts = mesh.split(only_watertight=False)
  if len(parts) > 1:
    biggest = max(len(p.faces) for p in parts)
    parts = [p for p in parts if len(p.faces) >= biggest * min_ratio]
    mesh = trimesh.util.concatenate(parts)
  mesh.merge_vertices()
  mesh.update_faces(mesh.nondegenerate_faces())
  mesh.remove_unreferenced_vertices()
  trimesh.repair.fill_holes(mesh)
  trimesh.repair.fix_normals(mesh)
  return mes
