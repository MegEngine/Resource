
MegEngine (天元)是一个快速、可拓展、易于使用且支持自动求导的开源深度学习框架。拥有三大核心优势：训练推理一体、全平台高效支持、动静结合的训练能力。

在开源软件供应链点亮计划 - 暑期 2021 活动中，MegEngine 将提供以下项目任务，并搭配导师，帮助大家更好的完成项目。

MegEngine 官网：https://megengine.org.cn/

天元开发者交流 QQ 群：1029741705



## 项目一：添加 RNN/LSTM 系列算子

1. 项目标题：添加 RNN/LSTM 系列算子

2. 项目描述：目前 MegEngine 对于 NLP 相关接口的支持比较少，较为经典的 RNN/LSTM 算子没有提供支持，希望能在 MegEngine 中提供支持

3. 项目难度：高

4. 项目社区导师：陈振寰

5. 导师联系方式：chenzhenhuan@megvii.com

6. 项目产出要求：
   - 在 megengine python 接口层面添加 RNN/LSTM 算子
   - 参考内部文档在 c++层面实现 RNN/LSTMCell 算子，改进上层 python 接口，并达到与 pytorch 接近的性能

7. 项目技术要求：python、pytorch、C++

8. 相关的开源软件仓库列表：https://github.com/pytorch/pytorch

## 项目二：x86 中添加并优化 local

1. 项目标题：x86 中添加并优化 local
2. 项目描述：目前 MegEngine 中 naive 和 CUDA 中支持了 local 和 local share 算子，但是 x86 中并没有支持，因此这些算子在 x86 上运行只能使用 naive 的算子，速度很慢
3. 项目难度：高
4. 项目社区导师：陈其友
5. 导师联系方式：chenqiyou@megvii.com
6. 项目产出要求：
   - 在 x86 backend 下面完成 local 算子填加
   - 算子计算结果和 naive 在所有 case 下结果完全一致
   - 优化算子，使其逼近最佳性能

7. 项目技术要求：C++，性能优化
8. 相关的开源软件仓库列表：https://github.com/MegEngine/MegEngine/tree/master/dnn/src/naive/local

## 项目三：x86 中添加并优化 local share 算子

1. 项目标题：x86 中添加并优化 local share 算子
2. 项目描述：目前 MegEngine 中 naive 和 CUDA 中支持了 local 和 local share 算子，但是 x86 中并没有支持，因此这些算子在 x86 上运行只能使用 naive 的算子，速度很慢
3. 项目难度：高
4. 项目社区导师：陈其友
5. 导师联系方式：chenqiyou@megvii.com
6. 项目产出要求：
   - 在 x86 backend 下面完成 local share 算子填加
   - 算子计算结果和 naive 在所有 case 下结果完全一致
   - benchmark 并优化算子，使其逼近最佳性能

7. 项目技术要求：C++，性能优化

8. 相关的开源软件仓库列表：https://github.com/MegEngine/MegEngine/tree/master/dnn/src/naive/local_share

## 项目四：web 上运行 mge 模型

1. 项目标题：web 上运行 mge 模型
2. 项目描述：在 web 上跑起来简单的 mge 模型
3. 项目难度：高
4. 项目社区导师：柳俊杰
5. 导师联系方式：liujinjie@megvii.com
6. 项目产出要求：

   在 web 上跑起来线性回归模型/手写字模型，要求提供 mge.js 和可运行的 model。

	方案：

   - 框架部分用 wasm 编译为 mge.js（需要能加载 dump 的 mge 模型，最好不要做模型转换）
   - 缺的 kernel 可以参考 xnnpack 用 wasm 进行补充。（webgpu 当前效率不高，webgl 用于计算比较别扭，所以还是选支持 simd 的 wasm）

	实现的效果分为 7 级：
   
   - L0：可以加载模型和数据（可以不支持图优化/存储优化等各种优化，可以对现有的框架通过宏进行裁剪，甚至可以重写一个新框架，但必须保证模型的兼容性加载）
   - L1：dense/matmul（必选）的前向 op 单测通过（要求 nchw 的 layout 下正确性ok）
   - L2: 跑通线性回归模型前向
   - L3: 跑通线性回归模型的后向和训练
   - L4: 跑通 mnist 模型前向
   - L5: 跑通 mnist 后向和训练
   - L6: mnist 的 demo（参考 https://storage.googleapis.com/tfjs-examples/mnist/dist/index.html）

7. 项目技术要求：js/wasm/c++/python

8. 相关的开源软件仓库列表：

   - https://github.com/tensorflow/tfjs

   - https://github.com/google/XNNPACK

   - https://www.tensorflow.org/js/demos?hl=zh-cn

   - https://zhuanlan.zhihu.com/p/356317676

   - https://github.com/alibaba/MNN/blob/master/3rd_party/flatbuffers/docs/source/JavaScriptUsage.md

   - https://github.com/torch-js/torch-js


## 项目五：一个对用户友好的 web profile 工具

1. 项目标题：一个对用户友好的 web profile 工具
2. 项目描述：在 web 上提交 mge 模型，后端执行并反馈 profile 细节
3. 项目难度：高
4. 项目社区导师：柳俊杰
5. 导师联系方式：liujinjie@megvii.com
6. 项目产出要求：
	
	一个对用户友好的 web profile 工具 C/S 结构，前端负责收集模型、可视化、打印 profile 结果。后端负责实际跑模型，后端的支持可以覆盖 x86/cuda/arm 等。
	
	- L0: 前端能提交 mge 模型，打印模型的执行延迟。后端支持 X86，能接受前端的模型并反馈延迟结果，后端的执行可以包装 load_and_run。
	- L1: 前端支持打印 profile 结果，后端反馈 profile 结果。后端的 profile 可以直接返回load_and_run的profile json结果，并提供过滤、排序、聚合等操作
	- L2: 前端支持模型结构预览，并可视化每层的耗时
	- L3: 扩展后端范围，包括 cuda/arm。方便没有设备的用户能直接得到性能数据。

7. 项目技术要求：html/js/c++/python

## 项目六：dnn backend 加入 apple NPU 的支持

1. 项目标题：dnn backend 加入 apple NPU 的支持
2. 项目描述：在 MACOS 上推理可用 APPLE np
3. 项目难度：高
4. 项目社区导师：张浩龙
5. 导师联系方式：zhanghaolong@megvii.com
6. 项目产出要求：

	在 MACOS上 推理可用 APPLE npu，基于 CoreML API

	- L0: MegEngine 模型转换到 CoreML 可用格式, 能使用 CoreML API 把这个模型跑起来

	- L1: 参考 MegEngine/src/tensorrt/impl 实现 CoreML 在 MegEngine 下的 runtime opr

	- L2：最终在支持 CoreML 的平台上跑起来推理 MegEngine 并且利用 CoreML 加速

7. 项目技术要求：c++, macos

8. 相关的开源软件仓库列表：

	- https://developer.apple.com/documentation/coreml/core_ml_api

	- https://github.com/MegEngine/MegEngine

## 项目七：python whl 支持 apple ARM macos

1. 项目标题：python whl 支持 apple ARM macos
2. 项目描述：在 apple arm macos 上，可用 megengine python
3. 项目难度：高
4. 项目社区导师：张浩龙
5. 导师联系方式：zhanghaolong@megvii.com
6. 项目产出要求：

	在 apple arm macos 上，可用 MegEngine python

	- L0: 本地编译通过

	- L1: 包具备分发性，可安装到其他 aarch64+ macbook 上，且能运行

	- L2: 能在基于 aarch64 + macbook 上训练一个模型

7. 项目技术要求：c++, 编译，macos

8. 相关的开源软件仓库列表：https://github.com/MegEngine/MegEngine

## 项目八：python whl 支持 Android (限定在主流的 ARM)

1. 项目标题：python whl 支持 Android (限定在主流的ARM吧)
2. 项目描述：在 Android arm 上，可用 megengine python
3. 项目难度：高
4. 项目社区导师：张浩龙
5. 导师联系方式：zhanghaolong@megvii.com
6. 项目产出要求：

	在 Android aarch64 上(termux 环境)，可用 MegEngine python

	- L0: NDK-x86 linux cross build aarch64 Android 编译通过

	- L1: 包具备分发性，可安装到其他 aarch64+ Android 上，且能运行

	- L2: 能在基于 aarch64 + Android + termux 训练一个小模型

7. 项目技术要求：c++, 编译， Android

8. 相关的开源软件仓库列表：https://github.com/MegEngine/MegEngine

## 项目九：模型转换 - ONNX 转 MegEngine

1. 项目标题：模型转换 - ONNX 转 MegEngine
2. 项目描述：

	背景：目前官方的 mgeconvert 仓库里面只提供了 MegEngine 模型转到其他框架的功能，反过来不行。
	目标：完成 ONNX 模型到 MegEngine 的转换。

   - 支持选择 ONNX/MegEngine 版本
   - 转换并 dump 出 cpp model（可以用 MegEngine op graph 建图并 dump）
   - 只支持推理，不支持训练。

3. 项目难度：中
4. 项目社区导师：熊鹏
5. 导师联系方式：xiongpeng@megvii.com
6. 项目产出要求：

	转换能力需覆盖 model hub 里的模型

	方案：
	
	- 完成 ONNX 模型的解析
	- 实现 ONNX 与 MGE 各类算子的转换
	- 根据 ONNX 模型中包含的算子搭建出完整的 MGE 模型

	实现效果：转换出来的模型可以完成推理。
	
	- L0：在特定版本上实现模型的转换
	- L1：实现不同版本 ONNX 到 MGE 的转换

7. 项目技术要求：Python、ONNX

8. 相关的开源软件仓库列表：

	- https://github.com/MegEngine/mgeconvert

	- https://github.com/MegEngine/MegEngine/blob/master/imperative/python/megengine/utils/network.py 



