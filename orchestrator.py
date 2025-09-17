from models.text_to_image import generate_image
from models.text_to_audio import generate_audio
from models.text_to_music import generate_music
from models.text_to_video import generate_video

def run_pipeline(prompt):
    img_path = generate_image(prompt)
    audio_path = generate_audio(prompt)
    music_path = generate_music("background music " + prompt)
    video_path = generate_video(img_path, audio_path)

    return img_path, audio_path, music_path, video_path
