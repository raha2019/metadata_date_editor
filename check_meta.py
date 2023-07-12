# For checking videos
import subprocess
import json

def get_mp4_metadata(mp4_path):
    try:
        cmd = ['ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', mp4_path]
        output = subprocess.check_output(cmd).decode('utf-8')
        metadata = json.loads(output)
        return metadata
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        return None

# Example usage
# mp4_path = "./Why We're Reaching the Theoretical Limit of Computer Power.mp4"  # Replace with the actual MP4 file path
mp4_path = "./output/output-0.mp4"
metadata = get_mp4_metadata(mp4_path)

if metadata:
    print("MP4 metadata:")
    print(json.dumps(metadata, indent=4))
else:
    print("MP4 file not found or error occurred while retrieving metadata.")

# --------------------------------------------------

# from PIL import Image, ExifTags
# import os
# import datetime


# def get_exif_date(image_path):
#     try:
#         image = Image.open(image_path)
#         exif_data = image._getexif()

#         if exif_data is not None:
#             for tag_id, value in exif_data.items():
#                 tag_name = ExifTags.TAGS.get(tag_id, tag_id)
#                 if tag_name == "DateTimeOriginal":
#                     creation_date = datetime.datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
#                     return creation_date
#         return None
#     except Exception:
#         return None


# def check_image_metadata(image_path):
#     try:
#         file_size = os.path.getsize(image_path)
#         width, height = Image.open(image_path).size
#         image_format = Image.open(image_path).format

#         print("File Path:", image_path)
#         print("File Size:", file_size, "bytes")
#         print("Image Format:", image_format)
#         print("Dimensions:", f"{width}x{height}")

#         creation_date = get_exif_date(image_path)
#         if creation_date:
#             print("Creation Date:", creation_date)
#         else:
#             print("Creation Date not found in EXIF metadata.")

#     except FileNotFoundError:
#         print("Image file not found.")
#     except Exception as e:
#         print("An error occurred:", str(e))

# # Provide the path to the image file here
# image_path = "./images/IMG_0742.jpg"
# check_image_metadata(image_path)


