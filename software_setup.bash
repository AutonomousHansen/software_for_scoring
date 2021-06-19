# Installing brew package manager
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# # Installing Handbrake video/audio encoder
# brew install handbrake

# # Installing ffmpeg command-line audio encoder
# brew install ffmpeg

# # Installing youtube-dl youtube video downloader
# brew install youtube-dl

# Inject Bash functions into .bashrc

'function wav_to_mp3() {
for i in *.wav;
  do ffmpeg -i "$i" -vn -ar 44100 -ac 2 -b:a 192k "${i%.wav}.mp3";
done
}

alias cb_to_film="python ~/sofware_for_scoring/cb_to_film.py"
}' >> ~/.bash_profile