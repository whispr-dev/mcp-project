#!/usr/bin/env python3
"""Pydub audio editing example"""
from pydub import AudioSegment
import os

def edit_audio():
    if not os.path.exists("song.mp3"):
        print("song.mp3 not found - creating demo info")
        return

    # Load audio
    sound = AudioSegment.from_mp3("song.mp3")
    print(f"Duration: {len(sound)}ms")

    # Extract clip (first 10 seconds)
    clip = sound[:10000]
    clip.export("clip.mp3", format="mp3")
    print("✓ Clip extracted (0-10s)")

    # Change volume
    louder = sound + 6
    louder.export("louder.mp3", format="mp3")
    print("✓ Volume increased by 6dB")

    # Fade in/out
    faded = sound.fade_in(2000).fade_out(2000)
    faded.export("faded.mp3", format="mp3")
    print("✓ Fade in/out applied")

def merge_audio(files):
    if not all(os.path.exists(f) for f in files):
        print("Not all audio files found")
        return

    combined = AudioSegment.empty()
    for f in files:
        combined += AudioSegment.from_mp3(f)

    combined.export("merged_audio.mp3", format="mp3")
    print("✓ Audio merged")

if __name__ == "__main__":
    print("Audio tools ready - provide MP3 files to test")
    # edit_audio()
    # merge_audio(['song1.mp3', 'song2.mp3'])
