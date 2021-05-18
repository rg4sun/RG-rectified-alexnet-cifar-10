# RG-rectified-alexnet-cifar-10

代码源自：https://github.com/xi-mao/alexnet-cifar-10

做了以下微调：

+ 改了tensorflow的import方式，使其适用于tensorflow v2【源码用的是1.0】
+ 调整了 data.py 的部分代码，原先直接跑不了【python3.7.5下跑不了】
+ 将 train.py 在训练过程中的输出重定向到 `train.log` 文件，保留终端输出
+ 增加 模型训练的耗时计算代码，将训练用时 输出到 log 文件中

之后将做的工作：

+ 修改代码，使其通过alluxio读写数据集进行训练
  + 预期修改文件 `data.py` 、`train.py `

