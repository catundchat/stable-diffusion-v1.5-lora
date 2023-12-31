# Stable Diffusion v1.5 LoRA
Stable Diffusion v1.5 LoRA fine-tuning weapon image generation record (axe, spear, trident, whip)

Stable Diffusion v1.5经LoRA方法微调后生成武器图片实录（斧子，长矛，三叉戟，鞭子）

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
- Packages installed : `pip install -r requirements.txt`

## Process
Here I chose Stable Diffusion v1.5 as the base model and collected different weapon images as dataset(axe, spear, trident and whip). After training, the model could generate 4 kinds of weapons with pink blossom patterns on them.

### Data collection
In the `dataset/axe` folder, the axe images for training were uploaded as an example. For each kind of weapon, 100 photos were collected then labeled in `metadata.jsonl`. I preferred images with different backgrounds, lighting conditions, angles, and perspectives to make the model more robust and versatile, so I used Photoshop to simplify some complex backgrounds including watermarks and some strange lines.

### Model
The model is on huggingface [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5). 

v1-5-pruned.ckpt - 7.7GB, ema+non-ema weights. uses more VRAM - suitable for fine-tuning is needed.


### Training
Using `train_text_to_image_lora.py`, I trained the model with the following commands:
```
accelerate launch train_text_to_image_lora.py `
  --pretrained_model_name_or_path="D:\models--runwayml--stable-diffusion-v1-5" `
  --resolution=512 --center_crop --random_flip `
  --train_batch_size=1 `
  --gradient_accumulation_steps=4 `
  --gradient_checkpointing `
  --mixed_precision="fp16" `
  --max_train_steps=15000 `
  --learning_rate=1e-05 `
  --max_grad_norm=1 `
  --lr_scheduler="constant" --lr_warmup_steps=0 `
  --output_dir="D:\weapon\axe_output" `
  --num_train_epochs=600 `
  --train_data_dir="D:\weapon\axe"
```
After 15000 steps which took about 2.5h in my environment, I got the output `pytorch_lora_weights.bin`

### Weapon images generation
Using `weapon_generation.py`, after setting up img_num, prompt, negative_prompt, width, height and other parameters, the weapon images are generated under `img` folder. Here is some axe generations.

![merge002.png](img/merge002.png)

## PS:Animal photo generation

### Intro
Training sdv1.5 to generate particular style animal photos according to artists's works.

### Datasets
10 pictures from Artist Lee Sangsoo in `dataset/animal`

### Parameters
Using `train_text_to_image_lora.py`, I trained the model with the following commands:
```
accelerate launch train_text_to_image_lora.py `
  --pretrained_model_name_or_path="D:\models--runwayml--stable-diffusion-v1-5" `
  --resolution=512 --center_crop --random_flip `
  --train_batch_size=2 `
  --gradient_accumulation_steps=2 `
  --gradient_checkpointing `
  --mixed_precision="fp16" `
  --max_train_steps=1500 `
  --learning_rate=5e-06 `
  --max_grad_norm=0.5 `
  --lr_scheduler="constant" --lr_warmup_steps=0 `
  --output_dir="D:\weapon\animal_output_v1" `
  --num_train_epochs=50 `
  --train_data_dir="D:\weapon\animal"
```
After 1500 steps which took about 0.5h in my env, I got the output file `pytorch_lora_weights.safetensors`

### Examples
Here is some relevant photo generation of it.

Dragon:

![dragon](img2/dragon.png)

Bird:

![bird1](img2/bird1.png)
![bird2](img2/bird2.png)
![bird3](img2/bird3.png)

## References
1. [Stable Diffusion 微调及推理优化](https://cloud.tencent.com/developer/article/2302436)
2. [Using LoRA for Efficient Stable Diffusion Fine-Tuning](https://huggingface.co/blog/lora)
3. [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
