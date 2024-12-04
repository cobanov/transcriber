import click

from embedder import generate_embeddings
from lancedb_manager import LanceDBManager
from query_engine import query_lancedb
from transcriber import transcribe_audio
from youtube_downloader import download_audio_from_youtube


@click.group()
def cli():
    """Transcribify CLI"""
    pass


@cli.command()
@click.argument("url")
@click.option(
    "--output_dir", default="downloads", help="Directory to save downloaded audio"
)
def download(url, output_dir):
    """Download audio from YouTube"""
    file_path = download_audio_from_youtube(url, output_dir)
    click.echo(f"Audio downloaded to: {file_path}")


@cli.command()
@click.argument("audio_file")
def transcribe(audio_file):
    """Transcribe an audio file"""
    transcript = transcribe_audio(audio_file)
    click.echo(f"Transcript:\n{transcript}")


@cli.command()
@click.argument("audio_file")
@click.option("--db_path", default="lancedb", help="Path to LanceDB database")
@click.option("--table_name", default="transcripts", help="LanceDB table name")
def process(audio_file, db_path, table_name):
    """Transcribe and store audio embeddings in LanceDB"""
    transcript = transcribe_audio(audio_file)
    embeddings = generate_embeddings([transcript])

    db_manager = LanceDBManager(db_path=db_path)
    db_manager.insert_data(
        table_name=table_name,
        data=[{"text": transcript, "embedding": embeddings[0]}],
    )
    click.echo(f"Processed and stored transcript in LanceDB: {transcript}")


@cli.command()
@click.argument("query")
@click.option("--db_path", default="lancedb", help="Path to LanceDB database")
@click.option("--table_name", default="transcripts", help="LanceDB table name")
def search(query, db_path, table_name):
    """Search transcripts in LanceDB"""
    results = query_lancedb(query, db_path=db_path, table_name=table_name)
    click.echo(f"Search Results:\n{results}")


if __name__ == "__main__":
    cli()
