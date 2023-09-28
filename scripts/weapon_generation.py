import torch
import os
import uuid
import requests
import socket
import sys
import socketserver
import yaml
import random
import time
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler, StableDiffusionImg2ImgPipeline, \
    EulerAncestralDiscreteScheduler
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler


model_id = "runwayml/stable-diffusion-v1-5"

time

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_attention_slicing()
pipe = pipe.to("cuda")
pipe.enable_xformers_memory_efficient_attention()
pipe.enable_model_cpu_offload()
id = str(int(time.time()))

# After training put the .bin file here
pipe.unet.load_attn_procs("D:\\weapon\\axe_output")

for i in range(10):
    prompt = "An axe featuring a blade with an aggressive curve, a lot of pink peach blossoms style patterns on the axe. Concept art and highly detailed."
    negative_prompt = "worst quality,low quality,bad quality, blurry, grainy texture, pixelated, rough edges, warped, two or more axes, complex background."
    image = pipe(prompt=prompt, negative_prompt=negative_prompt, width=640, height=512, num_inference_steps=50).images[0]
    image.save("D:\\weapon\\axe\\v1_1_{}_{}.png".format(i, id))


# whip prompt example 
# prompt = "A medium-length whip with a distinct handle and a tapering end, a lot of pink peach blossom style patterns and texture on the whip. Highly detailed, realistic."
# negative_prompt = "worst quality,low quality,bad quality,lowres, blurry, grainy texture, pixelated, rough edges, warped, hand and humanbody, cup"

# axe prompt example
# prompt = "An axe featuring a blade with an aggressive curve, a lot of pink peach blossoms style patterns on the axe. Concept art and highly detailed."
# negative_prompt = "worst quality,low quality,bad quality, blurry, grainy texture, pixelated, rough edges, warped, two or more axes."

# spear prompt example
# prompt = "A balanced and traditional spear, with a harmonious blend of blade and handle, a lot of pink peach blossom style patterns and texture on the spear. Highly detailed, realistic."
# negative_prompt = "worst quality,low quality,bad quality, blurry, grainy texture, pixelated, rough edges, warped, hand and humanbody."

# trident prompt example
# prompt = "A trident with a distinct handle and a tapering end, a lot of pink peach blossom style patterns and texture on the trident. Highly detailed, realistic."
# negative_prompt = "worst, low and bad quality, blurry, grainy texture, pixelated, rough edges, warped, two or more tridents, complex background."