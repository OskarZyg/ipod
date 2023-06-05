# ipod
Useful scripts for the iPod shuffle (4th generation) to sync with spotify.
Barebones, but a WIP.

### Limitations
* assumes your `~/Music` folder
* vulnerable to people writing malicious code to your ipod
* a pita to set up, but should take less than 10 mins

## Setup
> Warning: In this setup, python scripts are executed off the ipod. This is a security risk if you let people you don't trust access it's filesystem.

Firstly, clone this repository with `git clone --recurse-submodules `, adding the repo url to the end

### Dependencies
`apt-get install python3 python3-mutagen libttspico*`
`pip install spotdl`


### Local Setup

1. symlink `ipodsync.sh` to a location where you can access it quickly
2. make sure the `~/Music` folder exists.

### iPod Setup

1. format the ipod with iTunes (on Windows or macOS)
2. copy the `convert_filenames.py` file into the iPod's root directory
3. copy the `ipod_tools/ipod-shuffle-4g.py` file into the iPod's root directory
4. run `spotdl sync <url_to_your_playlist> /path/to/ipod/iPod.spotdl` and let it run

## Usage
run `ipodsync.sh /path/to/ipod`
