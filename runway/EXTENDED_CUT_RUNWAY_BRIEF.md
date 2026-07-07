# Used for: generating the extra Runway image-to-video inserts needed to expand the documentary to a natural Sonia-voice cut without narration compression.

## Goal

- Expand the current cut from about 81 seconds to about 96 to 100 seconds.
- Keep Sonia speaking at a natural pace.
- Add visual breathing room instead of forcing the audio to fit short shots.

## Recommended Strategy

- Use a hybrid approach.
- Keep the strongest existing clips that already work well.
- Add only 3 genuinely new inserts where the current cut feels rushed or visually repetitive.

## Why This Is Better

- Reusing everything is the weakest option because `shot03`, `shot04`, and `shot08` already cover similar harbor space and would start to feel repetitive.
- Replacing too much is wasteful because several current shots are already strong:
  - `shot04_quay_loading.mp4`
  - `shot05_marketplace_exchange.mp4`
  - `shot06_ship_construction.mp4`
  - `shot08_bormla_repair.mp4`
  - `shot10_underwater_shipwreck.mp4`
  - `shot11_modern_conservation.mp4`
- The best return on credits is to keep those strong shots and generate new inserts only where the narration needs more time or a more specific visual.

## What To Keep

- Keep these existing clips:
  - `intro_ocean.mp4`
  - `shot01_trade_network_fleet.mp4`
  - `shot02_hero_gaulos_ship.mp4`
  - `shot03_harbor_approach.mp4`
  - `shot04_quay_loading.mp4`
  - `shot05_marketplace_exchange.mp4`
  - `shot06_ship_construction.mp4`
  - `shot07_trade_route_map.mp4`
  - `shot08_bormla_repair.mp4`
  - `shot09_night_navigation.mp4`
  - `shot10_underwater_shipwreck.mp4`
  - `shot11_modern_conservation.mp4`

## What To Generate

- Generate these 3 new inserts:
  - `insert_trade_goods_detail.mp4`
  - `insert_gaulos_broadside_hull.mp4`
  - `insert_cultural_influence_map.mp4`

The old `insert_trade_goods.mp4` is not recommended as the final insert. It feels too still and includes small beads that read as off-period.

## Where To Put The Returned Videos

- Preferred if you want the repo self-contained:
  - `cloud_repo/pika/finals/selected/`
- Also supported if you keep media in the main project workspace:
  - `pika/finals/selected/`

`build_pdf_documentary.py` now accepts `VIDEO_SELECTED_DIR`, so I can render from either location without reorganizing everything again.

## Workflow

- The still keyframes below have already been generated and saved in `runway/extended_cut_keyframes/`.
- Upload those stills to Runway and use the matching motion prompt below.

## Runway Instructions

- Generate each clip in `16:9`.
- Aim for `5 seconds` per insert.
- Keep motion slow and documentary-like.
- Preserve the original composition of the keyframe you generate.
- Avoid dramatic zooms, whip pans, fantasy effects, modern objects, and text overlays.

## Shot 1: Trade Goods Detail Insert

- Generated still keyframe:
  - `runway/extended_cut_keyframes/insert_trade_goods_detail.png`
- Keyframe prompt:
  - `Tight cinematic historical documentary close-up on an ancient Maltese stone quay during the Phoenician era, dock workers handling volcanic stone millstones, amphorae, and diverse decorated pottery, hands passing cargo, coarse rope, weathered wood, warm Mediterranean sunlight, realistic textures, no modern objects, no text, 16:9.`
- Upload image:
  - `runway/extended_cut_keyframes/insert_trade_goods_detail.png`
- Save returned video as:
  - `insert_trade_goods_detail.mp4`
- Insert after:
  - `shot01_trade_network_fleet.mp4`
- Motion prompt:
  - `Phoenician dock workers actively handling volcanic stone millstones, amphorae, and decorated pottery on an ancient Maltese quay, realistic hand and shoulder motion, cargo passed from person to person, rope shifting, cloth moving lightly in sea breeze, subtle harbor water movement in background, cinematic historical documentary realism, no modern objects, no text.`

## Shot 2: Gaulos Broadside Hull Insert

- Generated still keyframe:
  - `runway/extended_cut_keyframes/insert_gaulos_broadside_hull.png`
- Keyframe prompt:
  - `Broadside documentary view of a Phoenician gaulos merchant ship at sea, clear rounded cargo belly, symmetrical hull shape, high curved bow and stern, square sail, calm Mediterranean water, golden late-afternoon light, historically grounded, realistic wood texture, no modern objects, no text, 16:9.`
- Upload image:
  - `runway/extended_cut_keyframes/insert_gaulos_broadside_hull.png`
- Save returned video as:
  - `insert_gaulos_broadside_hull.mp4`
- Insert after:
  - `shot02_hero_gaulos_ship.mp4`
- Motion prompt:
  - `Phoenician gaulos ship moving steadily through calm Mediterranean water, realistic wake, gentle sail movement, subtle hull rocking, stable side-view composition, preserve the rounded cargo body and high curved bow and stern, emphasize balance, cargo capacity, and seaworthiness, warm documentary light, no modern objects, no text.`

## Shot 3: Cultural Influence Map Insert

- Generated still keyframe:
  - `runway/extended_cut_keyframes/insert_cultural_influence_map.png`
- Keyframe prompt:
  - `Ancient Mediterranean trade map laid on a wooden table, Malta at the center with visible links toward Sardinia, North Africa, the Levant, and southern Europe, parchment, trade tokens, pottery fragments, warm candlelight, scholarly historical documentary mood, no modern labels, no text overlay, 16:9.`
- Upload image:
  - `runway/extended_cut_keyframes/insert_cultural_influence_map.png`
- Save returned video as:
  - `insert_cultural_influence_map.mp4`
- Insert after:
  - `shot07_trade_route_map.mp4`
- Motion prompt:
  - `Ancient Mediterranean trade map in candlelight with subtle animated route pulses linking Malta, Sardinia, North Africa, the Levant, and southern Europe, slight parchment movement, small trade markers shifting gently, stable overhead documentary framing, emphasize cultural and commercial influence spreading across the sea, no modern labels, no text overlays.`

## Planned Order In The Extended Cut

1. `intro_ocean.mp4`
2. `shot01_trade_network_fleet.mp4`
3. `insert_trade_goods_detail.mp4`
4. `shot02_hero_gaulos_ship.mp4`
5. `insert_gaulos_broadside_hull.mp4`
6. `shot03_harbor_approach.mp4`
7. `shot04_quay_loading.mp4`
8. `shot05_marketplace_exchange.mp4`
9. `shot06_ship_construction.mp4`
10. `shot07_trade_route_map.mp4`
11. `insert_cultural_influence_map.mp4`
12. `shot08_bormla_repair.mp4`
13. `shot09_night_navigation.mp4`
14. `shot10_underwater_shipwreck.mp4`
15. `shot11_modern_conservation.mp4`
16. `end_legacy`
