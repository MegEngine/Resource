## 开源软件供应链点亮计划—天元MegEngine项目
天元（MegEngine）是在旷视长期进行大规模AI业务落地过程中诞生的，这种业务形态对深度学习框架有很多挑战，在不断解决这些挑战的过程中，天元形成了动静合一、兼容并包、灵活高效、训练推理一体化等特性,能够帮助开发者高效的完成深度学习算法的设计、训练、部署，有效提升AI研发工作效率。
社区官方网址：https://megengine.org.cn/

天元开发者交流QQ群：1029741705

### 任务列表
>注：以下任务均需要能在纯开源版本中进行，因此最好避开过于底层的 C++ 代码（因为外部没有手机 Arm 测试）

任务名称| 内容 | 难度| 导师|具体内容|所需技能
---|---|---|---|---|---|
Github CI 增加 commit 内容检查 | 增加 commit message checker，以规范贡献者 commit 格式|中|张禄<br>zhanglu@megvii.com|<br>1. 使用 commitlint 工具，对于 commit message 进行规范 <br>2. 集成 Gitlab Action| <br>1. SHELL<br>2. Git
实现 MegEngine to Caffe 转换器 | 编写转换器，将 MegEngine 训练出的模型转换成 Caffe 模型|高|陈远昭<br>chenyuanzhao@megvii.com|<br>1. 学习 MegEngine to MACE 转换器 <br>2. 编写 Caffe 转换器<br>3. 正确性、性能测试| <br>1. Python<br>2. Caffe
实现 MegEngine to TFLite 转换器 | 编写转换器，将 MegEngine 训练出的模型转换成 TFLite 模型|高|陈远昭<br>chenyuanzhao@megvii.com|<br>1. 学习 MegEngine to MACE 转换器 <br>2. 编写 TFLite 转换器<br>3. 正确性、性能测试| <br>1. Python<br>2. TF Lite
添加一些常用的opr |添加一些目前MegEngine缺乏的、常用的opr，大部分只需要在python层进行封装。<br>opr包括：<br><li>deformable_conv<br><li>deformable_ps_roipooing<br><li>mask_convolution<br><li>matinv<br><li>svd<br><li>cumsum<br><li>batchrenormalization<br><li>adaptive_max_pooling<br><li>adaptive_avg_pooling<br><li>maxout|中|胡焜<br>hukun@megvii.com|<br>1. 开发 operator <br>2. 添加测试证明正确性<br>3. 添加详细的docstring| <br>1. Python
添加各类常用分类模型|classification模型比如mobilenet/inception，但不需要训练/推理等完整代码，也不需要预训练权重，只需要模型实现即可，统一放在 vision/classification/models[contribution]下面，类似于torchvision那样，前期可以提供示例。|中|周亦庄<br>zhouyizhuang@megvii.com|<br><li>InceptionNet<br><li>Googlenet<br><li>EfficientNet<br><li>Mobilenetv123<br><li>SqueezeNet<br><li>DenseNet<br><li>NASNet-series| <br>1. Python<br>2.PyTorch
实现 assistant 库 | 针对容易出错的使用方式，进行 warning 提示。<br>希望达到玩游戏的时候的那种辅助提示的效果<br><li>比如 momentum < 0.5 的时候，提示："The momentum of batch normalization layer rarely uses a value less than 0.5, Please check the document for momentum's definition, which is different from PyTorch."<br><li>至多提示一次，如果用户觉得我明白风险，可以忽略或显式用 API 表明”我了解这个风险”|高|许欣然<br>xxr@megvii.com|<br>1. 实现一套 warning 的机制 <br>2. 对于 momentum 等地方进行处理，在错读的地方报错<br>3. 编写测试| <br>1. Python<br>2.深度学习框架使用经验
MegEngine 网络可视化|基于 Netron，对 MegEngine 训练网络进行可视化|高|许欣然<br>xxr@megvii.com|| <br>1.Javascript <br>2. Python
C++ 文档生成|基于 Doxygen 和 Sphinx，生成用于集成在官网的 C++ 使用文档|中|许欣然<br>xxr@megvii.com|| <br>1. Python
Models-CI 增加模型检查|对于Models中开源出去模型，进行试运行检查，及时定位Models中的问题|高|王枫<br>wangfeng02@megvii.com|1. 了解github中的workflow<br>2. 实现在CI下对模型试运行的逻辑<br>3. 编写对应测试| <br>1. Python<br>2. shell<br>3. Git
