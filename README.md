# ComfyUI Z-Image Prompt Builder（个人改造版）

这是 [VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder](https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder) 的个人改造版。

原插件与本仓库均遵循 [MIT License](LICENSE)。完整安装方式、原始功能说明与更新记录，请前往上游仓库查看。

## 本仓库新增功能

- 新增 **9:21 竖构图** 与 **21:9 横构图** 的推荐尺寸输出。
- 画面比例新增 **随机竖屏** 与 **随机横屏**：仅在相应方向的比例中随机，方形比例不参与。
- 强化 21:9 超宽构图：
  - 非卧姿自动使用近距离、主体占满横向画幅的相机组合；
  - 不允许站姿、行走、坐姿或蹲姿使用动态全身、全身、环境构图等会留下大面积横向空白的景别；
  - 只有真正横向展开的卧姿可保留横向全身构图；
  - 提示词加入主体横向占据画面主要宽度、两侧仅保留少量背景的正向构图说明，以减少同一人物在超宽画幅中被重复绘制。
- 21:9 随机场景会避开文本中直接描述行人或人群的选项。

## 上游仓库

- https://github.com/VividMuse-AGI/ComfyUI-Z-Image-Prompt-Builder
