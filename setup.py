from setuptools import setup, find_packages
from pathlib import Path
import os

if __name__ == "__main__":
    with Path(Path(__file__).parent, "README.md").open(encoding="utf-8") as file:
        long_description = file.read()

    def _read_reqs(relpath):
        fullpath = os.path.join(os.path.dirname(__file__), relpath)
        with open(fullpath) as f:
            return [s.strip() for s in f.readlines() if (s.strip() and not s.startswith("#"))]

    REQUIREMENTS = _read_reqs("requirements.txt")

    setup(
        name="clip-video-encode",
        packages=find_packages(),
        include_package_data=True,
        version="1.2.0",
        license="MIT",
        description="Easily compute clip embeddings from video frames",
        long_description=long_description,
        long_description_content_type="text/markdown",
        entry_points={"console_scripts": ["clip-video-encode=clip_video_encode.cli:main"]},
        author="Maciej Kilian",
        author_email="kilianmaciej6@gmail.com",
        url="https://github.com/iejMac/clip-video-encode",
        data_files=[(".", ["README.md"])],
        keywords=["machine learning"],
        install_requires=REQUIREMENTS,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.6",
        ],
    )
