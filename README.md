# mvgen

A music video generator based on beat patterns

Built with [essentia](https://github.com/MTG/essentia) audio analysis, [moviepy](https://github.com/Zulko/moviepy) Python video editing, and [tesseract](https://github.com/tesseract-ocr/tesseract) OCR

## Strategy

1 - Provide an audio file and a set of video files.

2 - Perform rhythm analysis and extract beat intervals from the audio.

3 - Generate a set of random video segments from the video files, with durations corresponding to the durations of the beat intervals. Discard and replace segments with scene changes, solid colors or very dark scenes, and detectable text (e.g. credits).

4 - Combine all the segments in order, overlay the audio, and output the resulting music video.

5 - Save a reusable spec file detailing the structure of the music video. 

6 - Optionally output all the video segments that compose the music video, so that users can edit and compose the music video elsewhere.

Note: The audio should have a sample rate of 44.1 KHz for accurate rhythm analysis via essentia. 

## Installation (Mac OS X)

**1 - [Install Miniconda](http://conda.pydata.org/miniconda.html) (A Python virtual environment and package manager)**

**2 - [Install Homebrew](http://brew.sh/) (General purpose package manager for mac)**

**3 - Add homebrew to top of path in `~/.bash_profile`**

```
#Homebrew
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

**4 - [Install tesseract >= 3.04](https://github.com/tesseract-ocr/tesseract) via Homebrew8**

`brew install tesseract --with-all-languages`

**5 - Create mvgen virtual environment**

`conda env create -f environment.yml`

**6 - Activate mvgen environment**

`source activate mvgen`

**7 - Update Xcode to most recent version**

**8 - [Install essentia >= 2.1](https://github.com/MTG/essentia) via Homebrew**

```
brew tap MTG/essentia
brew install essentia 
```

**9 - Move essentia package from Homebrew to your mvgen conda environment**

`cp -r /usr/local/lib/python2.7/site-packages/essentia /Users/myuser/miniconda/envs/mvgen/lib/python2.7/site-packages/essentia`

**10 - [Fix matplotlib](http://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python)**

`echo "backend : TkAgg" > ~/.matplotlib/matplotlibrc`

**11 - Download [scherroman/moviepy](https://github.com/scherroman/moviepy) from github (forked from [Zulko/moviepy](https://github.com/Zulko/moviepy) with added fix [#225](https://github.com/Zulko/moviepy/pull/225)).**

**12 - Install moviepy into mvgen conda environment (from downloaded moviepy directory)**

`(sudo) python setup.py install`

## Examples

**Get Help Menu**

```
python make_music_video.py --help
python make_music_video.py create --help
python make_music_video.py recreate --help
```

**Run generator with file selection dialog**

`python make_music_video.py create`

**Run generator with file inputs via terminal**

`python make_music_video.py create -a ~/Documents/mp3s/MACINTOSH\ PLUS\ -\ リサフランク420\ -\ 現代のコンピュー.mp3 -v /Volumes/Media_Drive/Movies/Timescapes/TimeScapes.2012.1080p.mkv`

