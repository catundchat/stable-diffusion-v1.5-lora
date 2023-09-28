# Stable Diffusion v1.5 LoRA
Stable Diffusion v1.5 LoRA fine-tuning image generation record

## Introduction
- Stable Diffusion is a latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
- The Stable-Diffusion-v1-5 checkpoint was initialized with the weights of the Stable-Diffusion-v1-2 checkpoint and subsequently fine-tuned on 595k steps at resolution 512x512 on "laion-aesthetics v2 5+" and 10% dropping of the text-conditioning to improve classifier-free guidance sampling.

## Requirements
Local running configs
- RTX A5000
- necessary packages```pip install -r requirements.txt```

## References
1. [Stable Diffusion 微调及推理优化](https://cloud.tencent.com/developer/article/2302436)
2. [Using LoRA for Efficient Stable Diffusion Fine-Tuning](https://huggingface.co/blog/lora)
3. [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
