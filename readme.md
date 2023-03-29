# PRACTISE ABOUT HOW TO MAKE AUTO-SUBTITLE AND TRANSLATOR

## auto-subtitle
[auto-subtitle](https://github.com/m1guelpf/auto-subtitle)：uses ffmpeg and OpenAI's Whisper to automatically generate and overlay subtitles on any video.
### cracks
After installing the package ,something was wrong:
`ffmpeg._run.Error: ffmpeg error (see stderr output for detail) `

With the guide of **chatgpt** ,I finally deal it by using `subprocess.run()`

[Click here](auto-subtitle\test.py)

## subtitle translate

I find this tool in weibo :[Subtitle Translator](https://github.com/gnehs/subtitle-translator-electron)

But I think it is not perfect cuz it generated sentences repeatly.But it is the best tool for translate srt freely.