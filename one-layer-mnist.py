import tensorflow as tf
import os
from tensorflow.examples.tutorials.mnist import input_data
print("\t+-----Welcome to the MNIST Neural Network-----+\n\n")
networkName = "1HL"
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
print("\t>> DATA IMPORT COMPLETE <<\n")

sess = tf.InteractiveSession()

#multi-run handling
logs_path = ""
for i in range(1000):
  deflogs_path = "/tmp/mnist/" + ("{1}: run{0}".format(i,networkName))
  if os.path.isdir(deflogs_path) != True:
    logs_path = deflogs_path
    break

with tf.name_scope("inputs"):
    inp = tf.placeholder(tf.float32, shape=[None,784]) 
    output_ = tf.placeholder(tf.float32, shape=[None,10])

with tf.name_scope('weight1'):
    W1 = tf.Variable(tf.random_normal([784,256]))
with tf.name_scope('bias1'):
    b1 = tf.Variable(tf.random_normal([256]))
with tf.name_scope('First_Layer'):
    layer1 = tf.add(tf.matmul(inp,W1), b1)
    

with tf.name_scope('weight2'):
    W2 = tf.Variable(tf.random_normal([256,10]))
with tf.name_scope('bias2'):
    b2 = tf.Variable(tf.random_normal([10]))
with tf.name_scope('Wx_plus_b'):
    output = tf.add(tf.matmul(layer1, W2) , b2)

with tf.name_scope("costFunction"):
    costFunc = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels = output_, logits = output ))
with tf.name_scope('train'):
    train_step = tf.train.AdamOptimizer(0.001).minimize(costFunc)
sess.run(tf.global_variables_initializer())

#Acccuracy management
with tf.name_scope('accuracyFunction'):
      with tf.name_scope('correct_prediction'):
          correct_prediction = tf.equal(tf.argmax(output,1), tf.argmax(output_,1))
      with tf.name_scope('accuracy'):
          accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#Tensorboard logger
writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())
tf.summary.scalar("cost", costFunc)
tf.summary.scalar("accuracy", accuracy)
merged = tf.summary.merge_all()

#training loop
for t in range(1000):
    batch = mnist.train.next_batch(100)
    train_step.run(feed_dict={inp: batch[0], output_: batch[1]})
    writer.add_summary(merged.eval(feed_dict={inp: batch[0], output_: batch[1]}),t+1)
    if t % 100 == 0:
      print("Batch {} completed".format(t))
print("\n\t+-----Done training-----+\n\n")


percent = accuracy.eval(feed_dict={inp: mnist.test.images, output_: mnist.test.labels})

print("Accuracy: {}%".format(percent*100))