## morilab

### imgcrip.py

#### get4PlatesFromAImage(filename, save_as, x, y, width, height)
スキャン画像から4つのプレート画像を切り出す  
座標の指定には、スキャン画像の縦横の割合で指定する  

```python
x = np.array([204, 204, 1823, 1824])/3200
y = np.array([47, 2063, 42, 2063])/4000
width = np.array([1302, 1302, 3129, 3122])/3200
height = np.array([1945, 3961, 1940, 3961])/4000
save_as = ["a.jpg", "b.jpg", "c.jpg", "d.jpg"]

get4PlatesFromAImage("./scanimg.jpg", save_as, x, y, width, height)
```

### scanner.py

#### scan(option, save_as)
オプション（画質、色、透過・反射）と保存名を指定してスキャンを行う  

```python
option = "--resolution 360\
--mode Color\
--source TPU8x10\
--format=tiff".split() #.split()で文字列を配列に変換する
save_as = "a.tiff"
scan(option, save_as)
```
