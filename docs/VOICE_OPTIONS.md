# Used for: choosing the documentary narration voice and locating preview samples before the next render.

## Recommended First

- `en-GB-ThomasNeural`
  - Best fit for a serious British documentary tone.
  - Current render default in `build_pdf_documentary.py`.
  - Preview: `audio/voice_samples/en-GB-ThomasNeural.mp3`

- `en-GB-RyanNeural`
  - Slightly cleaner and lighter than Thomas.
  - Good fallback if Thomas feels too flat.
  - Preview: `audio/voice_samples/en-GB-RyanNeural.mp3`

## Other Available British Voices

- `en-GB-LibbyNeural`
  - Female, clear and polished.
  - Preview: `audio/voice_samples/en-GB-LibbyNeural.mp3`

- `en-GB-MaisieNeural`
  - Female, softer and brighter.
  - Preview: `audio/voice_samples/en-GB-MaisieNeural.mp3`

- `en-GB-SoniaNeural`
  - Female, slightly firmer than Maisie.
  - Preview: `audio/voice_samples/en-GB-SoniaNeural.mp3`

## Important Limitation

The free local voices available here do not naturally sound elderly, rough, or smoker-like. The closest free option is `en-GB-ThomasNeural` with a lowered pitch. If none of these samples are convincing enough, the next step is a different TTS engine or an external voice service rather than further tweaking the same voice.

## Render Override

`build_pdf_documentary.py` now accepts environment overrides:

```powershell
$env:VIDEO_TTS_VOICE='en-GB-ThomasNeural'
$env:VIDEO_TTS_RATE='-8%'
$env:VIDEO_TTS_PITCH='-14Hz'
python build_pdf_documentary.py
```
