Multimodal Content Generator (POC)
A Proof-of-Concept (POC) application to generate images, audio, music, and video from text prompts using AI models.
This project demonstrates a simple multimodal pipeline where a single text prompt can produce:
A generated image (Stable Diffusion)
A spoken audio file (Coqui TTS)
Background music (MusicGen)
A simple video combining the image and audio (MoviePy)
Text-to-Image: Generates realistic images from text using Stable Diffusion.
Text-to-Audio: Converts text prompts into spoken audio using Coqui TTS.
Text-to-Music: Generates background music using MusicGen.
Text-to-Video: Combines generated image and audio to produce a video using MoviePy.
Streamlit Frontend: Simple web interface for testing prompts and downloading outputs.

Run the Streamlit app:
streamlit run app.py