# Phoenician Video Work Plan

Used for: the current project strategy, active decisions, folder structure, and what happens next.

## Goal

Create a short PDF-aligned documentary cut first, based on `scene_prompts.txt`, `presentation_script.txt`, and `Phoenician Ship in the Port of Bormla, Malta.pdf`, before attempting the full 10-minute version.

## Source Check

- `scene_prompts.txt`: original scene and visual direction
- `presentation_script.txt`: longer investor-style narration source
- `Phoenician Ship in the Port of Bormla, Malta.pdf`: the primary structure for the next edit

## Current Decision

- Move from the old 8-shot pilot to an 11-shot documentary cut.
- Reuse the strongest existing Pika and Runway clips already saved in `pika/finals/selected/`.
- Match the narration directly to the PDF sections instead of the longer investor script.
- Add narration and subtitles now that the visual sequence is effectively locked.

## Current Status

- `pika/finals/selected/` is the locked clip set for the present documentary pass.
- `pilot/output/phoenician_pilot_rough_cut.mp4` remains the older rough visual assembly.
- The uploaded clips now cover the PDF well enough for a narrated documentary cut.
- The only weaker area is page 18, which can be covered with narration plus a closing legacy card.

## Active Files

- `scene_prompts.txt`: original visual outline
- `presentation_script.txt`: longer narration source
- `RUNWAY_UPLOAD_CHECKLIST.md`: upload instructions and prompt mapping
- `PDF_EDIT_STRATEGY.md`: assembly order that maps clips to PDF sections
- `pdf_cut_narration.txt`: short narration source for the current cut
- `build_pdf_documentary.py`: assembles the PDF-aligned documentary cut with narration and subtitles

## Folder Structure

- `pika/`: generated sample videos and working area
- `pika/finals/`: returned generated final clips
- `pika/finals/selected/`: locked working clip set
- `runway/keyframes/`: image uploads for Runway generation
- `pilot/output/`: preview renders and documentary outputs

## Current Scope

- Length target: about 75 to 90 seconds
- Format: 16:9, 720p or 1080p MP4
- Style: cinematic historical documentary
- Audio: add narration now; add music only if a clean licensed track is chosen later

## Documentary Structure

1. Ocean introduction
2. Trade network fleet
3. Hero gaulos ship
4. Malta harbor approach
5. Quay loading and logistics
6. Marketplace exchange
7. Ship construction and materials
8. Trade route map
9. Bormla repair and safe-haven role
10. Night navigation
11. Underwater shipwreck evidence
12. Modern conservation
13. Closing legacy card

## Existing Coverage

- The selected clip set is complete enough for the next edit.
- `insert_trade_goods.mp4` stays optional as a cutaway insert if pacing needs it.

## Execution Steps

1. Normalize the selected clips into one documentary timeline.
2. Generate short narration from `pdf_cut_narration.txt`.
3. Build a subtitle file from the same narration timing.
4. Render a narrated documentary preview.
5. Review pacing and decide whether a modern Bormla closing shot is still needed.

## Deferred For Later

- Background music selection
- Longer 10-minute narration cut
- Optional modern-day Bormla closing footage

## Status

- Source review: complete.
- Existing Pika clip review: complete.
- Missing reference frame generation: complete.
- External generation round: complete.
- Documentary assembly: in progress.

## Next Step

- Render the narrated PDF-aligned documentary preview from the selected clip set.
