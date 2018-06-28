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
CSS 指层叠样式表 (Cascading Style Sheets),它允许我们将布局和设计添加到html页面，
并且它允许我们从元素到页面共享这些样式。
在我们了解所有功能之前，我们先来了解几个概念

### 理解css术语

#### Selectors
当元素被添加到网页中时，可以使用CSS进行样式化。选择器用来定位HTML中的哪些元素应用样式（例如颜色，大小和位置）
选择器可以包含不同限定符（元素类型，class，id。。）的组合，以选择独特的元素。例如，我们可能希望选择页面上的每个段落，
或者我们可能只想在页面上选择一个特定的段落。
选择器通常以属性值为目标，例如id或class值，或者定位元素的类型，例如<h1>或<p>

在CSS中，选择器后跟大括号{}，其中包含要应用于所选元素的样式。下面的选择器是针对所有的<p>元素
````
p { ... }
````
#### Properties
一旦选择了元素，属性将确定将应用于该元素的样式，属性名称位于大括号{}内的选择器之后，紧接在冒号之后：。
我们可以使用许多属性，例如背景，颜色，字体大小，高度和宽度，并且通常会添加新属性。
在下面的代码中，我们定义了要应用于所有<p>元素的颜色和字体大小属性。
````
p {
  color: ...;
  font-size: ...;
}

````

#### Values
到目前为止，我们已经选择了一个带有选择器的元素，并确定了我们想要使用属性的样式。现在我们可以用一个值来确定该属性的行为
值可以被识别为冒号和分号之间的文本。在这里，我们选择所有<p>元素，并将color属性的值设置为橙色，并将font-size属性的值设置为16像素。
````
p {
  color: orange;
  font-size: 16px;
}

````

在CSS中，我们的规则集以选择器开头，后面紧跟着大括号。在这些大括号内是由属性和值对组成的声明，每个声明都以一个属性开头
，后面跟着冒号，属性值，最后是分号。
[img](./Chapter-06-code/css-syntax-outline.png)

### 使用选择器

如前所述，选择器表示对哪些HTML元素进行样式化。充分了解如何使用选择器以及如何利用选择器非常重要。
第一步是熟悉不同类型的选择器。我们将从最常见的选择器开始：类型，类和ID选择器。

#### Type Selectors
类型选择器按元素类型定位元素。例如，如果我们希望定位所有的div元素，我们将使用div的类型选择器
以下代码显示了除法元素的类型选择器以及它选择的相应HTML

````
# css
div { ... }

# html
<div>...</div>          
<div>...</div>
````

#### Class Selectors
类选择器允许我们根据元素的类属性值选择一个元素。类选择器比类型选择器更具体，因为它们选择一组特定的元素而不是一种类型的所有元素。

类选择器允许我们通过跨多个元素使用相同的类属性值，一次将相同的样式应用于不同的元素。

在CSS中，类由前导点表示，后跟类属性值。下面类选择器将选择包含awesome类属性值的任何元素，包括分割元素和段落元素

````
# css
.awesome { ... }
# html
<div class="awesome">...</div>
<p class="awesome">...</p>
````
#### ID Selectors
ID选择器比类选择器更精确，因为它们一次只能定位一个独特的元素。

就像类选择器使用元素的类属性值作为选择器一样，ID选择器使用元素的id属性值作为选择器。

无论它们出现在哪种类型的元素上，每个页面使用的id属性值必须唯一。如果使用它们应该保留用于重要元素。

在CSS中，ID选择符由前导散列符号＃表示，后跟id属性值。这里ID选择器将只选择包含shayhowe的id属性值的元素。

````
# css
#shayhowe { ... }
<div id="shayhowe">...</div>
````
### 引用css
为了让我们的CSS对HTML生效，我们需要在我们的HTML中引用我们的CSS文件

引用我们的CSS的最佳做法是将所有样式包含在单个外部样式表中，该样式表从我们的HTML文档的<head>元素中引用

使用单个外部样式表可以让我们在整个网站上使用相同的样式，并在整个网站范围内快速进行更改。

其他用于引用CSS的选项包括使用内部样式和内联样式

要创建我们的外部CSS样式表，我们需要创建一个扩展名为.css的文件，我们的CSS文件应保存在我们的HTML文件所在的相同文件夹或子文件夹中

在HTML文档的<head>元素中，<link>元素用于定义HTML文件和CSS文件之间的关系
因为我们链接到CSS，我们使用rel属性和stylesheet的值来指定它们的关系。
此外，href属性用于标识CSS文件的位置或路径。

考虑下面一个引用单个外部样式表的HTML文档<head>元素的例子。
````
<head>
  <link rel="stylesheet" href="main.css">
</head>

````

为了CSS正确呈现，href属性值的路径必须直接关联到我们的CSS文件保存的位置，
在前面的示例中，main.css文件存储在与HTML文件相同的位置。

如果我们的CSS文件位于子目录或子文件夹内，则href属性值需要相应地与此路径相关联。
例如，如果我们的main.css文件存储在名为stylesheets的子目录中，那么href属性值将是stylesheets/main.css

### 层叠 Cascad
 
我们通过几个例子来了解css是如何层叠渲染页面的。在CSS中，所有样式从样式表顶部到底部分成多层，允许不同的层样式覆盖
例如，假设我们选择样式表顶部的所有段落元素，并将它们的背景颜色设置为橙色，并将它们的字体大小设置为24像素
然后在样式表的底部，我们再次选择所有段落元素，并将其背景颜色设置为绿色，如此处所示

[示例1](./Chapter-06-code/css-example1.html)
由于将背景色设置为绿色的段落选择符位于将背景色设置为橙色的段落选择符之后
它将在层叠中优先，所有段落将以绿色背景显示。字体大小将保持24像素，因为第二个段落选择器不能识别新的字体大小。

[示例2](./Chapter-06-code/css-example2.html)
层叠样式也适用于单个选择器内的属性。例如，再说一遍，我们选择所有的段落元素并将它们的背景颜色设置为橙色。
然后直接在橙色背景属性和值声明的下方，我们添加另一个属性和值声明，将背景颜色设置为绿色，如示例所示。
由于绿色背景颜色声明位于橙色背景颜色声明之后，因此它将取代橙色背景，并且与以前一样，我们的段落将以绿色背景显示。


#### 选择器权重

CSS中的每个选择器都具有特定权重，元素类型，class和ID选择器。这些选择器中的每一个具有不同的权重。
类型选择器具有最低的权重并且保持0-0-1的点值，class选择器具有中等权重并且保持0-1-0的点值，
ID选择器具有高权重并且保持1-0-0的点值。
正如我们所看到的，权重使用三列进行计算。第一列计数ID选择器，第二列计数class选择器，第三列计数元素类型选择器。

这里需要注意的是，ID选择器比class选择器具有更高的权重，并且class选择器具有比元素类型选择器更高的权重
选择器的权重越高，发生样式冲突时选择器就越有优势。
例如，如果在一个地方使用元素类型选择器并在另一个地方使用ID选择器来选择段落元素，
无论ID选择器在级联中出现的位置如何，ID选择器都将优先于类型选择器
[示例3](./Chapter-06-code/css-example3.html)


这里我们有一个带有food id属性值的段落元素。在我们的CSS中，该段落由两种不同的选择器选择：一个元素类型选择器和一个ID选择器
尽管元素类型选择器在级联中的ID选择器之后，但ID选择器优先于元素类型选择器，因为它具有更高的权重;因此该段落将以绿色背景显示

不同元素类型选择器的权重非常重要。

#### 组合选择器

到目前为止，我们已经看过如何分别使用不同类型的选择器，但我们也需要知道如何一起使用这些选择器。
通过组合选择器，我们可以更具体地了解我们想要选择的元素或元素组。

例如，假设我们要选择位于具有hotdog class属性值的元素内的所有段落元素，并将其背景颜色设置为棕色。
但是，如果其中一个段碰巧具有mustard的class属性值，我们希望将其背景颜色设置为黄色。

[示例4](./Chapter-06-code/css-example4.html
当选择器组合时，应该从右到左阅读.最右边的选择器直接位于花括号之前，被称为key选择器。
key选择器确切地标识样式将应用于哪个元素。key 选择器左侧的任何选择器都将用作预选者

上面的第一个组合选择器.hotdog p包含两个选择器：class 和 元素类型
这两个选择器由一个空格分开，key 选择器是一个针对段落元素的类型选择器。
而且因为这个元素类型选择器是用一个.hotdog class选择器进行预选择的，
所以完整的组合选择器将只选择位于具有class属性值为hotlog的元素内的段落元素

上面的第二个选择器.hotdog p.mustard包含三个选择器，两个class选择器和一个元素类型选择器。
第二个选择器和第一个选择器之间的唯一区别在于mustard的class选择器在段落类型选择器的末尾。
由于新的class选择器mustard一直落在组合选择器的右侧，.mustard是key选择器

在前面的组合选择器.hotdog p.mustard中，在hotdog class选择器和段落类型选择器之间存在空格，
但段落类型选择器和mustard class选择器之间没有

由于段落类型选择器和mustard class选择器之间没有空格，这意味着选择器仅选择mustard class的段落元素。
如果删除了段落类型选择器，并且mustard class选择器在其两侧都有空格，它将选择具有mustard类的任何元素，而不仅仅是段落

最佳做法是不要用类型选择器为class选择器的前缀，.hotdog .mustard