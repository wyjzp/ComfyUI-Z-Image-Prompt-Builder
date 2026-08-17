# ComfyUI Z-Image Prompt Builder (Personal Modification)

[简体中文](README.md) | [繁體中文](README.zh-TW.md) | English

This is a personal modification of [VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder](https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder).

The upstream project and this repository use the [MIT License](LICENSE). Refer to the upstream repository for original installation instructions, features, and changelog.

## Features added in this repository

- Added recommended dimensions for **9:21 portrait** and **21:9 landscape** canvases.
- Added **Random Portrait** and **Random Landscape** aspect-ratio options. They select only ratios in the matching orientation; square ratios are excluded.
- Strengthened 21:9 ultra-wide composition:
  - Upright subjects use close, subject-filling camera setups.
  - Standing, walking, seated, and crouching poses cannot retain dynamic full-body, full-body, or environmental framings that leave large lateral empty areas.
  - Only genuinely horizontal reclining poses may retain full-body ultra-wide framing.
  - Prompts request a subject occupying most of the banner width with narrow background margins, reducing repeated copies of the same subject in ultra-wide output.
- Random 21:9 scene selection avoids options whose text explicitly describes pedestrians or crowds.

## Upstream project

- https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder
- If this project is useful, please visit the upstream repository and give the original author a Star.

## Language

The Chinese README is the default documentation. This file provides an English version for international users.
