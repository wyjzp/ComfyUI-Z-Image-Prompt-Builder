# ComfyUI Z-Image Prompt Builder (Personal Modification)

This is a personal modification of [VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder](https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder).

The upstream project and this repository use the [MIT License](LICENSE). Refer to the upstream repository for installation instructions, original features, and changelog.

## Features added in this repository

- Added recommended dimensions for **9:21 portrait** and **21:9 landscape** canvases.
- Added **Random Portrait** and **Random Landscape** aspect-ratio options. They randomize only within the respective orientation; square ratios are excluded.
- Strengthened 21:9 ultra-wide composition:
  - Upright subjects automatically use close, subject-filling camera setups.
  - Standing, walking, seated, and crouching poses cannot retain dynamic full-body, full-body, or environmental framings that leave large lateral empty areas.
  - Only genuinely horizontal reclining poses may retain a full-body ultra-wide framing.
  - Prompts explicitly request a subject that occupies most of the banner width with only narrow background margins, reducing repeated copies of the same subject in ultra-wide output.
- Random 21:9 scene selection avoids options whose text explicitly describes pedestrians or crowds.

## Upstream project

- https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder
