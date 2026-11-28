import trimesh
def export_textured_glb(mesh, texture_img, out_path, material=None):
uv = mesh.visual.uv
if material is None:
material =
trimesh.visual.material.PBRMaterial(baseColorTexture=texture_img)
mesh.visual = trimesh.visual.TextureVisuals(uv=uv, material=material)
mesh.export(out_path)
return out_path
