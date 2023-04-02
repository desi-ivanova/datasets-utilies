# UVG dataset https://uvgarment.org/download/
# resolution 1080p, bit depth 8, format YUV, container RAW
import os
from pathlib import Path
import argparse
import urllib.request
import py7zr  # pip install py7zr

VIDEO_SHORT_NAMES = [
    "Beauty",
    "Bosphorus",
    "HoneyBee",
    "ReadySteadyGo",  # fideo name is "ReadySetGo"
    "YachtRide",
    "Jockey",
    "ShakeNDry",
]
POSTFIX = "_1920x1080_120fps_420_8bit_YUV"
ZIP_EXTENSION = "_RAW.7z"
VIDEO_EXTENSION = ".yuv"
BASE_URL = "https://ultravideo.fi/video/"


def download_uvg_dataset(path: Path) -> None:
    path.mkdir(exist_ok=True, parents=True)
    for short_name in VIDEO_SHORT_NAMES:
        short_name = "ReadySetGo" if short_name == "ReadySteadyGo" else short_name
        zip_video_name = f"{short_name}{POSTFIX}{ZIP_EXTENSION}"
        url = BASE_URL + zip_video_name
        filename = path / zip_video_name
        if not os.path.exists(filename):
            print("Downloading ", url)
            urllib.request.urlretrieve(url, filename)
            print("Download complete!")
        else:
            print(f"{zip_video_name} already downloaded")


def extract_uvg_dataset(path: Path) -> None:
    for short_name in VIDEO_SHORT_NAMES:
        video_name = f"{short_name}{POSTFIX}{VIDEO_EXTENSION}"  # ReadySteadyGo.yuv
        # if not extracted, the name of the Zip file is 'ReadySetGo'
        short_name = "ReadySetGo" if short_name == "ReadySteadyGo" else short_name
        zip_video_name = path / f"{short_name}{POSTFIX}{ZIP_EXTENSION}"

        if video_name in os.listdir(path):
            print(f"{video_name} already extracted")
            continue
        else:
            print("Extracting ", zip_video_name)
            with py7zr.SevenZipFile(zip_video_name, "r") as zip_ref:
                zip_ref.extractall(path)
            print("Extraxtion complete!")


def convert_uvg_dataset_to_png(path: Path) -> None:
    for short_name in VIDEO_SHORT_NAMES:
        video_name = f"{short_name}{POSTFIX}{VIDEO_EXTENSION}"
        saveroot = path / f"images/{short_name}"
        saveroot.mkdir(exist_ok=True, parents=True)
        savepath = saveroot / "im%03d.png"
        sys_call = (
            f"ffmpeg -y -pix_fmt yuv420p -s 1920x1080 -i "
            f"{path}/{video_name} {savepath}"
        )
        print(sys_call)
        os.system(sys_call)


# delete the .yuv files, .7z, copyright files
def delete_yuv_and_7z(path: Path) -> None:
    for short_name in VIDEO_SHORT_NAMES + ["ReadySetGo"]:
        video_name = f"{short_name}{POSTFIX}{VIDEO_EXTENSION}"
        zip_video_name = f"{short_name}{POSTFIX}{ZIP_EXTENSION}"
        for name in [video_name, zip_video_name]:
            try:
                os.remove(path / name)
            except FileNotFoundError:
                pass


def main(download_path):
    download_path = Path(download_path).expanduser()
    download_uvg_dataset(download_path)
    extract_uvg_dataset(download_path)
    convert_uvg_dataset_to_png(download_path)
    delete_yuv_and_7z(download_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # set the default path to the current directory
    parser.add_argument(
        "--download-path", type=str, default=".", help="Path to download data"
    )
    arg = parser.parse_args()
    main(download_path=arg.download_path)
