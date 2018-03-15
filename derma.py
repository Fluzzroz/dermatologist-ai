from keras.preprocessing import image
import matplotlib.pyplot as plt

fig = plt.figure()
original = image.load_img("data/ISIC_0015284.jpg")
img = image.load_img("data/ISIC_0015284.jpg", target_size=(299,299))
fig.add_subplot(1,2,1).imshow(original)
fig.add_subplot(1,2,2).imshow(img)
plt.show()
