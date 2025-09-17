import torch
from transformers import AutoProcessor, MusicgenForConditionalGeneration
import soundfile as sf

def generate_music(prompt, output_path="outputs/music/output.wav"):
    # Load model and processor
    processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")

    # Prepare input
    inputs = processor(text=[prompt], return_tensors="pt")

    # Generate audio (approx. 10s clip)
    audio_values = model.generate(**inputs, max_new_tokens=256)

    # Save as WAV
    sf.write(output_path, audio_values[0, 0].numpy(), samplerate=32000)
    return output_path
