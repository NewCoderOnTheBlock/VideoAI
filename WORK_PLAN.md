# Phoenician Video Work Plan

## Goal
Create a short pilot first, based on `note.txt`, `newnote.txt`, and `Phoenician Ship in the Port of Bormla, Malta.pdf`, before attempting the full 10-minute version.

## Source Check
- `note.txt`: 11-scene visual outline.
- `newnote.txt`: full 10-minute investor-style narration script.
- `Phoenician Ship in the Port of Bormla, Malta.pdf`: sufficient historical source for the pilot.

## Current Decision
- Start with a short pilot.
- Prefer a free external AI video path only if it is realistically usable.
- Otherwise generate the pilot locally in this workspace.

## External Tool Reality Check
- Runway currently has a free plan, but it is limited: one-time credits, watermark, and image-to-video only on free.
- Luma pricing currently appears paid-only on the public pricing page.
- Kling public pricing emphasizes paid plans; its free access is not clear enough to rely on for this project.
- Result: do not block the pilot on an external service.

## Pilot Scope
- Length target: 45 to 75 seconds.
- Format: 16:9, 1080p MP4.
- Style: cinematic historical documentary.
- Content focus:
  - Scene A: Phoenician trade network at sea.
  - Scene B: harbor trade activity with cargo.
  - Scene C: Malta and Bormla as a strategic hub.
  - Scene D: Gaulos ship detail or shipbuilding craftsmanship.
- Audio: start without licensed final music unless provided by user. Build a visual pilot first.

## Execution Steps
1. Lock the pilot scene order and timing.
2. Rewrite prompts for consistency and stronger visual continuity.
3. Generate pilot key visuals locally.
4. Assemble a first animatic-style video cut with motion, transitions, and titles if needed.
5. Upgrade the pilot with scene-paired motion variants so activity changes inside the frame.
6. Review the improved pilot result before scaling to the full version.

## Assumptions Unless User Changes Them
- Use the PDF as the factual anchor.
- Keep the pilot focused on visual tone and structure, not final narration polish.
- Use local generation and editing tools available in this environment.

## Status
- Source review: complete.
- Pilot planning: complete.
- Prompt design: complete.
- Pilot key visuals: complete.
- Pilot preview video: complete.
- Pilot motion variants: complete.
- Pilot v2 motion render: complete.

## Current Outputs
- Plan file: `WORK_PLAN.md`
- Execution brief: `AGENT_BRIEF.md`
- Prompt pack: `PILOT_PROMPTS.md`
- Motion brief: `PILOT_MOTION_PLAN.md`
- Image-to-video prompts: `PILOT_VIDEO_PROMPTS.md`
- Builder script: `build_pilot.py`
- Motion builder script: `build_pilot_alive.py`
- Pilot assets: `pilot/assets/`
- Pilot preview video: `pilot/output/phoenician_pilot_preview.mp4`
- Pilot v2 video: `pilot/output/phoenician_pilot_preview_alive.mp4`

## Next Review Points
- Check whether the in-scene motion is convincing enough.
- Decide whether to keep captions on screen or move to voiceover-only.
- Decide whether to add music and narration before the full 10-minute build.
- Decide whether the next upgrade should be:
  - more human/task motion per scene
  - stronger ship movement and water interaction
  - voiceover and music integration
