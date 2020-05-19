*Created in December 2019 by MinoZhao*


API :
1. `detailed_convert(chinese_name : str)`<br/>
    chinese_name : chinese name<br/>
    one `namedtuple` is returned<br/>
    e.g. 张三 -> Pinyin(surname='San', name='Zhang')
2. `lazy_convert(chinese_name : str) -> str`<br/>
    chinese_name : chinese name<br/>
    returned str : pinyin of the given chinese name<br/>
    e.g. 张三 -> "zhang san"

+ Can automatically identify the compound name
+ Names with special pronunciations also ensure correct pinyin output e.g. 单(shan)、单于(chanyu)


---


API :
1. `detailed_convert(chinese_name : str)`<br/>
    chinese_name : 中文名<br/>  
    返回值： 一个namedtuple<br/>
    e.g. 张三 -> Pinyin(surname='San', name='Zhang')
2.  `lazy_convert(chinese_name : str) -> str`<br/>
    chinese_name : 中文名<br/>
    返回值: 拼音（字符串）<br/>
    e.g. 张三 -> "zhang san"

+ 可以自动识别复姓并按照复姓的格式输出
+ 部分发音特殊的姓能保证输出正确 e.g. 单(shan)、单于(chanyu)
