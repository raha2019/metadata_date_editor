# metadata_date_editor
Encodes files (jpgs, mp4s) with datetime metadata from their corresponding file names 

# What is this and what's included? #
These scripts have only been tested on MacOS, not sure how it would it work on Windows -- USE AT YOUR OWN RISK

metadata.py - It's a script that encodes images and videos with names like "March-10" -- Month-Day
check_meta.py - A script to read metadata data of inputted images and videos to verify that the metadata actually changed

# How/What To Install #

After downloading this repo, you must:
1. install FFMPEG on your machine
2. Create a python virtual environment in the Repository directory -- paste the following line in Terminal
   - python3 -m venv myenv
   - source myenv/bin/activate
   - pip3 install -r requirements.txt

Now Everything is setup for use

# How to Run #
1. Create two folders named "images" and "output"
2. Place your files in the folder "images"
3. Run the following command in your terminal - make sure you are in the virtual environment you setup:
  - python3 metadata.py

Everything should run as expected and now your files all have their metadata encoded with the date associated with in the file's title.
