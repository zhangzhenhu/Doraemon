
Python技巧
-----------

真实案例
~~~~


|image86|

|image87|


下标循环迭代
~~~~~~

之前我们这样操作：
::
    i = 0
    for item in iterable:
        print i, item
        i += 1

现在我们这样操作：
::
    for i, item in enumerate(iterable):
        print i, item

enumerate函数还可以接收第二个参数。就像下面这样：
::
    >>> list(enumerate('abc'))

    [(0, 'a'), (1, 'b'), (2, 'c')]

    >>> list(enumerate('abc', 1))

    [(1, 'a'), (2, 'b'), (3, 'c')]


推导式
~~~~~

你也许知道如何进行列表解析，但是可能不知道字典/集合解析。它们简单易用且高效。就像下面这个例子：
::
    >>> my_list = [i for i in xrange(100)]
    >>> my_dict = {i: i * i for i in xrange(100)}
    >>> my_set = {i * 15 for i in xrange(100)}



强制浮点除法
~~~~~~~~~~~~

python中两个整数除法运算时，默认情况下得到的商也是整数，商的小数部分会被舍弃。
如果想要得到商是浮点数，可以用把除数、被除数强制转换成浮点数再进行除法。
::
    >>> result = 1 / 2
    0
    >>> result = float(1) / 2
    0.5




对Python表达式求值
~~~~~~~~~~~~~~~~~~

我们都知道eval函数，但是我们知道literal_eval函数么？也许很多人都不知道吧。可以用这种操作：
::
    import ast
    my_list = ast.literal_eval(expr)

来代替以下这种操作：
::
    expr = "[1, 2, 3]"
    my_list = eval(expr)

我相信对于大多数人来说这种形式是第一次看见，但是实际上这个在Python中已经存在很长时间了。


列表切片
~~~~~~~~

在python中对列表进行切片是非常有用的功能。
::
    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> a[1:4] = []
    >>> a
    [1, 5, 6, 7]

当然用 `del a[1:4]` 也是可以的，去除偶数项(偶数索引的):
::
    >>> a = [0, 1, 2, 3, 4, 5, 6, 7]
    >>> del a[::2]
    >>> a
    [1, 3, 5, 7]

你可以用以下方法快速逆序排列数列：
::
    >>> a = [1,2,3,4]
    >>> a[::-1] # 其效果等同于 a.reverse()
    [4, 3, 2, 1]

这总方式也同样适用于字符串的逆序：
::
    >>> foo = "yasoob"
    >>> foo[::-1]
    'boosay'


三元运算
~~~~~~~~

三元运算是 if-else 语句的快捷操作，也被称为条件运算。
这里有几个例子可以供你参考，它们可以让你的代码更加紧凑，更加美观。
其语法为
::
    [on_true] if [expression] else [on_false]

示例：
::
    >>> x, y = 50, 25
    >>> small = x if x < y else y
    25


拷贝对象
~~~~~~~~

标准库中的copy模块提供了两个方法来实现拷贝.一个方法是copy,它返回和参数包含内容一样的对象.
::
    >>> import copy
    >> new_list = copy.copy(existing_list)

有些时候,你希望对象中的属性也被复制,可以使用deepcopy方法:
::
    >>> import copy
    >>> new_list_of_dicts = copy.deepcopy(existing_list_of_dicts)

copy(x) Shallow copy operation on arbitrary Python objects.

deepcopy(x, memo=None, _nil=[]) Deep copy operation on arbitrary Python objects.


函数参数默认值的陷阱和原理深究
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

python中一切非基本类型对象都是引用
::
    def generate_new_list_with(my_list=[],
        element= None):
        my_list.append(element)
        return my_list


    list_1 = generate_new_list_with(element=1)
    print list_1
    # [1]
    list_2 = generate_new_list_with(element=2)
    print list_2
    # [1, 2]


可见代码运行结果并不和我们预期的一样。

list_2在函数的第二次调用时并没有得到一个新的list并填入2，
而是在第一次调用结果的基础上append了一个2。为什么会发生这样在其他编程语言中简直就是设计bug一样的问题呢？ 

可见如果参数默认值是在函数编译compile阶段就已经被确定。
之后所有的函数调用时，如果参数不显示的给予赋值，那么所谓的参数默认值不过是一个指向那个在compile阶段就已经存在的对象的指针。如果调用函数时，没有显示指定传入参数值得话。那么所有这种情况下的该参数都会作为编译时创建的那个对象的一种别名存在。如果参数的默认值是一个不可变(Imuttable)数值，那么在函数体内如果修改了该参数，那么参数就会重新指向另一个新的不可变值。而如果参数默认值是和本文最开始的举例一样，是一个可变对象(Muttable)，那么情况就比较糟糕了。所有函数体内对于该参数的修改，实际上都是对compile阶段就已经确定的那个对象的修改。

** **\ 链式比较操作符
~~~~~~~~~~~~~~~~~~~~~

1. x, y, z = 1,2,3

2. %timeit -n 1000000 **if** x < y < z:\ **pass**

3. %timeit -n 1000000 **if** x < y **and** y < z:\ **pass**

4. 1000000 loops, best of 3: 101 ns per loop

5. 1000000 loops, best of 3: 121 ns per loop

x < y < z效率略高，而且可读性更好。

带关键字的格式化
~~~~~~~~~~~~~~~~

1. >>> **print** "Hello %(name)s !" % {'name': 'James'}

2. Hello James !

3. >>> **print** "I am years %(age)i years old" % {'age': 18}

4. I am years 18 years old

更新些的格式化:

1. >>> **print** "Hello {name} !".format(name="James")

2. Hello James !

while 1 比 while True 更快
~~~~~~~~~~~~~~~~~~~~~~~~~~

1.  **def** while\_1():

2.  n = 100000

3.  **while** 1:

4.  n -= 1

5.  **if** n <= 0: **break**

6.  **def** while\_true():

7.  n = 100000

8.  **while** **True**:

9.  n -= 1

10. **if** n <= 0: **break**

11.
12. m, n = 1000000, 1000000

13. %timeit -n 100 while\_1()

14. %timeit -n 100 while\_true()

15. 100 loops, best of 3: 3.69 ms per loop

16. 100 loops, best of 3: 5.61 ms per loop

while 1 比 while
true快很多，原因是在python2.x中，True是一个全局变量，而非关键字。

`***漂亮地打印JSON*** <http://pyzh.readthedocs.io/en/latest/improving-your-python-productivity.html#id8>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON是一个很棒的序列格式，如今广泛应用在API和web服务中，但是很难用裸眼来看大数据量的JSON,它们很长，还在一行里。

可以用参数 indent 来更好地打印JSON数据，这在跟
REPL或是日志打交道的时候很有用:

>>> **import** **json**

>>> **print**\ (json.dumps(data)) *# No indention*

{"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz",
"lactose\_intolerant": true}, {"age": 29, "name": "Joe",
"lactose\_intolerant": false}]}

>>> **print**\ (json.dumps(data, indent=2)) *# With indention*

{

"status": "OK",

"count": 2,

"results": [

{

"age": 27,

"name": "Oz",

"lactose\_intolerant": true

},

{

"age": 29,

"name": "Joe",

"lactose\_intolerant": false

}

]

}

另外，去看看内建模块 pprint , 它可以帮助你漂亮地输出其它的东西。

-  命令行上漂亮地打印JSON:

-  echo '{"json":"obj"}' \| python -mjson.tool

而且，如果你安装了 Pygments 模块，可以高亮地打印JSON:

echo '{"json":"obj"}' \| python -mjson.tool \| pygmentize -l json

-  注意 {} 是一个空的字典，而不是空的集合

其它
~~~~

| **def main**\ (options):
| # 字符串拼接
| a\_list = ['a', 'b', 'c']
| **print** '\\t'.join(a\_list)
| **print** "%s\\t%d\\t%0.3f" % ('abc', 34, 45.67743)
| # 判断None 用 is
| m = None
| **if** m **is** None **or** m **is not** None:
| **print** m
| # 字典默认值
| v = {}
| v['a'] = v.get('a', 0) + 1
| # 字典迭代
| **for** key, value **in** v.iteritems(): # itervalues() iterkeys()
| **print** key, value
| # 字符串前后缀
| s = "prefix\_end"
| **print** s.startswith("prefix"), s.endswith("end")
| # 变量值交换
| a = 1
| b = 2
| b, a = a, b
| # 使用if isinstance(obj, int): 而不是 if type(obj) is type(1):
| **print** isinstance('3', str)
| # xrange range
| **print** type(xrange(1, 10)), type(range(1, 10))
| # 字符串换行
| a = ("erqwrfdsftrettrret"
| "dsfdafdsfdsfd")
| **print** a

`*python内置函数大全* <http://jianfeihit.iteye.com/blog/1835272>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

http://jianfeihit.iteye.com/blog/1835272

其它学习资料
~~~~~~~~~~~~

`*http://litaotao.github.io/python-materials* <http://litaotao.github.io/python-materials>`__

`*http://blog.jobbole.com/51062/* <http://blog.jobbole.com/51062/>`__

*http://python.jobbole.com/category/basic/*

`***Python
包、模块、类以及代码文件和目录的一种管理方案*** <http://python.jobbole.com/86376/>`__

`***Python第三方库安装及常见问题*** <http://python.jobbole.com/86397/>`__

`***一分钟让你的程序支持队列和并发*** <http://python.jobbole.com/86459/>`__

`***python unicode 编码整理*** <http://python.jobbole.com/86670/>`__

`***一行python代码*** <http://python.jobbole.com/86678/>`__

`***由一个例子到python的名字空间*** <http://python.jobbole.com/86655/>`__

`***Python 二分查找与 bisect
模块*** <http://python.jobbole.com/86609/>`__

`***PYTHON编码的前世今生*** <http://python.jobbole.com/86578/>`__

`***python supervisor使用*** <http://python.jobbole.com/86423/>`__

