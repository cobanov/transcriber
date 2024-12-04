from setuptools import find_packages, setup

setup(
    name="transcribify",
    version="0.1.0",
    description="A pipeline to transcribe audio, generate embeddings, and store/query data in LanceDB.",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    url="https://github.com/cobanov/transcribify",
    packages=find_packages(),
    install_requires=[
        "whisper",
        "sentence-transformers",
        "lancedb",
        "openai",
        "yt-dlp",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "transcribify=transcribify.cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
