from embedder import generate_embeddings
from lancedb_manager import LanceDBManager
from query_engine import query_lancedb
from transcriber import transcribe_audio

# 1. Transcribe Audio
audio_file_path = "example.mp3"
transcript = transcribe_audio(audio_file_path)

# 2. Generate Embeddings for the Transcript
embeddings = generate_embeddings([transcript])

# 3. Store in LanceDB
db_manager = LanceDBManager(db_path="lancedb")
db_manager.insert_data(
    table_name="transcripts", data=[{"text": transcript, "embedding": embeddings[0]}]
)

# 4. Query LanceDB
query = "Find something related to the video content"
results = query_lancedb(query)
print(results)
