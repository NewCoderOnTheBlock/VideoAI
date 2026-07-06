# VideoAI

AI-assisted pilot video project for a short film about Phoenician trade and maritime reach.

## Current scope

This repository contains a short pilot that demonstrates the visual direction before expanding into the planned 10-minute version. The current pass focuses on making scenes feel more alive through internal motion, not only camera pan and zoom.

## Key files

- `build_pilot.py`: renders the first preview from the base scene images
- `build_pilot_alive.py`: renders the stronger motion pass by alternating matched scene variants
- `pilot/assets/`: generated still frames and their action variants
- `pilot/output/`: generated preview location after a local render
- `note.txt` and `newnote.txt`: source planning material for the short and long versions

## Requirements

- Python 3.11+
- `ffmpeg` available on `PATH`

The scripts look for a font automatically on Windows, Linux, and macOS. If needed, set `VIDEOAI_FONT` to an installed `.ttf` file.

## Usage

```bash
python -m unittest discover -s tests
python build_pilot_alive.py
```

The second command writes the preview video to `pilot/output/phoenician_pilot_preview_alive.mp4`.

## Cloud build

GitHub Actions validates the Python code, renders the motion pilot in the cloud, and uploads the generated MP4 as a workflow artifact for download.
