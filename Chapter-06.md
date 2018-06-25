# 第六天
html和css
## html

#### 什么是html
HTML 是用来描述网页的一种语言。HTML 是超文本标记语言的缩写（Hyper Text Markup Language）
使用标记标签来描述网页。

#### HTML 标签
HTML 标记标签通常被称为 HTML 标签 (HTML tag)

+ HTML 标签是由尖括号包围的关键词，比如 <html>
+ HTML 标签通常是成对出现的，比如 <b> 和 </b>
+ 标签对中的第一个标签是开始标签，第二个标签是结束标签
+ 开始和结束标签也被称为开放标签和闭合标签

#### 网页
网页就是html 文档，Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。
浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：
````buildoutcfg
<html>
<head>
<title>
我是title
</title>
</head>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html
````

如果浏览器线上乱码，设置下字符集
````buildoutcfg
<meta charset=utf-8" />
````

<html> 与 </html> 之间的文本描述网页
<head> 与  </head>之间用来定义文档的头部，它是头部所有标签的容器
<title> 与 </title>之间用来定义文档在浏览器标签上显示的标题
<body> 与 </body> 之间的文本是可见的页面内容
<h1> 与 </h1> 之间的文本定义文档内的标题
<p> 与 </p> 之间的文本被显示为段落


#### html 标题

HTML 标题（Heading）是通过 <h1> - <h6> 等标签进行定义的。

````buildoutcfg
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
````

#### HTML 段落
HTML 段落是通过 <p> 标签进行定义的。
````buildoutcfg
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
````
注意在html里面换行是没有意义的

#### HTML 链接
````buildoutcfg
<a href="http://www.longtengtest.com/">龙腾测试</a>
````

#### HTML 图像

````buildoutcfg
<img src="ltcs.jpg" width="104" height="142" />
````

#### html 元素

HTML 文档是由 HTML 元素定义的，HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码
````buildoutcfg
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>标题</title>
</head>
<body>

</body>
</html>
````
<html>和</html>之间是html元素，<head>和</head> 之间是head元素，可以看到元素是可以嵌套的

#### HTML 属性
HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
属性总是以名称/值对的形式出现，比如：name="value"。
属性总是在 HTML 元素的开始标签中规定。

这里href就是标签<a>的属性
````buildoutcfg
<a href="http://www.longtengtest.com/">龙腾测试</a>
````

属性例子1,对齐方式

````buildoutcfg
<h1 align="center">对齐范式</h1>
````

尝试将center改成left，reight查看下效果

属性例子2，背景颜色

````buildoutcfg
<body bgcolor="yellow">
</body>
````
尝试将yellow 改成blue，red


#### HTML 折行
在不产生新段落的情况下换行<br/>
````buildoutcfg
<p>This is<br />a para<br />graph with line breaks</p>
````
注意: 当显示页面时，浏览器会移除源代码中多余的空格和空行。所有连续的空格或空行都会被算作一个空格。
需要注意的是，HTML 代码中的所有连续的空行（换行）也被显示为一个空格。


#### HTML 样式
````buildoutcfg
<h1>Look! Styles and colors</h1>
<p style="font-family:verdana;color:red">
    This text is in Verdana and red
</p>

<p style="font-family:times;color:green">
    This text is in Times and green
</p>

<p style="font-family:KaiTi;font-size:30px">
    龙腾测试
</p>
````

style 属性的作用,提供了一种改变所有 HTML 元素的样式的通用方法.内嵌式css
font-family 规定元素的字体，
常见英文字体 "times"、"courier"、"arial"、"serif"、"sans-serif"、"cursive"、"fantasy"、"monospace"
常见中文字体 黑体"SimHei"、新宋"NSimSun"、微软雅黑"Microsoft YaHei" 、楷体"KaiTi"
font-size 字体大小font-size 字体大小

例子文本对齐
````buildoutcfg
<h1 style="text-align:center">This is a heading</h1>
<p>The heading above is aligned to the center of this page.</p>
````
与<h1 align="center">对齐范式</h1> 效果相同


#### HTML 注释标签
````buildoutcfg
<!-- 在此处写注释 -->
````
在开始标签中有一个惊叹号，但是结束标签中没有。
浏览器不会显示注释，但是能够帮助记录您的 HTML 文档

````buildoutcfg
<!-- 这是一段注释 -->

<p>这是一个段落。</p>

<!-- 记得在此处添加信息 -->
````
#### 列表
有序列表是一列项目，列表项目使用数字进行标记。
有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。

````buildoutcfg
<ol>
<li>咖啡</li>
<li>牛奶</li>
</ol>
```

自定义列表不仅仅是一列项目，而是项目及其注释的组合。
自定义列表以 <dl> 标签开始。每个自定义列表项以 <dt> 开始。每个自定义列表项的定义以 <dd> 开始。

````buildoutcfg
<dl>
<dt>咖啡</dt>
<dd>黑色热饮</dd>
<dt>牛奶</dt>
<dd>白色冷饮</dd>
</dl>
````

例子1
````buildoutcfg
<h4>Disc 项目符号列表：</h4>
<ul type="disc">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ul>  

<h4>Circle 项目符号列表：</h4>
<ul type="circle">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ul>  

<h4>Square 项目符号列表：</h4>
<ul type="square">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ul>  
````

例子2

````buildoutcfg
<h4>数字列表：</h4>
<ol>
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ol>  

<h4>字母列表：</h4>
<ol type="A">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ol>  

<h4>小写字母列表：</h4>
<ol type="a">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ol>  

<h4>罗马字母列表：</h4>
<ol type="I">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ol>  

<h4>小写罗马字母列表：</h4>
<ol type="i">
 <li>苹果</li>
 <li>香蕉</li>
 <li>柠檬</li>
 <li>桔子</li>
</ol>  
````

例子3

````buildoutcfg
<dl>
   <dt>计算机</dt>
   <dd>用来计算的仪器 ... ...</dd>
   <dt>显示器</dt>
   <dd>以视觉方式显示信息的装置 ... ...</dd>
</dl>

````

嵌套列表
例子1
````buildoutcfg
<h4>一个嵌套列表：</h4>
<ul>
  <li>咖啡</li>
  <li>茶
    <ul>
    <li>红茶</li>
    <li>绿茶</li>
    </ul>
  </li>
  <li>牛奶</li>
</ul>
````

例子2

````buildoutcfg
<h4>一个嵌套列表：</h4>
<ul>
  <li>咖啡</li>
  <li>茶
    <ul>
    <li>红茶</li>
    <li>绿茶
      <ul>
      <li>中国茶</li>
      <li>非洲茶</li>
      </ul>
    </li>
    </ul>
  </li>
  <li>牛奶</li>
</ul>
````

#### 表格

表格由 <table> 标签来定义。每个表格均有若干行（由 <tr> 标签定义），每行被分割为若干单元格（由 <td> 标签定义）。
字母 td 指表格数据（table data），即数据单元格的内容。
数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

````buildoutcfg
<table border="1">
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
````

border 边框属性
如果不定义边框属性，表格将不显示边框。有时这很有用，但是大多数时候，我们希望显示边框。
使用边框属性来显示一个带有边框的表格

表格的表头
表格的表头使用 <th> 标签进行定义。

````buildoutcfg
<table border="1">
<tr>
<th>Heading</th>
<th>Another Heading</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
````

#### HTML 表单
HTML 表单用于搜集不同类型的用户输入
HTML 表单包含表单元素。
表单元素指的是不同类型的 input 元素、复选框、单选按钮、提交按钮等等

<input> 元素
<input> 元素是最重要的表单元素。
<input> 元素有很多形态，根据不同的 type 属性
text     定义常规文本输入
radio	 定义单选按钮输入（选择多个选择之一）
submit	 定义提交按钮（提交表单）

例子1
```buildoutcfg
<form>
 First name:<br>
<input type="text" name="firstname">
<br>
 Last name:<br>
<input type="text" name="lastname">
</form> 
```
表单本身并不可见。还要注意文本字段的默认宽度是 20 个字符


<input type="radio"> 定义单选按钮。
单选按钮允许用户在有限数量的选项中选择其中之一：

```buildoutcfg
<form>
<input type="radio" name="sex" value="male" checked>Male
<br>
<input type="radio" name="sex" value="female">Female
</form> 
```

<input type="submit"> 定义用于向表单处理程序（form-handler）提交表单的按钮。
表单处理程序通常是包含用来处理输入数据的脚本的服务器页面。
表单处理程序在表单的 action 属性中指定：

````buildoutcfg
<form action="action_page.php">
First name:<br>
<input type="text" name="firstname" value="Mickey">
<br>
Last name:<br>
<input type="text" name="lastname" value="Mouse">
<br><br>
<input type="submit" value="Submit">
</form> 
````

action 属性定义在提交表单时执行的动作。
向服务器提交表单的通常做法是使用提交按钮。
通常，表单会被提交到 web 服务器上的网页。
在上面的例子中，指定了某个服务器脚本来处理被提交表单：

method 属性规定在提交表单时所用的 HTTP 方法（GET 或 POST）

Name 属性
如果要正确地被提交，每个输入字段必须设置一个 name 属性

select 元素（下拉列表）

````buildoutcfg
<select name="cars">
<option value="volvo">Volvo</option>
<option value="saab">Saab</option>
<option value="fiat" selected>Fiat</option>
<option value="audi">Audi</option>
</select>
````
<option> 元素定义待选择的选项。
列表通常会把首个选项显示为被选选项。
能够通过添加 selected 属性来定义预定义选项

<textarea> 元素定义多行输入字段（文本域）
````
<textarea name="message" rows="10" cols="30">
The cat was playing in the garden.
</textarea>
````

<button> 元素定义可点击的按钮
````
<button type="button" onclick="alert('Hello World!')">Click Me!</button>
````

value 属性
value 属性规定输入字段的初始值

````
<form action="">
 First name:<br>
<input type="text" name="firstname" value="John">
<br>
 Last name:<br>
<input type="text" name="lastname">
</form> 
````

readonly 属性规定输入字段为只读（不能修改）
```buildoutcfg
<form action="">
 First name:<br>
<input type="text" name="firstname" value="John" readonly>
<br>
 Last name:<br>
<input type="text" name="lastname">
</form> 
```

size 属性规定输入字段的尺寸（以字符计）
````
<form action="">
 First name:<br>
<input type="text" name="firstname" value="John" size="40">
<br>
 Last name:<br>
<input type="text" name="lastname">
</form> 
````

## css
CSS 指层叠样式表 (Cascading Style Sheets),样式定义如何显示 HTML 元素

样式表定义如何显示 HTML 元素,样式通常保存在外部的 .css 文件中。
通过仅仅编辑一个简单的 CSS 文档，外部样式表使你有能力同时改变站点中所有页面的布局和外观。
css分为内部样式表（位于head内）、外部样式表、内联样式（在 HTML 元素内部）
CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明
selector {declaration1; declaration2; ... declarationN }

选择器通常是您需要改变样式的 HTML 元素。
每条声明由一个属性和一个值组成。
属性（property）是您希望设置的样式属性（style attribute）。每个属性有一个值。属性和值被冒号分开。

selector {property: value}

例子
```buildoutcfg
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        p
        {
            color:red;
            text-align:center;
        }
</style>
</head>
<body>
<p>Hello World!</p>
<p>这个段落采用CSS样式化。</p>
</body>
</html>
```

