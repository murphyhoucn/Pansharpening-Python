import spectral
import numpy as np
import matplotlib.pyplot as plt

# 设置文件路径
ms_path = r'../../home_info/202404 Test data_WV-2 Sydney MS400+PAN1600/GF2_BJ_mss.npy'
pan_path = r'../../home_info/202404 Test data_WV-2 Sydney MS400+PAN1600/GF2_BJ_pan.npy'

# 加载多光谱图像
img_ms = np.load(ms_path)

# 将图像数据转为数组形式
print(img_ms.shape)  # (高度, 宽度, 波段数)
print(type(img_ms))  # <class 'numpy.ndarray'>

[h, w, c] = img_ms.shape

# 提取不同波段的图像
img_ms_1 = img_ms[:, :, 0]
img_ms_2 = img_ms[:, :, 1]
img_ms_3 = img_ms[:, :, 2]
img_ms_4 = img_ms[:, :, 3]

print(img_ms_1.shape)  # 应该输出 (h, w)
print(type(img_ms_1))  # <class 'numpy.ndarray'>

# 创建2行2列的子图
fig, axs = plt.subplots(1, 4, figsize=(20, 5))

# 在第一个子图中显示灰度图像
axs[0].imshow(img_ms_1, cmap='gray')
axs[0].set_title('B')
axs[0].axis('off')  # 隐藏轴

# 在第二个子图中显示灰度图像
axs[1].imshow(img_ms_2, cmap='gray')
axs[1].set_title('G')
axs[1].axis('off')  # 隐藏轴

# 在第三个子图中显示灰度图像
axs[2].imshow(img_ms_3, cmap='gray')
axs[2].set_title('R')
axs[2].axis('off')  # 隐藏轴

# 在第四个子图中显示灰度图像
axs[3].imshow(img_ms_4, cmap='gray')
axs[3].set_title('nir')
axs[3].axis('off')  # 隐藏轴

# 调整子图布局
plt.tight_layout()
plt.show()



# 加载全色图像
img_pan = np.load(pan_path)
img_pan = np.array(img_pan)
print(img_pan.shape)  # (高度, 宽度)
print(type(img_pan))  # <class 'numpy.ndarray'>

# 显示全色图像
plt.imshow(img_pan, cmap='gray')
plt.title('PAN')
plt.axis('off')  # 隐藏轴
plt.show()

