# 这是一篇日记

 

## 序言

今天吃了 **早饭**，然后我学习 *Python* ，写了下面的代码：

```python
# 在函数定义的时候决定具体返回什么值，使用return关键字来返回

def get_formatted_name(first_name, last_name, middle_name = ""):
    if middle_name: # if len(middle_name) != 0:
        return f"{first_name} {middle_name} {last_name}".title()
    else:
        return f"{first_name} {last_name}".title()

coder = get_formatted_name('john', 'hooker')
print(coder)
```

* [ ] 法大师傅大师傅
* [x] 范德萨范德萨发士大夫
* [x] 范德萨发到付