# Project Reference

Used for: the final project state, the locked visual sequence, and the rebuild inputs for the short documentary.

## Final Status

- The short documentary is complete.
- The active final deliverable is `deliverables/final/phoenician_documentary_final.mp4`.
- The editable working render remains in `pilot/output/pdf_cut/`.

## Core Inputs

- `scene_prompts.txt`
- `presentation_script.txt`
- `Phoenician Ship in the Port of Bormla, Malta.pdf`
- `pdf_cut_narration.txt`
- `pika/finals/selected/`
- `audio/ambience/`
- `audio/music/bed.mp3`

## Locked Visual Sequence

1. `intro_ocean.mp4`
2. `shot01_trade_network_fleet.mp4`
3. `shot02_hero_gaulos_ship.mp4`
4. `shot03_harbor_approach.mp4`
5. `shot04_quay_loading.mp4`
6. `shot05_marketplace_exchange.mp4`
7. `shot06_ship_construction.mp4`
8. `shot07_trade_route_map.mp4`
9. `shot08_bormla_repair.mp4`
10. `shot09_night_navigation.mp4`
11. `shot10_underwater_shipwreck.mp4`
12. `shot11_modern_conservation.mp4`
13. `end_legacy`

## Coverage Note

- The current cut covers the PDF well enough for the short version.
- The only section handled more interpretively is the modern legacy ending, which is resolved through the closing card rather than a separate modern city shot.

## Rebuild Command

```bash
python build_ambience_pack.py
python build_pdf_documentary.py
```

## Historical Media

Older generation inputs and superseded source media were moved to:

- `archive/source_media/`

This includes archived Runway keyframes, older Pika source clips, upload clips, and superseded generated outputs.
