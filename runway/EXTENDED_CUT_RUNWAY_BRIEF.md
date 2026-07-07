# Used for: generating the extra Runway image-to-video inserts needed to expand the documentary to a natural Sonia-voice cut without narration compression.

## Goal

- Expand the current cut from about 81 seconds to about 96 to 100 seconds.
- Keep Sonia speaking at a natural pace.
- Add visual breathing room instead of forcing the audio to fit short shots.

## Priority

- Required new inserts:
  - `insert_gaulos_hull_detail.mp4`
  - `insert_bormla_harbor_overview.mp4`
  - `insert_influence_routes_map.mp4`
- Strongly recommended replacement:
  - `insert_trade_goods.mp4`

The current `insert_trade_goods.mp4` works as a placeholder, but it feels too much like a still life and includes small glass beads that read as off-period. The archived quay-loading keyframe is much stronger and should be used if you are willing to regenerate that insert.

## Where To Put The Returned Videos

- Preferred if you want the repo self-contained:
  - `cloud_repo/pika/finals/selected/`
- Also supported if you keep media in the main project workspace:
  - `pika/finals/selected/`

`build_pdf_documentary.py` now accepts `VIDEO_SELECTED_DIR`, so I can render from either location without reorganizing everything again.

## Runway Instructions

- Generate each clip in `16:9`.
- Aim for `5 seconds` per insert.
- Keep motion slow and documentary-like.
- Preserve the original composition of the keyframe.
- Avoid dramatic zooms, whip pans, fantasy effects, modern objects, and text overlays.

## Shot 1: Trade Goods Insert

- Status:
  - Replace the current insert if possible.
- Upload image:
  - `runway/extended_cut_keyframes/insert_trade_goods.png`
- Save returned video as:
  - `insert_trade_goods.mp4`
- Insert after:
  - `shot01_trade_network_fleet.mp4`
- Prompt:
  - `Phoenician merchants and dock workers actively loading amphorae and volcanic stone millstones beside a merchant ship in ancient Malta, realistic human motion, workers lifting cargo, passing pottery hand to hand, ropes shifting, sail cloth moving lightly, water lapping against the quay, warm Mediterranean sunlight, cinematic historical documentary realism, preserve the stone harbor, pottery, and millstones, no modern objects, no text.`

## Shot 2: Gaulos Hull Detail Insert

- Upload image:
  - `runway/extended_cut_keyframes/insert_gaulos_hull_detail.png`
- Save returned video as:
  - `insert_gaulos_hull_detail.mp4`
- Insert after:
  - `shot02_hero_gaulos_ship.mp4`
- Prompt:
  - `Close documentary view of a Phoenician gaulos ship moving steadily through calm Mediterranean water, realistic wake, gentle sail movement, subtle hull rocking, preserve the symmetrical rounded hull and high curved bow and stern, emphasize cargo-bearing stability and seaworthiness, warm golden light, no modern objects, no text.`

## Shot 3: Bormla Harbor Overview Insert

- Upload image:
  - `runway/extended_cut_keyframes/insert_bormla_harbor_overview.png`
- Save returned video as:
  - `insert_bormla_harbor_overview.mp4`
- Insert after:
  - `shot03_harbor_approach.mp4`
- Prompt:
  - `Wide elevated view of ancient Bormla and the Grand Harbour in the Phoenician era, realistic moving water, multiple ships drifting slowly, sails fluttering lightly, small harbor traffic, subtle birds above the limestone inlets, stable cinematic documentary framing, preserve the harbor geometry and stone shoreline, no modern objects, no text.`

## Shot 4: Influence And Route Insert

- Upload image:
  - `runway/extended_cut_keyframes/insert_influence_routes_map.png`
- Save returned video as:
  - `insert_influence_routes_map.mp4`
- Insert after:
  - `shot07_trade_route_map.mp4`
- Prompt:
  - `Ancient Mediterranean parchment map with glowing animated trade routes linking the Levant, Malta, Sardinia, North Africa, and southern Europe, warm candlelit atmosphere, slow route pulses, subtle parchment movement, stable overhead documentary framing, emphasize the spread of trade and cultural influence, no modern labels, no text overlays.`

## Planned Order In The Extended Cut

1. `intro_ocean.mp4`
2. `shot01_trade_network_fleet.mp4`
3. `insert_trade_goods.mp4`
4. `shot02_hero_gaulos_ship.mp4`
5. `insert_gaulos_hull_detail.mp4`
6. `shot03_harbor_approach.mp4`
7. `insert_bormla_harbor_overview.mp4`
8. `shot04_quay_loading.mp4`
9. `shot05_marketplace_exchange.mp4`
10. `shot06_ship_construction.mp4`
11. `shot07_trade_route_map.mp4`
12. `insert_influence_routes_map.mp4`
13. `shot08_bormla_repair.mp4`
14. `shot09_night_navigation.mp4`
15. `shot10_underwater_shipwreck.mp4`
16. `shot11_modern_conservation.mp4`
17. `end_legacy`
