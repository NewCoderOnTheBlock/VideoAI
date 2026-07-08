Used for: the `v3` rebuild handoff, including why the pacing changed before, what was fixed, and which scenes still benefit most from longer or better-motion source footage.

# V3 Cut Plan

## What Changed In V3

- All narration now uses `en-GB-SoniaNeural` only.
- TTS fallback is disabled by default, so the build fails instead of switching voice mid-video.
- Narration is no longer sped up to fit short clips.
- Short clips are extended to fit the spoken line, using held final frames where needed.
- The `v2` script remains in place because it covers the stronger historical details.

## Why V2 Sounded Wrong

- `v2` started with `edge-tts` and then silently fell back to Windows SAPI.
- Several lines were compressed with `atempo`, which changed speaking pace shot by shot.

## Scenes That Needed Extension In V3

These are the segments where the spoken line was longer than the source clip:

- `intro_ocean`: clip `5.03s`, target `7.91s`, extended `2.88s`
- `shot01_trade_network_fleet`: clip `5.03s`, target `7.74s`, extended `2.71s`
- `insert_trade_goods_detail`: clip `8.08s`, target `8.34s`, extended `0.26s`
- `shot02_hero_gaulos_ship`: clip `5.03s`, target `6.02s`, extended `0.98s`
- `shot04_quay_loading`: clip `8.08s`, target `8.49s`, extended `0.40s`
- `shot05_marketplace_exchange`: clip `8.08s`, target `9.95s`, extended `1.87s`
- `shot06_ship_construction`: clip `7.08s`, target `8.30s`, extended `1.21s`
- `shot07_trade_route_map`: clip `5.03s`, target `6.50s`, extended `1.46s`
- `shot08_bormla_repair`: clip `8.08s`, target `8.99s`, extended `0.91s`
- `shot09_night_navigation`: clip `6.08s`, target `9.38s`, extended `3.29s`
- `shot11_modern_conservation`: clip `6.08s`, target `8.51s`, extended `2.43s`
- `end_legacy`: card `4.00s`, target `8.13s`, extended `4.13s`

## Best Candidates For Better Source Footage

These are the scenes where a longer or more animated replacement would improve `v3` the most:

- `intro_ocean`
- `shot01_trade_network_fleet`
- `shot05_marketplace_exchange`
- `shot09_night_navigation`
- `shot11_modern_conservation`
- `end_legacy`

## Runway Note

- Runway footage was not removed completely.
- `v3` still uses Runway-derived shots in the core sequence.
- The three insert replacements remained non-Runway because the original insert exports had visible branding and were weaker than the clean substitutes.

## Current Best Deliverable

- `deliverables/final/phoenician_documentary_final_v3.mp4`
