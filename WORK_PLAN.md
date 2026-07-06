# Phoenician Video Work Plan

Used for: the current project strategy, active decisions, folder structure, and what happens next.

## Goal
Create a short 8-shot pilot first, based on `scene_prompts.txt`, `presentation_script.txt`, and `Phoenician Ship in the Port of Bormla, Malta.pdf`, before attempting the full 10-minute version.

## Source Check
- `scene_prompts.txt`: 11-scene visual outline.
- `presentation_script.txt`: full 10-minute investor-style narration script.
- `Phoenician Ship in the Port of Bormla, Malta.pdf`: sufficient historical source for the pilot.

## Current Decision
- Use an 8-shot pilot.
- Reuse the strongest existing Pika clips where they already work.
- Use image-to-video generation for the missing shots.
- Because the free Runway path accepts images more reliably than video, use keyframes from `runway/keyframes/` for upload.
- Add narration, music, and titles only after the visual clips are locked.

## Current Status
- `pika/finals/selected/` is the locked clip set for the present pilot pass.
- `pilot/output/phoenician_pilot_rough_cut.mp4` is the current rough visual assembly at about 56 seconds.
- The current pilot is strong enough for review, but it does not yet cover every topic in the PDF.
- Cloud validation should focus on the still-image render path, while externally generated MP4 clips remain local assets.

## Active Files
- `scene_prompts.txt`: original 11-scene prompt source
- `presentation_script.txt`: full 10-minute narration source
- `RUNWAY_UPLOAD_CHECKLIST.md`: exact upload instructions and prompt mapping
- `build_pika_upload_clips.py`: creates clean 5-second upload clips
- `extract_runway_keyframes.py`: creates Runway upload images

## Folder Structure
- `pika/`: existing generated sample videos and working area
- `pika/reference_frames/`: still reference images created for missing scenes
- `pika/upload_clips/`: clean short clips prepared for image/video generation tools
- `pika/finals/`: save returned generated final clips here
- `runway/keyframes/`: image uploads for Runway free-plan generation
- `pilot/assets/`: local still assets
- `pilot/output/`: local preview renders

## Pilot Scope
- Length target: about 40 to 60 seconds
- Format: 16:9, 1080p MP4
- Style: cinematic historical documentary
- Audio: add narration and music after clip generation is complete

## 8-Shot Pilot Structure
1. Trade network fleet at sea
2. Hero Phoenician ship underway
3. Malta harbor approach
4. Quay loading and trade logistics
5. Marketplace cultural exchange
6. Ship construction / engineering
7. Animated trade route map
8. Bormla repair / safe-haven maintenance

## Existing Coverage
- Already usable:
  - `pika/boat.mp4` for Shot 1
  - `pika/biggerscaleboat.mp4` for Shot 2
  - `pika/map.mp4` for Shot 7
- Optional insert only:
  - `pika/object.mp4`
- Still need generation:
  - Shots 3, 4, 5, 6, 8

## Execution Steps
1. Upload the keyframe images from `runway/keyframes/`.
2. Use the exact matching prompts from `RUNWAY_UPLOAD_CHECKLIST.md`.
3. Save generated outputs into `pika/finals/`.
4. Review the returned clips for continuity and realism.
5. Assemble the pilot edit.
6. Add presenter voice, music, and titles after the visual sequence is approved.

## Deferred For Later
- Night navigation by stars
- Underwater archaeology
- Modern ROV science
- Full present-day Bormla legacy transition

## Status
- Source review: complete.
- Existing Pika clip review: complete.
- Missing reference frame generation: complete.
- Upload clip generation: complete.
- Runway keyframe extraction: complete.
- Ready for external generation: complete.

## Next Step
- Generate the missing shots from the files listed in `RUNWAY_UPLOAD_CHECKLIST.md`.
