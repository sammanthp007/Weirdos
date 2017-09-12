#!/bin/zsh

youtube-dl -x --audio-format mp3 $1

for f in ./*.mp3
do
    mv $f audio/
done

echo "Done"
