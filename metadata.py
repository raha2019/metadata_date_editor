# For Image Processing
import os 
import piexif
import datetime

# For Video Processing
import subprocess

def edit_mp4_creation_time(video_path, new_creation_time, counter):
    try:
        # Create the FFmpeg command to update the metadata
        command = [
            'ffmpeg',
            '-i', video_path,
            '-metadata', 'creation_time=' + new_creation_time,
            '-codec', 'copy',
            new_path + 'output-'+ str(counter) + '.mp4'
        ]

        # Execute the command
        subprocess.run(command, check=True)
        print('Creation time updated successfully.')
    except subprocess.CalledProcessError as e:
        print('An error occurred:', e)

def modify_image_creation_date(image_path, new_creation_date):
    try:
        # Load the EXIF metadata
        exif_data = piexif.load(image_path)

        # Update the creation date
        exif_data['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_creation_date

        # Convert the updated metadata to bytes
        updated_metadata = piexif.dump(exif_data)

        # Save the updated metadata to the image
        piexif.insert(updated_metadata, image_path)

        print("Creation date updated successfully.")

    except Exception as e:
        print("An error occurred:", str(e))

def get_month(month):
    month = month.lower()
    if(month == "january"):
        return "01"
    elif (month == "february"):
        return "02"
    elif (month == "march"):
        return "03"
    elif (month == "april"):
        return "04"
    elif (month == "may"):
        return "05"
    elif (month == "june"):
        return "06"
    elif (month == "july"):
        return "07"
    elif (month == "august"):
        return "08"
    elif (month == "september"):
        return "09"
    elif (month == "october"):
        return "10"
    elif (month == "november"):
        return "11"
    elif (month == "december"):
        return "12"


path = './images/'
new_path = "./output/"

video_counter = 0 

dir_list = os.listdir(path)


print(dir_list)

for file in dir_list:
    if file.lower().endswith('.mp4'):
        # new_creation_time = "2023-03-01T12:00:00Z"
        file_name = file.split(".")[0]

        month = str(get_month(file_name.split("-")[0])) 
        day = str("{:02d}".format(int(file_name.split("-")[1])))

        new_creation_time = "2023-"+month+"-"+day+"T12:00:00Z"
        edit_mp4_creation_time(path + file, new_creation_time, video_counter)
        # os.rename(path + "output-" + str(video_counter) + ".mp4", new_path + "output-" + str(video_counter) + ".mp4")
        video_counter += 1
        print("Video has changed date: " + file)

    elif file.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_name = file.split(".")[0]

        month = str(get_month(file_name.split("-")[0]))
        day = str(file_name.split("-")[1])

        new_creation_date = "2023:" + month +":" + day + " 12:00:00"
        modify_image_creation_date(path + file, new_creation_date)
        os.rename(path + file, new_path + file)
        print("Image has changed date: " + file)

    else:
        print(file + " is not an MP4 or JPG")


