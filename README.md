## morilab

### imgcrip.py

#### get4PlatesFromAImage(filename, x, y, width, height)
スキャン画像から4つのプレート画像を切り出す  
座標の指定には、スキャン画像の縦横の割合で指定する  

```python
x = np.array([204, 204, 1823, 1824])/3200
y = np.array([47, 2063, 42, 2063])/4000
width = np.array([1302, 1302, 3129, 3122])/3200
height = np.array([1945, 3961, 1940, 3961])/4000

get4PlatesFromAImage("./scanimg.jpg", x, y, width, height)
```