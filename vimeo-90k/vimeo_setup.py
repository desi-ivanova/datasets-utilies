import os
from pathlib import Path
import argparse
import urllib.request
import zipfile

# http://toflow.csail.mit.edu/index.html#septuplet
SEPTUPLET_URL = "http://data.csail.mit.edu/tofu/dataset/vimeo_septuplet.zip"
SEPTUPLET_FILENAME = "vimeo_septuplet.zip"


def download_vimeo_dataset(path: Path) -> None:
    path.mkdir(exist_ok=True, parents=True)
    filename = path / SEPTUPLET_FILENAME
    if not os.path.exists(filename):
        print("Downloading ", SEPTUPLET_URL)
        urllib.request.urlretrieve(SEPTUPLET_URL, filename)
        print("Download complete!")
    else:
        print(f"{filename} already downloaded")


def extract_vimeo_dataset(path: Path) -> None:
    # unzip the zipped file that was downloaded
    # https://stackoverflow.com/questions/3451111/unzipping-files-in-python
    if SEPTUPLET_FILENAME[:-4] in os.listdir(path):
        print(f"{SEPTUPLET_FILENAME[:-4]} already extracted")
        return
    with zipfile.ZipFile(path / SEPTUPLET_FILENAME, "r") as zip_ref:
        print("Extracting ", SEPTUPLET_FILENAME)
        zip_ref.extractall(path)
    print("Extraxtion complete!")


def delete_zip(download_path):
    os.remove(download_path / SEPTUPLET_FILENAME)


def main(download_path):
    download_path = Path(download_path).expanduser()
    download_vimeo_dataset(download_path)
    extract_vimeo_dataset(download_path)
    delete_zip(download_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # set the default path to the current directory
    parser.add_argument(
        "--download-path", type=str, default=".", help="Path to download data"
    )
    arg = parser.parse_args()
    main(download_path=arg.download_path)
