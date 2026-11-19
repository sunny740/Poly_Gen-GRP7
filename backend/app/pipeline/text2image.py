import torch
from diffusers import AutoPipelineForText2Image
_pipe = None
def get_pipe():
global _pipe
if _pipe is None:
_pipe = AutoPipelineForText2Image.from_pretrained(
'stabilityai/sdxl-turbo', torch_dtype=torch.float16, 
variant='fp16'
).to('cuda')
return _pipe
TEMPLATE = ('{p}, single object, centered, full object visible, '
'three-quarter view, plain white background, soft studio 
lighting, '
'high detail, 3d asset reference')
def text_to_image(prompt, out_path):
image = get_pipe()(prompt=TEMPLATE.format(p=prompt),
num_inference_steps=1, guidance_scale=0.0).images[0]
image.save(out_path)
return out_path
