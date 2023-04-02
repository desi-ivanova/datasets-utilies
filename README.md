# datasets-utilies
Collection of utility scripts to do with data (download, setup, etc.)

## Video

### UVG dataset
https://uvgarment.org/download/

- UVG is a standard evaluation dataset for e.g. learnt video compression.
- `uvg/uvg_setup.py` downloads, extracts and covnerts the yuv files to png (treat videos as images).
    - you need to have `ffmpeg` installed for the yuv-to-png conversion (e.g. `brew install ffmpeg` or `sudo apt install ffmpeg`).
    - compressed (`7z`) and the unzipped yuv files are deleted.
    - total size of the unzipped image data ~16GB.

### Vimeo-90k Septuplet dataset
http://toflow.csail.mit.edu/index.html#septuplet

- Vimeo-90k is a standard training dataset for e.g. neural image compression and neural video compression, video super-resolution, frame interpolation etc.
- `viemo-90k/vimeo_setup.py` downloads and extracts the dataset, which comes in the form of png images.
    - Size of zip file is ~82GB which gets deleted after it's unzipped.
    - Total size of the unzipped data ~169GB.


## Audio
Coming.