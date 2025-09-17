from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="outputs/images/output.png"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    ).to(device)

    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path
