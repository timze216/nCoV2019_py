获取 nCoV2019 统计数据；

[TOC]

---

## 获取数据

| 属性/方法       | 数据               |
| --------------- | ------------------ |
| `.qq_source()`  | 使用QQ news数据    |
| `.data_url`     | 数据来源URL        |
| `.chinaDayList` | 国内每日通报       |
| `.chinaDayADD`  | 国内每日新增通报   |
| `.global_area`  | 全球地区数据       |
| `.china`        | 国内各省数据       |
| `.get()`        | 获取制定地区数据   |
| `.search('')`   | 有记录地区名称查询 |
|                 |                    |



## Example

```python
import nCoV2019
nCov = nCoV2019.qq_source()
```

```
截止 2020-02-04 11:02:52; 2019nCoV 已蔓延 23 个国家/地区
中国累计 20471 例确诊，自昨日00:00新增3266
```




```python
# 卫健委每日通报
nCov.chinaDayList
# 卫健委每日通报新增
nCov.chinaDayADD
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
      <th>confirm</th>
      <th>suspect</th>
      <th>dead</th>
      <th>heal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01.20</td>
      <td>77</td>
      <td>27</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>01.21</td>
      <td>149</td>
      <td>53</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>01.22</td>
      <td>131</td>
      <td>257</td>
      <td>8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>01.23</td>
      <td>259</td>
      <td>680</td>
      <td>8</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>01.24</td>
      <td>444</td>
      <td>1118</td>
      <td>16</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>01.25</td>
      <td>688</td>
      <td>1309</td>
      <td>15</td>
      <td>11</td>
    </tr>
    <tr>
      <th>6</th>
      <td>01.26</td>
      <td>769</td>
      <td>3806</td>
      <td>24</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>01.27</td>
      <td>1771</td>
      <td>2077</td>
      <td>26</td>
      <td>9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>01.28</td>
      <td>1459</td>
      <td>3248</td>
      <td>26</td>
      <td>43</td>
    </tr>
    <tr>
      <th>9</th>
      <td>01.29</td>
      <td>1737</td>
      <td>4148</td>
      <td>38</td>
      <td>21</td>
    </tr>
    <tr>
      <th>10</th>
      <td>01.30</td>
      <td>1982</td>
      <td>4812</td>
      <td>43</td>
      <td>47</td>
    </tr>
    <tr>
      <th>11</th>
      <td>01.31</td>
      <td>2102</td>
      <td>5019</td>
      <td>46</td>
      <td>72</td>
    </tr>
    <tr>
      <th>12</th>
      <td>02.01</td>
      <td>2590</td>
      <td>4562</td>
      <td>45</td>
      <td>85</td>
    </tr>
    <tr>
      <th>13</th>
      <td>02.02</td>
      <td>2829</td>
      <td>5173</td>
      <td>57</td>
      <td>147</td>
    </tr>
    <tr>
      <th>14</th>
      <td>02.03</td>
      <td>3235</td>
      <td>5072</td>
      <td>64</td>
      <td>157</td>
    </tr>
  </tbody>
</table>



```python
# 全球数据
nCov.global_area
```



`.get()`  对省级地区返回省级统计以及辖区各市数据

```python
# 国内各省市数据
nCov.get("武汉")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>confirm</th>
      <th>suspect</th>
      <th>dead</th>
      <th>heal</th>
      <th>confirm_add</th>
      <th>suspect_add</th>
      <th>dead_add</th>
      <th>heal_add</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>武汉</td>
      <td>6384</td>
      <td>0</td>
      <td>313</td>
      <td>303</td>
      <td>1242</td>
      <td>0</td>
      <td>48</td>
      <td>79</td>
    </tr>
  </tbody>
</table>





```python
nCov.get("湖北")
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>city</th>
      <th>confirm</th>
      <th>suspect</th>
      <th>dead</th>
      <th>heal</th>
      <th>confirm_add</th>
      <th>suspect_add</th>
      <th>dead_add</th>
      <th>heal_add</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>湖北</td>
      <td>13522</td>
      <td>0</td>
      <td>414</td>
      <td>396</td>
      <td>2345</td>
      <td>0</td>
      <td>64</td>
      <td>97</td>
    </tr>
    <tr>
      <th>1</th>
      <td>武汉</td>
      <td>6384</td>
      <td>0</td>
      <td>313</td>
      <td>303</td>
      <td>1242</td>
      <td>0</td>
      <td>48</td>
      <td>79</td>
    </tr>
    <tr>
      <th>2</th>
      <td>黄冈</td>
      <td>1422</td>
      <td>0</td>
      <td>19</td>
      <td>36</td>
      <td>176</td>
      <td>0</td>
      <td>2</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>孝感</td>
      <td>1120</td>
      <td>0</td>
      <td>17</td>
      <td>4</td>
      <td>202</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>随州</td>
      <td>641</td>
      <td>0</td>
      <td>6</td>
      <td>3</td>
      <td>183</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>襄阳</td>
      <td>632</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>84</td>
      <td>0</td>
      <td>1</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>荆州</td>
      <td>613</td>
      <td>0</td>
      <td>7</td>
      <td>4</td>
      <td>114</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>宜昌</td>
      <td>452</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>60</td>
      <td>0</td>
      <td>2</td>
      <td>-1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>黄石</td>
      <td>405</td>
      <td>0</td>
      <td>2</td>
      <td>9</td>
      <td>71</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>荆门</td>
      <td>400</td>
      <td>0</td>
      <td>14</td>
      <td>3</td>
      <td>55</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>咸宁</td>
      <td>348</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>鄂州</td>
      <td>332</td>
      <td>0</td>
      <td>18</td>
      <td>2</td>
      <td>26</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12</th>
      <td>十堰</td>
      <td>291</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>35</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>仙桃</td>
      <td>188</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
      <td>19</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>恩施州</td>
      <td>123</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>12</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>天门</td>
      <td>117</td>
      <td>0</td>
      <td>10</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>潜江</td>
      <td>44</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>9</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>神农架</td>
      <td>10</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>地区待确认</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>19</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>





使用 `search` 方法进行地名查询：

```python
nCov.search('六')
```


    ['兵团第六师五家渠市', '六盘水', '六安']

部分地名带行政单位，比如"丽江"，"丽江市"，可以用search 来确定。

```python
# 地名查询，部分地名带行政单位
# eg: 丽江 vs 丽江市
nCov.search('丽江')
```


    ['丽江市']



![image-20200204125921879](./png/screenshot.png)

