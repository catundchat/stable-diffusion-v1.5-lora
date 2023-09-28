# Stable Diffusion v1.5 LoRA
Stable Diffusion v1.5 LoRA fine-tuning weapon image generation record

![merge001.png](img/merge001.png)

## Introduction
- Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input. The Stable-Diffusion-v1-5 checkpoint was initialized with the weights of the Stable-Diffusion-v1-2 checkpoint and subsequently fine-tuned on 595k steps at resolution 512x512 on "laion-aesthetics v2 5+" and 10% dropping of the text-conditioning to improve classifier-free guidance sampling.
- LoRA : Low rank adaptation of LLMs or Stable Diffusion models, which is a training technique to fine tune these models while maintain manageable file sizes. It applies smaller changes to standard checkpoint models, resulting in a reduced file size about 2-500MB, much smaller than checkpoint size(about 5GB)

## Requirements
Local running configs
- Windows 10 system
- RTX A5000(VRAM 24G)
- PyTorch : 2.0.1+cu118
- CUDA : 11.8
- Python 3.10.6
- necessary packages`pip install -r requirements.txt`

## References
1. [Stable Diffusion 微调及推理优化](https://cloud.tencent.com/developer/article/2302436)
2. [Using LoRA for Efficient Stable Diffusion Fine-Tuning](https://huggingface.co/blog/lora)
3. [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
