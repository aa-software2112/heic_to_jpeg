import os
from PIL import Image
import pillow_heif  # For HEIC support

def convert_and_reduce_quality(input_path, output_path, quality=50):
  """Converts an image to JPEG and reduces its quality.

  Args:
      input_path (str): Path to the input image (HEIC or JPEG).
      output_path (str): Path to save the output JPEG.
      quality (int, optional): JPEG quality (1-95). Defaults to 50.
  """

  _, ext = os.path.splitext(input_path)
  if ext.lower() == ".heic":
      with open(input_path, "rb") as f:
          heif_file = pillow_heif.read_heif(f)
          image = Image.frombytes(
              heif_file.mode, heif_file.size, heif_file.data, "raw", heif_file.mode, heif_file.stride
          )
  else:
      image = Image.open(input_path)

  # Ensure output path has a .jpg extension
  output_path = os.path.splitext(output_path)[0] + ".jpg"

  image.save(output_path, "JPEG", quality=quality)

import glob
PATH_TO_LOAD = "FOLDER/PATH/HERE"#BARCELONA_IPHONE/*.HEIC"
PATH_TO_JPEGS = "FOLDER_PATH_HERE"
# Example usage:
images_to_convert = glob.glob(PATH_TO_LOAD)
for image_to_convert in images_to_convert:
    filename = os.path.basename(image_to_convert)
    name, _ = os.path.splitext(os.path.basename(filename))
    jpeg_output_name = name + ".jpg"
    jpeg_output_name = os.path.join(PATH_TO_JPEGS, jpeg_output_name)
    print("Converting", filename, "into", jpeg_output_name)
    convert_and_reduce_quality(image_to_convert, jpeg_output_name, quality=25)