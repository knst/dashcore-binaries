# Dash Core Binary Processor

This repo contains a tool for processing / signing dashcore binaries and creating a draft github release for that
version, and uploading those binaries.

### Using
Simply run `./process.py` or `python3 process.py`. You'll then enter the version and then if the release is a release
candidate or other beta (and you didn't create signed binaries), you'll want to say `n`

### Structure

The repo stucture should look something like this below. specifically dashpaydash should point to the repo where you 
have push permissions to the dashpay/dash github repo; and you must have the `gh` cli tool installed and setup
```
./
../
.git/
.gitignore
.idea/
18.2.0/
18.2.0-rc.1/
18.2.0-rc.2/
18.2.0-rc.3/
18.2.0-rc.4/
18.2.1/
README.md
dashpaydash@ -> ../dash
do.sh
do_release.sh
old-19.0.0-beta.1/
process.py*
venv/
```