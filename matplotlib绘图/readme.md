
# 绘图 （线性）


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
# print(x)
fig = plt.figure()
plt.plot(x, np.sin(x), '*')
plt.plot(x, np.cos(x), '-.')
fig.savefig('res1.png')
```


![png](1-1_files/1-1_1_0.png)


# 保存图片


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
# print(x)
plt.plot(x, np.sin(x), '*')
plt.plot(x, np.cos(x), '.')
plt.show()
```


![png](1-1_files/1-1_3_0.png)


# 画子图(matplab风格)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100) 
plt.figure()

# 子图一
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
# 子图二
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
# 子图三
plt.subplot(2, 2, 3)
plt.plot(x, np.tan(x))
# 子图四
plt.subplot(2, 2, 4)
plt.plot(x, np.arctan(x))
```




    [<matplotlib.lines.Line2D at 0x219404897f0>]




![png](1-1_files/1-1_5_1.png)


# 画子图(面向对象风格)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(2)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))

```




    [<matplotlib.lines.Line2D at 0x2194058ddd8>]




![png](1-1_files/1-1_7_1.png)


# 线性网格图


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.plot(x, np.cos(x))
```




    [<matplotlib.lines.Line2D at 0x2194181bba8>]




![png](1-1_files/1-1_9_1.png)


# 设置颜色、线条


```python
'''
    设置线条颜色
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, ax = plt.subplots(2,1)
ax[0].plot(x, np.sin(x - 0))#, color='blue'
ax[0].plot(x, np.sin(x - 1))#, color='orange'
ax[0].plot(x, np.sin(x - 2))#, color='red'
ax[0].plot(x, np.sin(x - 3))#, color='green'

ax[1].plot(x, np.sin(x - 0), color='blue')
ax[1].plot(x, np.sin(x - 1), color='orange')
ax[1].plot(x, np.sin(x - 2), color='red')
ax[1].plot(x, np.sin(x - 3), color='green')
```




    [<matplotlib.lines.Line2D at 0x21941b77320>]




![png](1-1_files/1-1_11_1.png)



```python
'''
    设置形状、颜色
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0), linestyle='-',color='blue')
plt.plot(x, np.sin(x - 1), linestyle='--',color='orange')
plt.plot(x, np.sin(x - 2), linestyle='-.',color='red')
plt.plot(x, np.sin(x - 3), linestyle=':',color='green')
```




    [<matplotlib.lines.Line2D at 0x21941bf2828>]




![png](1-1_files/1-1_12_1.png)



```python
'''
    综合设置形状、颜色
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x - 0),'-g')
plt.plot(x, np.sin(x - 1),'--c')
plt.plot(x, np.sin(x - 2),'-.k')
plt.plot(x, np.sin(x - 3), ':r')
```




    [<matplotlib.lines.Line2D at 0x21941c5b390>]




![png](1-1_files/1-1_13_1.png)


# 设置坐标轴


```python
"""
    逆序
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.xlim(11, -1)
plt.ylim(1.5, -1.5)

```




    (1.5, -1.5)




![png](1-1_files/1-1_15_1.png)



```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5)

```




    (-1.5, 1.5)




![png](1-1_files/1-1_16_1.png)


# 设置标签


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")
```




    Text(0, 0.5, 'sin(x)')




![png](1-1_files/1-1_18_1.png)



```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
# plt.axis('equal')

plt.legend()
```




    <matplotlib.legend.Legend at 0x21941e4b860>




![png](1-1_files/1-1_19_1.png)

