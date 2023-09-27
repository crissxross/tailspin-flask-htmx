# Recreating Tailspin notes

JSON data for all the segments (or fragments) of the story, containing:

- id
- animation (optional)
- audio list (optional)
- character ?? (George or Karen)
- scene number ??

Online YAML parser - http://yaml-online-parser.appspot.com/

I've changed the daughter's name to ALISON

## This YAML

- scene: 1
  fragments:
  - id: g1
    text: |
        He shouts.
        Shocks them into silence.
    animation: ""
    audio: []
  - id: g2
    text: |
        The first time a bomb exploded, he thought he'd gone deaf in his other ear too.
    animation: ""
    audio: []

### produces this JSON

```json
[
  {
    "fragments": [
      {
        "text": "He shouts.\nShocks them into silence.\n",
        "animation": "",
        "id": "g1",
        "audio": []
      },
      {
        "text": "The first time a bomb exploded, he thought he'd gone deaf in his other ear too.\n",
        "animation": "",
        "id": "g2",
        "audio": []
      }
    ],
    "scene": 1
  }
]
```
