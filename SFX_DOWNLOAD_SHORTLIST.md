# SFX Download Shortlist

Used for: the first five ambience files to download before doing a larger sound pass.

## Why These Five First

These five cover the most noticeable gaps in the current cut:

1. sea atmosphere at the start
2. harbor arrival realism
3. worker activity on the quay
4. shipbuilding texture
5. repair-harbor texture

If you only download these first, the documentary will already feel much more alive.

## Download First

### 1. `intro_ocean`

- Rename the downloaded file to: `audio/ambience/intro_ocean.mp3`
- Best source page:
  - Pixabay ocean search: `https://pixabay.com/sound-effects/search/ocean/`
  - Pixabay soft waves search: `https://pixabay.com/sound-effects/search/soft%20waves%20sound/`
- What to pick:
  - soft sea wash
  - no music
  - no people
  - no crashing storm waves
- Good duration target:
  - 20 seconds or longer

### 2. `shot03_harbor_approach`

- Rename the downloaded file to: `audio/ambience/shot03_harbor_approach.mp3`
- Best source page:
  - Pixabay harbor search: `https://pixabay.com/sound-effects/search/harbour/`
  - Pixabay harbor ambience search: `https://pixabay.com/sound-effects/search/harbor%20sound/`
  - Pixabay seagull search: `https://pixabay.com/sound-effects/search/seagull/`
- What to pick:
  - light harbor water
  - distant gulls
  - coastal air
  - no modern engines or horns
- Good duration target:
  - 15 seconds or longer

### 3. `shot04_quay_loading`

- Rename the downloaded file to: `audio/ambience/shot04_quay_loading.mp3`
- Best source page:
  - Mixkit tools page: `https://mixkit.co/free-sound-effects/tools/`
  - Mixkit wood page: `https://mixkit.co/free-sound-effects/wood/`
  - Mixkit ambience page: `https://mixkit.co/free-sound-effects/ambience/`
- What to pick:
  - soft wood knocks
  - rope or crate handling texture
  - subtle worker ambience
  - avoid sharp industrial metal hits
- Good duration target:
  - 8 to 20 seconds

### 4. `shot06_ship_construction`

- Rename the downloaded file to: `audio/ambience/shot06_ship_construction.mp3`
- Best source page:
  - Mixkit construction page: `https://mixkit.co/free-sound-effects/construction/`
  - Mixkit tools page: `https://mixkit.co/free-sound-effects/tools/`
  - Mixkit wood page: `https://mixkit.co/free-sound-effects/wood/`
- What to pick:
  - measured hammering on wood
  - timber creaks
  - hand-tool feel
  - avoid power tools or modern machine sounds
- Good duration target:
  - 8 to 20 seconds

### 5. `shot08_bormla_repair`

- Rename the downloaded file to: `audio/ambience/shot08_bormla_repair.mp3`
- Best source page:
  - Mixkit construction page: `https://mixkit.co/free-sound-effects/construction/`
  - Mixkit tools page: `https://mixkit.co/free-sound-effects/tools/`
  - Pixabay harbor search: `https://pixabay.com/sound-effects/search/harbour/`
- What to pick:
  - light repair hammering
  - hull or rope movement
  - water against dock or hull
  - avoid loud modern construction noise
- Good duration target:
  - 10 seconds or longer

## After These Five

Next most useful files would be:

- `audio/ambience/shot05_marketplace_exchange.mp3`
- `audio/ambience/shot09_night_navigation.mp3`
- `audio/ambience/shot10_underwater_shipwreck.mp3`

## Second Wave

These three are the next best return after the first five.

### 6. `shot05_marketplace_exchange`

- Rename the downloaded file to: `audio/ambience/shot05_marketplace_exchange.mp3`
- Best source page:
  - Mixkit ambience page: `https://mixkit.co/free-sound-effects/ambience/`
  - Mixkit people page: `https://mixkit.co/free-sound-effects/people/`
  - Pixabay seagull search: `https://pixabay.com/sound-effects/search/seagull/`
- What to pick:
  - low crowd murmur
  - distant shore birds
  - general harbor life
  - avoid clear modern words or city traffic
- Good duration target:
  - 10 seconds or longer

### 7. `shot09_night_navigation`

- Rename the downloaded file to: `audio/ambience/shot09_night_navigation.mp3`
- Best source page:
  - Pixabay wind search: `https://pixabay.com/sound-effects/search/wind/`
  - Pixabay sea wind search: `https://pixabay.com/sound-effects/search/sea%20wind/`
  - Pixabay ocean search: `https://pixabay.com/sound-effects/search/ocean/`
- What to pick:
  - low wind
  - calm night water
  - minimal rigging feel
  - avoid birds, crowds, storms, and dramatic whooshes
- Good duration target:
  - 15 seconds or longer

### 8. `shot10_underwater_shipwreck`

- Rename the downloaded file to: `audio/ambience/shot10_underwater_shipwreck.mp3`
- Best source page:
  - Pixabay underwater search: `https://pixabay.com/sound-effects/search/underwater/`
  - Mixkit underwater page: `https://mixkit.co/free-sound-effects/underwater/`
- What to pick:
  - subtle underwater wash
  - light submerged ambience
  - almost abstract texture
  - avoid scuba bubbles, sonar pings, and cinematic booms
- Good duration target:
  - 10 seconds or longer

## Lowest Priority

These can stay empty for now without hurting the cut much:

- `audio/ambience/shot01_trade_network_fleet.mp3`
- `audio/ambience/shot02_hero_gaulos_ship.mp3`
- `audio/ambience/shot07_trade_route_map.mp3`
- `audio/ambience/shot11_modern_conservation.mp3`
- `audio/ambience/end_legacy.mp3`

## Rebuild Command

After you place the files in `audio/ambience/`, run:

```bash
python build_pdf_documentary.py
```

Then check:

- `pilot/output/pdf_cut/phoenician_pdf_documentary_subtitled.mp4`
- `pilot/output/pdf_cut/ambience_report.txt`
