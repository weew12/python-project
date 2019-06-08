from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("G:\python 资源\deep learning\MNIST_data", one_hot=True)

# 训练数据集
print(mnist.train.num_examples)
# 验证数据集
print(mnist.validation.num_examples)
# 测试数据集
print(mnist.test.num_examples)
# 打印一个训练图片的数据
print(mnist.train.images[0])
# 打印一个训练图片的分类标签
print(mnist.train.labels[0])
