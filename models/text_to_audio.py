from TTS.api import TTS

def generate_audio(prompt, output_path="outputs/audio/output.wav"):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    tts.tts_to_file(text=prompt, file_path=output_path)
    return output_path
