# Pilot Motion Plan

## Objective
Upgrade the pilot from a still-image animatic to a motion-first historical teaser with selective in-scene animation.

## Motion Principle
- Do not animate everything.
- Animate the elements that sell life, scale, and function.
- Prioritize water, sails, smoke, dust, human gestures, and cargo handling.
- Keep motion slow and cinematic rather than fast or exaggerated.

## Scene 1: Fleet at Sea
### High-value motion
- Lead ship moving forward through water
- Gentle ship bobbing
- Linen sails flexing in the wind
- Wake and surface ripples
- Subtle cloud drift and light shimmer

### Optional motion
- Seabirds in the far distance
- Small crew silhouette shifts on deck

### Avoid
- Violent rocking
- Unrealistically fast ship speed
- Storm effects

## Scene 2: Trade Quay
### High-value motion
- Workers carrying amphorae
- One worker guiding a millstone or cargo bundle
- Ropes swaying
- Water moving against the quay
- Cloth garments moving slightly in the breeze

### Optional motion
- A ship moored in the background drifting slightly
- Dust or sun haze in the air

### Avoid
- Crowd chaos
- Too many simultaneous gestures
- Modern dock behavior or tools

## Scene 3: Bormla Harbor
### High-value motion
- Slow ship movement across harbor water
- Anchored vessels rocking gently
- Sun glint across the protected water
- Light wind in sails and banners

### Optional motion
- Tiny rowboat or service craft crossing the frame
- Soft atmospheric haze

### Avoid
- Busy modern harbor energy
- Large crowd motion
- Aggressive camera movement

## Scene 4: Shipwrights and Construction
### High-value motion
- One or two shipwrights hammering or fitting timber
- A worker carrying planks or tools
- Dust in sunlight
- Rope movement
- Slight cloth and hair movement from wind

### Optional motion
- Resin application or caulking gesture
- Background worker silhouette activity

### Avoid
- Too many workers moving at once
- Repetitive looped gestures that look robotic
- Modern construction rhythm

## Worth Animating First
1. Ships moving on water
2. Sails reacting to wind
3. Workers doing one clear task
4. Cargo handling
5. Dust, smoke, and sunlight particles

## Lower Priority
- Facial expression changes
- Large crowd choreography
- Complex hand-to-object interactions across many people
- Fast scene transitions driven by motion alone

## Best Execution Strategy
### External AI video model
Use the still keyframe as the reference image, then prompt for:
- subtle ship motion
- historically accurate sail movement
- workers performing one or two clear tasks
- cinematic realism
- no morphing, no extra limbs, no modern elements

### Local fallback
If external video generation is not usable:
- add layered motion to ships and water
- add route-line or glow effects where suitable
- add smoke, dust, and lighting motion
- add gentle parallax and masked foreground movement

## Recommended Prompt Style for Image-to-Video
- "Animate this historical scene with subtle realistic motion. The ship moves slowly forward through calm Mediterranean water, sails flex naturally in a light wind, and the hull rises gently with the swell. Preserve the original composition, historical accuracy, and documentary tone. No fantasy elements, no modern objects, no distortion, no extra people."

- "Animate this harbor trade scene with restrained human activity. Two or three dock workers carry amphorae and guide cargo toward the ship, ropes sway lightly, garments move in the breeze, and water laps against the stone quay. Preserve the original framing and keep movement realistic and period-accurate."

## Pilot V2 Direction
- Keep the existing four pilot scenes.
- Replace still-only motion with selective object motion.
- Test one sea scene and one shipyard scene first.
- If those work, upgrade the full pilot rather than rebuilding from scratch.
