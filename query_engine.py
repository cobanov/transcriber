from embedder import generate_embeddings
from lancedb_manager import LanceDBManager


def query_lancedb(query, db_path="lancedb", table_name="transcripts"):
    db_manager = LanceDBManager(db_path=db_path)
    embedding = generate_embeddings([query])[0]
    results = db_manager.search(table_name, embedding)
    return results
