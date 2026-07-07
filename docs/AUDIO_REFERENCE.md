# Audio Reference

Used for: the final narration, ambience, and music setup for the documentary cut.

## Current Voice

- Engine: `edge-tts`
- Voice: `en-GB-SoniaNeural`
- Rate: `-8%`
- Pitch: `-14Hz`

## Current Music Bed

- Track: `Vastness`
- Artist: `Andrew Ev`
- Local file: `audio/music/bed.mp3`
- Source and license notes: see `MUSIC_SOURCE.md`

## Current Ambience Sources

The curated ambience pack is built from Mixkit source clips stored in:

- `audio/mixkit_sources/`

Shot-level ambience files are stored in:

- `audio/ambience/`

## Active Ambience Coverage

- `intro_ocean`
- `shot01_trade_network_fleet`
- `shot02_hero_gaulos_ship`
- `shot03_harbor_approach`
- `shot04_quay_loading`
- `insert_trade_goods_detail`
- `shot05_marketplace_exchange`
- `shot06_ship_construction`
- `insert_gaulos_broadside_hull`
- `shot07_trade_route_map`
- `insert_cultural_influence_map`
- `shot08_bormla_repair`
- `shot09_night_navigation`
- `shot10_underwater_shipwreck`

These remain narration-only unless you add new ambience files:

- `shot11_modern_conservation`
- `end_legacy`

## Build Outputs

After rendering, check:

- `pilot/output/pdf_cut/phoenician_pdf_documentary_subtitled.mp4`
- `pilot/output/pdf_cut/phoenician_pdf_documentary_narration.wav`
- `pilot/output/pdf_cut/phoenician_pdf_documentary.srt`
- `pilot/output/pdf_cut/ambience_report.txt`
- `pilot/output/pdf_cut/music_report.txt`

## Optional Future Changes

- Replace the narration voice with a recorded voiceover
- Replace the music bed with a different licensed track
- Add ambience for the conservation or ending shots
