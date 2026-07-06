# VideoAI

Used for: the repository-level overview of the Phoenician pilot workflow, its scripts, and its cloud validation path.

AI-assisted pilot video project for a short documentary about Phoenician trade, ships, and Bormla's harbor role.

## What this repository is for

This repository stores the working scripts, planning files, and still-image assets for the pilot workflow. Generated MP4 clips, rough cuts, and temporary review files stay out of version control so the project can stay lightweight and cloud-friendly.

## Current workflow

1. Use `scene_prompts.txt`, `presentation_script.txt`, and the source PDF locally for planning.
2. Generate or review still assets in `pilot/assets/`, `pika/reference_frames/`, and `runway/keyframes/`.
3. Build upload clips for Pika or similar tools with `build_pika_upload_clips.py`.
4. Extract still keyframes for Runway with `extract_runway_keyframes.py`.
5. Assemble the returned final clips into a rough pilot with `build_rough_cut_from_finals.py`.
6. Keep the older still-image pilot render path available through `build_pilot.py` and `build_pilot_alive.py`.

## Key files

- `WORK_PLAN.md`: active project strategy and current scope
- `RUNWAY_UPLOAD_CHECKLIST.md`: exact upload file-to-prompt mapping
- `ASSET_MANIFEST.md`: locked clip inventory for the current pilot
- `build_pika_upload_clips.py`: builds short upload clips from still images
- `extract_runway_keyframes.py`: extracts upload keyframes from local clips
- `build_rough_cut_from_finals.py`: concatenates the selected final clips into a rough pilot
- `build_pilot.py`: renders the original still-image preview
- `build_pilot_alive.py`: renders the motion-pass still-image preview

## Requirements

- Python 3.11+
- `ffmpeg` on `PATH`

The render scripts automatically look for a usable system font. If needed, set `VIDEOAI_FONT` to a local `.ttf` file.

## Validation

```bash
python -m unittest discover -s tests
python -m py_compile build_pilot.py build_pilot_alive.py build_pika_upload_clips.py build_rough_cut_from_finals.py extract_runway_keyframes.py render_support.py
python build_pilot_alive.py
```

The GitHub Actions workflow runs the same Python validation and renders the still-image motion pilot in the cloud. The externally generated MP4 workflow remains local because those video assets are intentionally not tracked in Git.
