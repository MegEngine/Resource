
MegEngine 是一个快速、可拓展、易于使用且支持自动求导的深度学习框架，具备训练推理一体、超低硬件门槛和全平台高效推理 3 大核心优势。

在开源软件供应链点亮计划 - 暑期 2022 活动中，MegEngine 将提供以下项目任务，并搭配导师，帮助大家更好的完成项目。

## 项目一：MegEngine 中 Arm backend 中反卷积支持 nc4hw4 layout 计算优化


1. 项目描述：
   * 背景：MegEngine 作为训推一体框架，其在 Arm 上的推理性能也非常重要，目前 MegEngine Arm 推理性能经过 benchmark 在业界处于第一梯队，主要优化方式是在Arm上支持 NC4HW4的layout，Layout 的详细解释见：[知乎回答](https://www.zhihu.com/question/337513515)，目前反卷积 Forward 算子中没有支持这种 Layout 形式优化，希望通过支持这种 Layout 达到优化性能的目的。
   * 需求：在 ArmCommon 中 ConvolutionBackwardDataImpl 中支持 NC4HW4 layout 的计算，使得 ConvolutionBackwardDataImpl 可以在 NC4HW4 的 layout 下完成计算，并且性能不差于目前的 NCHW layout。

2. 项目难度：进阶

3. 项目产出要求：
   * 代码规范
   * 相同 shape 下，性能超过目前 NCHW

4. 项目技术要求
   * C++
   * 反卷积计算原理
   * Arm neon 优化

5. 项目成果仓库：https://github.com/MegEngine/MegEngine


## 项目二：MegEngineLite 支持进程化 Debug

1. 项目描述：
   * 背景：目前 MegEngine 作为用户的最底层，很多情况下崩溃，会将栈暴露在 MegEngine 中，但是很多情况是由于用户环境里面的其他程序踩踏了 Lite 的内存，因此看上去是崩溃在  MegEngine 中。
   * 需求：lite 计算支持一种 debug 模式，这种模式通过 env 控制（模式配置需要在 caller 调用发生调用任意 LITE API 之前就完成，所以需要和 API 本身解绑），在这种模式下模型的执行会 fork 一个单独的进程，并执行，这时候就和用户的进程进行了隔离，避免内存被踩踏的情况发生。

2. 项目难度：进阶

3. 项目产出要求：能让 MegEngine 推理服务和 Lite 接口 caller 分别运行在不同的进程，进程间通信高效 

4. 项目技术要求
   * C++/C
   * 主流操作系统创建进程
   * 高效的进程间通信

5. 项目成果仓库：https://github.com/MegEngine/MegEngine

## 项目三：MegEngine 补充跨模态模型的实现

1. 项目描述：
   * 背景：MegEngine Hub 中实现了常用的分类检测等算法，但是还缺少一些最新的深度学习研究领域的算法实现。
   * 需求：用 MegEngine 中，添加 CLIP、VQGAN、DALL·E、BigSleep 模型的推理代码，确保精度与其他框架中一致，并添加到 MegEngine Hub 上。

2. 项目难度：进阶

3. 项目产出要求：
   * 在 https://github.com/MegEngine/ 下贡献一个代码实现的 repo 并有对应的使用文档说明
   * 模型运行与其他框架结果可对应（比如实现 CLIP，可与 https://github.com/openai/CLIP 进行模型对分）
  
4. 项目技术要求
   * Python
   * 深度学习

5. 项目成果仓库：
   * https://github.com/MegEngine/MegEngine
   * https://github.com/MegEngine/Models
   
## 项目四：python whl 支持 apple ARM macos

1. 项目描述：
   * 背景：目前 MegEngine 开发时没有没有进行 apple aarch64 macos 操作系统的适配，MegEngine 并没有发布适配 apple aarch64 macos 的安装包。随着 apple aarch64 macos 电脑越来越多，此需求日益剧增。
   * 需求：在 MegEngine 中适配 apple aarch64 macos，完成 MegEngine apple aarch64 macos 安装包发布。
  
2. 项目难度：进阶

3. 项目产出要求：在 apple aarch64 macos 上，产出 MegEngine 的 wheel 安装包。
   * L0: MegEngine 在 apple aarch64 macos 上可本地编译通过。
   * L1: 包具备分发性，可安装到其他 aarch64+ macbook 上，且能正常运行。
   * L2: 安装后能训练一个模型。  

4. 项目技术要求
   * C++
   * 编译
   * macos

5. 项目成果仓库：https://github.com/MegEngine/MegEngine


项目申请：https://summer-ospp.ac.cn/#/org/orgdetail/294bd67f-5476-40d4-bd74-2a9d5296cf5a/

MegEngine 官网：https://www.megengine.org.cn/

MegEngine 技术交流 QQ 群：1029741705
