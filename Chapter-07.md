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
