## 背景
AI 浪潮一波又一波，仿佛不会算法就落后于时代。
深度学习框架处理了各种设备的计算细节、求导、计算优化序列的工作，而在动态、静态两套截然不同的世界中，这些步骤又各自有他们不同的优化点和瓶颈。
如何在中间获取一个高效的平衡呢？以及如何克服训练完的模型在推理部署中无数的坑（闻者落泪），那个堪称对此进行降维打击的“训练推理一体化”到为何物？

## 分享内容
MegEngine 天元作为旷视全员自用6年的自研深度学习框架，是一个在淘金热时，坚持选择卖铲子的团队。旷视研究院 AI 系统高级技术总监、MegEngine 技术负责人许欣然作为主讲人。
他将带我们了解一个深度学习框架是如何把网络的定义逐步优化并最终执行的，从框架开发者的视角来看待深度学习。<br/>

**视频地址：** https://www.bilibili.com/video/BV11C4y1t7xH<br/>

**课件地址：**[金枪鱼之夜：MegEngine 框架设计.pdf](./slides/金枪鱼之夜：MegEngine%20框架设计.pdf)<br/>

## 分享大纲
- 背景介绍
  - 深度学习框架是干啥的？
  - 道理我都懂，为什么又搞一个深度学习框架？
  - 你们为啥不用 PyTorch / TensorFlow？
  - 训推一体是个啥玩意？
- 如何写出一个深度学习框架？（超简化版）
  - 动态图训练
  - 调用 = 执行
  - 依赖关系图 forward & backward
  - megdnn kernel
  - exec
  - Shape Deduce
  - 静态图训练 + 推理（粗糙版）
    - Tensor
    - Graph、SymborVar
    - CompNode
    - Shape Inference
    - Graph Optimization
    - 拓扑排序
    - 内存优化
    - Computing Sequence
- 一个陈年静态图框架是怎么变成动态图框架的？
  - Dynamic Region
  - Eager Graph
  - Eager Runtime + Proxy Graph
- 对未来的展望
  - 各种芯片模组的对接，挑战训推一体的理念
  - MLIR 等技术的兴起
  - 如何做到真 JIT
