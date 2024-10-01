# AudiobookBuddy
For instant playback functionality, please install MPV: https://mpv.io/. You might also need to pip install mpv, edge-tts, or whatever other requirement is asked for since I already forgot what they are.

Simple edge-tts GUI with CMD interface. Just run the .py file. If you don't fill out the Filename input, clicking on generate will only play back the text/file.

When filename is left blank, instant playback will occur (as for testing the voices). When entering a filename, instant playback will not occur and instead it will be saved into the specified filename into the current directory. Do not use spaces and use the .wav or .mp3 extension. eg. my-audio-file.wav

When choosing "File", look for the search bar on the bottom of the app and make sure you select a .txt file in UTF-8 format.

Saved files should be saved in the current directory the app is run from, please change the output directory for the "Open Folder" button directly on the .py file.
