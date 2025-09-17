from moviepy.editor import ImageClip, AudioFileClip
print("MoviePy works!")

def generate_video(image_path, audio_path, output_path="outputs/videos/output.mp4"):
    # Create a video clip from the image (5 seconds long)
    image_clip = ImageClip(image_path).set_duration(5)

    # Add audio narration
    audio_clip = AudioFileClip(audio_path)

    # Sync audio with video
    video = image_clip.set_audio(audio_clip)

    # Export video
    video.write_videofile(output_path, fps=24)
    return output_path
