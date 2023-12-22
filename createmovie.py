# import moviepy.editor as mp
import os
import configparser
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/Users/shivi/anaconda3/lib/python3.11/site-packages/imageio_ffmpeg"
from moviepy.editor import *

import random



config = configparser.ConfigParser()
config.read('config.ini') 


voiceovers = config['Directory']['voice_overs']
screenshots = config['Directory']['screenshots']
output_dir = config['Directory']['output_directory']
video_dir = config['Directory']['video_files']




def createClip(screenShot, voiceOver, name):
    print("creating clip")
    stock_videos = [x for x in os.listdir(video_dir) if x != ".DS_Store"]
    random_stock_video = random.choice(stock_videos)
    bgVideoName = f"{video_dir}/{random_stock_video}"
    bgVideo = VideoFileClip(filename=bgVideoName, audio=False)
    audioClip = AudioFileClip(voiceOver)
    imageClip = ImageClip(screenShot, duration=5).set_position("center")
    imageClip = imageClip.resize(0.5)
    videoClip = imageClip.set_audio(audioClip)
    finalVideo = CompositeVideoClip(
        clips = [bgVideo, videoClip]
    ).set_duration(audioClip.duration)
    outputFile = f"{output_dir}/Videos/{name}.mp4"
    finalVideo.write_videofile(
        outputFile,
        audio_codec="aac",
        codec="mpeg4",
        threads=12,
        bitrate="8000k",
        )
    return videoClip


def getRandomScAndVo():
    print("getting random voice over")
    # exlucde the .DS_Store file from random choice
    voice_directories = [x for x in os.listdir(voiceovers) if x != ".DS_Store"]
    screenshot_directories = [x for x in os.listdir(screenshots) if x != ".DS_Store"]
    random_voice = random.choice(voice_directories)
    random_screenshot = random.choice(screenshot_directories)
    voiceOver = f"{voiceovers}/{random_voice}"
    screenshot = f"{screenshots}/{random_screenshot}"
    print(screenshot)
    print("here:", voiceOver)
    return screenshot, voiceOver


# randScreenShot, randVoiceOver = getRandomScAndVo()



# print(randScreenShot)
# print(randVoiceOver)

# createClip(randScreenShot, randVoiceOver, "test")


