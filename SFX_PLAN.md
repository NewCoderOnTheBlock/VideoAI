# SFX Plan

Used for: the free ambient sound workflow for the narrated documentary cut.

## Folder To Use

- Drop local sound files into `audio/ambience/`

## Naming Rule

Use the exact segment key as the filename stem. Supported formats are:

- `.wav`
- `.mp3`
- `.m4a`
- `.flac`
- `.ogg`

Examples:

- `audio/ambience/intro_ocean.mp3`
- `audio/ambience/shot04_quay_loading.wav`
- `audio/ambience/shot08_bormla_repair.mp3`

If the file exists, `build_pdf_documentary.py` will:

- loop it if it is too short
- trim it to the clip duration
- add a short fade in and fade out
- mix it quietly under the narration

## Free Source Strategy

- Use `Pixabay` for ocean, wind, birds, and general coastal ambience
- Use `Mixkit` for hammering, wood impacts, ropes, workshop, and harbor labor sounds
- Only use `Freesound` if the file is clearly `CC0` or otherwise acceptable to you

## Shot Plan

1. `intro_ocean`
   - Suggested sound: soft sea wash, light wind
   - Avoid: strong crashing waves

2. `shot01_trade_network_fleet`
   - Suggested sound: open sea, mild wind
   - Avoid: birds or port noise

3. `shot02_hero_gaulos_ship`
   - Suggested sound: gentle hull creak, soft wind over water
   - Avoid: loud storm sound

4. `shot03_harbor_approach`
   - Suggested sound: shore wind, distant gulls, soft harbor water
   - Avoid: modern engines

5. `shot04_quay_loading`
   - Suggested sound: rope movement, wood knocks, light worker handling sounds
   - Avoid: metal industrial sounds

6. `shot05_marketplace_exchange`
   - Suggested sound: quiet crowd murmur, shore birds, harbor ambience
   - Avoid: intelligible modern speech

7. `shot06_ship_construction`
   - Suggested sound: low hammering on wood, timber creaks, rope strain
   - Avoid: heavy machine tools

8. `shot07_trade_route_map`
   - Suggested sound: very soft wind or almost none
   - Avoid: busy harbor effects

9. `shot08_bormla_repair`
   - Suggested sound: measured hammering, water against hull, rope motion
   - Avoid: aggressive construction noise

10. `shot09_night_navigation`
    - Suggested sound: low night wind, calm water
    - Avoid: birds, crowds, loud rigging

11. `shot10_underwater_shipwreck`
    - Suggested sound: subtle underwater wash or none
    - Avoid: bubbles, scuba gear, cinematic booms

12. `shot11_modern_conservation`
    - Suggested sound: light room tone, subtle paper or equipment handling
    - Avoid: modern office chatter

13. `end_legacy`
    - Suggested sound: none, or reuse a very light sea wind track only if you want continuity

## Build Output

After rendering, check:

- `pilot/output/pdf_cut/phoenician_pdf_documentary_subtitled.mp4`
- `pilot/output/pdf_cut/ambience_report.txt`

The ambience report tells you which shots used a sound file and which ones are still narration-only.
