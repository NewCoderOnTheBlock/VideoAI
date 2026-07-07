# VideoAI

Used for: the repository-level overview of the Phoenician documentary workflow, its scripts, and its final reference docs.

AI-assisted video project for a short documentary about Phoenician trade, ships, and Bormla's harbor role.

## What this repository is for

This repository stores the working scripts, final reference docs, and lightweight production metadata for the documentary workflow. Generated MP4 clips, rough cuts, and temporary review files stay out of version control so the project can stay lightweight and cloud-friendly.

## Current workflow

1. Use `scene_prompts.txt`, `presentation_script.txt`, and the source PDF locally for planning.
2. Generate or review still assets in `pilot/assets/`, `pika/reference_frames/`, and `runway/extended_cut_keyframes/`.
3. Build upload clips for Pika or similar tools with `build_pika_upload_clips.py`.
4. Extract still keyframes for Runway with `extract_runway_keyframes.py`.
5. Assemble the returned final clips into a rough pilot with `build_rough_cut_from_finals.py`.
6. Build the narrated PDF-aligned documentary cut with `build_pdf_documentary.py`.
7. Keep the older still-image pilot render path available through `build_pilot.py` and `build_pilot_alive.py`.

For the current longer no-compression revision, use:

- `runway/EXTENDED_CUT_RUNWAY_BRIEF.md`
- `pdf_cut_narration_extended_draft.txt`

## Key files

- `FINAL_PRODUCT.md`: where the finished deliverable lives and which folders still matter
- `docs/PROJECT_REFERENCE.md`: locked visual sequence and rebuild inputs
- `docs/AUDIO_REFERENCE.md`: narration, ambience, and music setup
- `docs/RUNWAY_UPLOAD_CHECKLIST.md`: archived prompt mapping for visual regeneration
- `runway/EXTENDED_CUT_RUNWAY_BRIEF.md`: active Runway shot list for the longer cut
- `pdf_cut_narration_extended_draft.txt`: active narration split for the longer cut
- `MUSIC_SOURCE.md`: the current free music bed source for the final mix
- `build_pika_upload_clips.py`: builds short upload clips from still images
- `extract_runway_keyframes.py`: extracts upload keyframes from local clips
- `build_rough_cut_from_finals.py`: concatenates the selected final clips into a rough pilot
- `build_pdf_documentary.py`: renders the narrated documentary cut with optional ambience and subtitles
- `build_ambience_pack.py`: builds shot-level ambience files from the downloaded free source clips
- `build_pilot.py`: renders the original still-image preview
- `build_pilot_alive.py`: renders the motion-pass still-image preview

## Requirements

- Python 3.11+
- `ffmpeg` on `PATH`

The render scripts automatically look for a usable system font. If needed, set `VIDEOAI_FONT` to a local `.ttf` file.

## Validation

```bash
python -m unittest discover -s tests
python -m py_compile build_pilot.py build_pilot_alive.py build_pika_upload_clips.py build_rough_cut_from_finals.py build_pdf_documentary.py extract_runway_keyframes.py render_support.py
python build_pilot_alive.py
python build_pdf_documentary.py
```

## Audio workflow

To rebuild the local curated ambience pack and final documentary cut:

```bash
python build_ambience_pack.py
python build_pdf_documentary.py
```

See:

- `docs/AUDIO_REFERENCE.md`
- `MUSIC_SOURCE.md`

The GitHub Actions workflow runs the same Python validation and renders the still-image motion pilot in the cloud. The externally generated MP4 and optional local ambience workflow remain local because those media assets are intentionally not tracked in Git.
