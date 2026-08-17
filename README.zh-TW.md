# ComfyUI Z-Image Prompt Builder（個人改造版）

[简体中文](README.md) | 繁體中文 | [English](README.en.md)

這是 [VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder](https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder) 的個人改造版。

上游專案與本倉庫採用 [MIT License](LICENSE)。完整安裝方式、原始功能說明與更新記錄，請前往上游倉庫查看。

## 本倉庫新增功能

- 新增 **9:21 直向構圖** 與 **21:9 橫向構圖** 的推薦尺寸輸出。
- 畫面比例新增 **隨機直向** 與 **隨機橫向**：只在對應方向比例中隨機，方形比例不參與。
- 強化 21:9 超寬構圖：
  - 非臥姿自動使用近距離、主體填滿橫向畫面的相機組合；
  - 站姿、行走、坐姿或蹲姿不使用會留下大面積橫向空白的全身或環境構圖；
  - 只有真正橫向伸展的臥姿可以保留橫向全身構圖；
  - 提示詞要求主體佔據畫面主要寬度，減少超寬畫面中同一人物被重複繪製。
- 21:9 隨機場景會避開文字中直接描述行人或人群的選項。

## 上游倉庫

- https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder
- 如果本專案對你有幫助，歡迎前往上游倉庫為原作者點一個 Star。
