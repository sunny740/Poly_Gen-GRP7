# Poly_Gen-GRP7
Repo For Infotact project
## Project at glance 
Text prompt
||
[1] Text -> Image  (Stable Diffusion / SDXL-Turbo (diffusers)          
[2] Background removal     (rembg)
[3] Image -> 3D mesh (TripoSR -> raw mesh, 100k to 500k triangles)               
[4] Cleanup + Decimation   (trimesh / open3d   -> about 10k triangles (QEM))
[5] UV unwrap (xatlas)
[6] Texture (bake colours, then SD + ControlNet projection)                
[7] PBR material (roughness, metalness, normal map)          
[8] Export Format (.glb)
[9] FastAPI backend  ->  (React + react-three-fiber (Three.js) viewer)
