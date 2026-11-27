import numpy as np
from scipy.spatial import cKDTree
def bake_vertex_colors(low, high, size=1024):
uv = np.asarray(low.visual.uv, dtype=np.float64)
px = np.column_stack([uv[:, 0], 1.0 - uv[:, 1]]) * (size - 1)  # image 
rows run top to bottom
verts = np.asarray(low.vertices)
faces = np.asarray(low.faces)
colors = np.asarray(high.visual.vertex_colors)[:, :3]
tree = cKDTree(np.asarray(high.vertices))
xy_list, pos_list = [], []
for f in faces:
a, b, c = px[f]
m = np.array([[b[0] - a[0], c[0] - a[0]],
[b[1] - a[1], c[1] - a[1]]])
if abs(np.linalg.det(m)) < 1e-9:
continue
lo = np.floor(np.minimum(np.minimum(a, b), c)).astype(int)
hi = np.ceil(np.maximum(np.maximum(a, b), c)).astype(int)
xs, ys = np.meshgrid(np.arange(lo[0], hi[0] + 1), np.arange(lo[1], 
hi[1] + 1))
pts = np.column_stack([xs.ravel(), ys.ravel()]).astype(float)
uvw = np.linalg.solve(m, (pts - a).T).T
w = np.column_stack([1 - uvw.sum(axis=1), uvw])   # barycentric 
weights
inside = (w >= -1e-6).all(axis=1)
if inside.any():
  xy_list.append(pts[inside].astype(int))
pos_list.append(w[inside] @ verts[f])         
# 3D position of each pixel
xy = np.clip(np.concatenate(xy_list), 0, size - 1)
pos = np.concatenate(pos_list)
_, nearest = tree.query(pos)
img = np.zeros((size, size, 3), dtype=np.uint8)
filled = np.zeros((size, size), dtype=bool)
img[xy[:, 1], xy[:, 0]] = colors[nearest]
filled[xy[:, 1], xy[:, 0]] = True
return img, filled
