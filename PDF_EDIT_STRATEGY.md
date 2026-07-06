# PDF Edit Strategy

Used for: the final assembly order that matches the uploaded clips to the PDF sections.

## Decision

The next cut should move from the old 8-shot pilot to an **11-shot PDF-aligned documentary cut** with:

- the uploaded `selected` clips as the visual backbone
- a short male narration track
- optional burned subtitles
- a closing legacy card instead of blocking on one more generated video

## Coverage Order

1. `intro_ocean.mp4`
   - Purpose: calm opening mood
   - PDF tie: transition into the historical context section

2. `shot01_trade_network_fleet.mp4`
   - PDF tie: page 4, Mediterranean expansion and trade reach

3. `shot02_hero_gaulos_ship.mp4`
   - PDF tie: pages 8 and 10, gaulos design and open-sea travel

4. `shot03_harbor_approach.mp4`
   - PDF tie: pages 5, 6, and 12, Malta and Bormla as strategic harbor space

5. `shot04_quay_loading.mp4`
   - PDF tie: pages 4 and 13, cargo handling and maritime logistics

6. `shot05_marketplace_exchange.mp4`
   - PDF tie: pages 4, 6, and 13, cultural and economic exchange

7. `shot06_ship_construction.mp4`
   - PDF tie: pages 8 and 9, shipbuilding methods and materials

8. `shot07_trade_route_map.mp4`
   - PDF tie: pages 4 and 5, route logic across the Mediterranean

9. `shot08_bormla_repair.mp4`
   - PDF tie: pages 12 and 14, safe haven, repair, and maintenance

10. `shot09_night_navigation.mp4`
    - PDF tie: page 10, celestial navigation

11. `shot10_underwater_shipwreck.mp4`
    - PDF tie: page 16, underwater excavation and cargo evidence

12. `shot11_modern_conservation.mp4`
    - PDF tie: page 17, conservation and digital documentation

13. Closing legacy card
    - PDF tie: pages 18 and 19, modern Bormla legacy and ending

## Judgment

- The uploaded clips are now enough to build a coherent documentary cut from the PDF.
- The weakest visual match is page 18, modern Bormla legacy.
- For the next pass, cover page 18 with narration plus the closing legacy card.
- Only generate another video if you specifically want a modern-day Three Cities ending shot.

## Files To Use

- Clip folder: `pika/finals/selected/`
- Narration source: `pdf_cut_narration.txt`
- Build script: `build_pdf_documentary.py`
- Output folder: `pilot/output/pdf_cut/`
