# Transcribify

[![PyPI version](https://badge.fury.io/py/transcribify.svg)](https://pypi.org/project/transcribify/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Transcribify** is a Python package that helps you download audio from YouTube, transcribe it using OpenAI's Whisper, generate embeddings with Sentence Transformers, and store/query data in LanceDB. Perfect for building search-enabled video and audio repositories.

## Features

- 🎥 **Download Audio**: Extract and download audio from YouTube videos.
- 📝 **Transcribe**: Convert audio files to text with OpenAI's Whisper.
- 🤖 **Generate Embeddings**: Use Sentence Transformers to create semantic embeddings of transcripts.
- 📦 **Store & Query**: Store transcripts and embeddings in LanceDB for efficient search and retrieval.
- 🔍 **Search Transcripts**: Query stored transcripts using semantic similarity.

## Installation

Install Transcribify directly from PyPI:

```bash
pip install transcribify
```

## Requirements

- Python 3.7 or higher
- Dependencies:
  - `whisper`
  - `sentence-transformers`
  - `lancedb`
  - `yt-dlp`
  - `click`

## CLI Usage

Transcribify comes with a command-line interface for easy interaction.

### 1. **Download Audio from YouTube**

```bash
transcribify download <youtube_url> --output_dir <output_directory>
```

Example:

```bash
transcribify download https://www.youtube.com/watch?v=abcd1234 --output_dir downloads
```

### 2. **Transcribe Audio**

```bash
transcribify transcribe <audio_file>
```

Example:

```bash
transcribify transcribe downloads/example.mp3
```

### 3. **Process Audio and Store in LanceDB**

```bash
transcribify process <audio_file> --db_path <path_to_db> --table_name <table_name>
```

Example:

```bash
transcribify process downloads/example.mp3 --db_path lancedb --table_name transcripts
```

### 4. **Search Transcripts in LanceDB**

```bash
transcribify search <query> --db_path <path_to_db> --table_name <table_name>
```

Example:

```bash
transcribify search "What is this video about?" --db_path lancedb --table_name transcripts
```

## Programmatic Usage

You can also use Transcribify programmatically in your Python scripts.

### Example Workflow

```python
from transcribify.youtube_downloader import download_audio_from_youtube
from transcribify.transcriber import transcribe_audio
from transcribify.embedder import generate_embeddings
from transcribify.lancedb_manager import LanceDBManager
from transcribify.query_engine import query_lancedb

# Step 1: Download audio from YouTube
audio_path = download_audio_from_youtube("https://www.youtube.com/watch?v=abcd1234")

# Step 2: Transcribe audio
transcript = transcribe_audio(audio_path)

# Step 3: Generate embeddings
embeddings = generate_embeddings([transcript])

# Step 4: Store transcript and embeddings in LanceDB
db_manager = LanceDBManager(db_path="lancedb")
db_manager.insert_data(
    table_name="transcripts",
    data=[{"text": transcript, "embedding": embeddings[0]}]
)

# Step 5: Search for transcripts
results = query_lancedb("What is this video about?", db_path="lancedb", table_name="transcripts")
print(results)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for the amazing [Whisper](https://github.com/openai/whisper) transcription model.
- Hugging Face for the [Sentence Transformers](https://www.sbert.net/).
- LanceDB for the efficient database engine for machine learning use cases.
- `yt-dlp` for YouTube audio/video downloads.
