cd ~/Music
cp "${1}iPod.spotdl" .
spotdl sync iPod.spotdl
cd "${1}"
rm *.mp3
cp ~/Music/*.mp3 .
python3 convert_filenames.py
python3 ipod-shuffle-4g.py -t -u -v .
echo "done."
