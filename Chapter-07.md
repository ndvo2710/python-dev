## 第七天

### Box Model 盒子模型

现在我们要深入一点，看看网页中元素的显示方式以及它们的大小。

在这个过程中，我们将讨论所谓的盒子模型以及它如何与HTML和CSS一起使用

**如何显示元素**

究竟如何显示元素，由display属性决定。每个元素都有一个默认的display属性值;
但是，与所有其属性的值一样，该值可能会被覆盖。最常见的是block, inline, inline-block, 和none

每个元素都有默认的display值，根据display的值可分为 块（block）元素，内联（inline）元素和 内嵌（inline-block）元素


block元素独占一行，并且可以设置width,height，margin，padding属性。

inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化，
inline元素设置width,height属性无效

inline-block 元素呈现为inline对象，让block元素不再独占一行，多个block元素可以同排一行，且元素具有block的属性，
可设置width、height是block和inline元素的综合体

none 使元素不显示


我们可以通过在CSS中设置显示display的值来更改元素的显示属性值。

[示例](./Chapter-07-code/example1.html)

**什么是Box Model(盒子模型)**

根据盒子模型概念，页面上的每个元素都是一个矩形框，并且可以具有width(宽度)，height(高度)，padding(填充)，border(边框)和margin(边距)。
*页面上的每个元素都是一个矩形框* 每个页面上的每个元素都符合盒子模型

每个元素都是一个矩形框，并且有width、height、padding、border、margin几个属性决定了该框的大小.
[示例]

````
div {
  border: 6px solid #949599;
  height: 100px;
  margin: 20px;
  padding: 20px;
  width: 400px;
}

````

根据盒子模型，可以使用下面的公式计算元素的总宽度

````
margin-right + border-right + padding-right + width + padding-left + border-left + margin-left

````

根据盒子模型，元素的总高度可以使用以下公式计算：
````
margin-top + border-top + padding-top + height + padding-bottom + border-bottom + margin-bottom

````
使用公式，我们可以找到示例代码的总高度和宽度

````
Width: 492px = 20px + 6px + 20px + 400px + 20px + 6px + 20px
Height: 192px = 20px + 6px + 20px + 100px + 20px + 6px + 20px
````
盒子模型毫无疑问是HTML和CSS中容易混乱的一部分。我们将width属性值设置为400像素，但元素的实际宽度为492像素
为了确定箱子的实际尺寸，我们需要考虑箱子所有四边的填充，边框和边距

**Width & Height**

每个元素都有默认的宽度和高度。宽度和高度可以是0像素，但默认情况下，浏览器将呈现每个元素的大小.
根据元素的显示方式，默认宽度和高度可能足够.如果元素是页面布局的关键，则可能需要指定的width和height属性值
在这种情况下，可以指定非内联元素的属性值。

元素的默认宽度取决于其显示值。块级元素的默认宽度为100％，占用整个可用的水平空间.
inline和inline-block元素水平扩展和收缩以适应其内容,内联级元素不能具有固定大小，因此宽度和高度属性仅与非内联元素相关
要为非内联元素设置特定宽度，请使用width属性：

````
div {
  width: 400px;
}
````


元素的默认高度由其内容决定,元素将根据需要垂直扩展和收缩以适应其内容.要为非内联元素设置特定高度，请使用height属性：
````
div {
  height: 100px;
}

````
Margin(边距) & Padding(填充)

根据元素的不同，浏览器可以将默认边距和填充应用于元素，以帮助提高易读性和清晰度。
margin属性允许我们设置元素周围的空间量，元素的边距（margin）落在边框（border）之外，并且颜色完全透明。
边距可用于帮助将元素定位在页面上的特定位置，与所有其他元素保持安全距离。
````
div {
  margin: 20px;
}

````

填充（padding）属性与边距（margin）属性非常相似;但是，如果元素具有边框，则它落在元素的边框内。

当涉及边距和填充时，内联（inline）元素的影响与块（block）和内嵌（inline-block）元素略有不同，magin对内联元素（inline）仅在
水平方向起作用即左右。padding在水平和垂直均起作用，但会渗透到上下元素中

**设置magrin和padding**

````
div {
  margin: 20px;
}
````
以上方式设置元素的4个方向margin值均为20px

如果上下和左右的值不同,设置方式如下
````
div {
  margin: 10px 20px;
}

````

10px 为上下的值，20px为左右的值

如果上下左右各不同。设置方式如下
````
div {
  margin: 10px 20px 0 15px;
}

````

上（top） 10px，右（right）20px，下（bottom）0,左（left）15px  方向为顺时针

也可以单独设置某个方向的值，如：
````
div {
  margin-top: 10px;
  padding-left: 6px;
}

````

边距（magin）和填充（padding）是完全透明的，不接受任何颜色值。但是，它们显示相对元素的背景颜色
对于边距，我们看到父元素的背景颜色，对于填充，我们看到应用填充的元素的背景颜色

**Borders**

边框（border）位于填充（padding）和边距（margin）之间，提供围绕元素的轮廓。
边框（border）属性需要三个值：宽度（width），样式（style）和颜色（color）。
````
div {
  border: 6px solid #949599;
}

````

边框（border）的style常见的有solid, double, dashed, dotted, 和 none

[示例](./Chapter-07-code/example3.html)


单独设置border的各个边，border-top, border-right, border-bottom, 和 border-left
````
div {
  border-bottom: 6px solid #949599;
}

````

另外，可以将各个边界侧的样式控制在更精细的水平。例如，如果我们只希望更改底部边框的宽度，我们可以使用以下代码
````
div {
  border-bottom-width: 12px;
}

````
可选top, right, bottom, 和left

border-radius属性，使我们能够对元素的角进行圆角处理。border-radius属性接受长度单位，包括百分比和像素，用于标识元素的角的半径
````
div {
  border-radius: 5px;
}

````

[示例](./Chapter-07-code/example4.html)



### css定位

**浮动定位**
在页面上定位元素的一种方法是使用float属性。浮动属性非常通用，可以以多种不同方式使用。
从本质上讲，float属性允许我们获取一个元素，将其从页面的正常流中移除，并将其放置在其父元素的左侧或右侧



当float属性同时用于多个元素时，它提供了通过直接相邻或相对浮动元素来创建布局的能力，如多列布局中所示

````
img {
  float: left;
}

````
未使用float属性
[示例](./Chapter-07-code/example5.html)

这里的`<section>`和`<aside>`元素作为块级元素.默认情况下，它们将堆叠在一起
但是，我们希望这些元素并排放置。将`<section>`浮动到左侧，将`<aside>`浮动到右侧
我们可以将它们定位为彼此相对的两列。我们的CSS应该是这样的

````
section {
  float: left;
}
aside {
  float: right;
}
````


作为参考，当一个元素浮动时，它将一直浮动到其父元素的边缘。如果没有父元素，则浮动元素将一直浮动到页面边缘
当我们浮动一个元素时，我们将它从HTML文档的正常流程中取出。这会导致该元素的宽度默认为其中内容的宽度
有时，例如当我们为可重用布局创建列时，不希望出现这种情况.可以通过向每列添加固定宽度属性值来更正它。
另外，为了防止浮动元素彼此接触，导致一个元素的内容直接位于另一个元素的内容旁边，我们可以使用margin属性在元素之间创建空间。
在这里，我们扩展了前面的代码块，为每列添加了边距和宽度，以更好地塑造我们期望的结果
````
section {
  float: left;
  margin: 0 1.5%;
  width: 63%;
}
aside {
  float: right;
  margin: 0 1.5%;
  width: 30%;
}

````

[示例](./Chapter-07-code/example6.html)

浮动可能会更改元素的显示值
浮动元素时，识别元素从页面的正常流中移除也很重要，这可能会更改元素的默认显示值。
float属性依赖于显示值为block的元素，如果元素的默认显示值尚未显示为block元素，则可能会更改该元素的默认显示值。

例如，显示值为inline的元素（例如`<span>`inline元素）将忽略任何height或width属性值
但是，如果inline元素被浮动，其显示值将更改为block，然后它可以接受高度或宽度属性值


有两列我们可以将一列向左浮动而另一列向右浮动，但是如果列数更多，我们必须改变我们的方法
比方说，我们希望在`<header>`和`<footer>`元素之间有一行三列。

如果我们删除<aside>元素并使用三个<section>元素，我们的HTML可能如下所示

````
<header>...</header>
<section>...</section>
<section>...</section>
<section>...</section>
<footer>...</footer>

````

要将这三个`<section>`元素放在一个三列的行中，而不是向左浮动一列，向右浮动一列，我们将所有三个`<section>`元素浮动到左侧。
我们还需要调整`<section>`元素的宽度以考虑其他列，并使它们彼此相邻。
````
section {
  float: left;
  margin: 0 1.5%;
  width: 30%;
}

````
这里我们有三列，所有列都具有相等的宽度和边距值，并且全部浮动到左侧。
[示例](./Chapter-07-code/example7.html)

练习:
网站设计大会





