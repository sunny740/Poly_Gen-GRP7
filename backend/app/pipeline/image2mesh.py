import sys
import numpy as np
import torch
import rembg
from PIL import Image
sys.path.append('third_party/TripoSR')   # make this configurable in 
config.py
from tsr.system import TSR
from tsr.utils import remove_background, resize_foreground
_model = None  # load once, reuse (loading is slow)
def get_model(device='cuda'):
    global _model
    if _model is None:
        _model = TSR.from_pretrained(
            'stabilityai/TripoSR',
            config_name='config.yaml',
            weight_name='model.ckpt',
        )
        _model.renderer.set_chunk_size(8192)
        _model.to(device)
    return _model
def image_to_mesh(image_path, out_path, resolution=256, device='cuda'):
    model = get_model(device)
    session = rembg.new_session()
    image = remove_background(Image.open(image_path), session)
    image = resize_foreground(image, 0.85)
    arr = np.array(image).astype(np.float32) / 255.0
    arr = arr[:, :, :3] * arr[:, :, 3:4] + (1 - arr[:, :, 3:4]) * 0.5
    image = Image.fromarray((arr * 255).astype(np.uint8))
    with torch.no_grad():
      scene_codes = model([image], device=device)
    mesh = model.extract_mesh(scene_codes, True, resolution=resolution)[0]
    mesh.export(out_path)
    return out_path
