import whisper


def transcribe_audio(file_path, model_name="base"):
    model = whisper.load_model(model_name)
    result = model.transcribe(file_path)
    return result["text"]
