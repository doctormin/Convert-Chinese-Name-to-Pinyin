*Created in December 2019 by MinoZhao*


API :
1. `detailed_convert(chinese_name : str)`<br/>
    chinese_name : chinese name<br/>
    one `namedtuple` is returned<br/>
    e.g. ���� -> Pinyin(surname='San', name='Zhang')
2. `lazy_convert(chinese_name : str) -> str`<br/>
    chinese_name : chinese name<br/>
    returned str : pinyin of the given chinese name<br/>
    e.g. ���� -> "zhang san"

+ Can automatically identify the compound name
+ Names with special pronunciations also ensure correct pinyin output e.g. ��(shan)������(chanyu)


---


API :
1. `detailed_convert(chinese_name : str)`<br/>
    chinese_name : ������<br/>  
    ����ֵ�� һ��namedtuple<br/>
    e.g. ���� -> Pinyin(surname='San', name='Zhang')
2.  `lazy_convert(chinese_name : str) -> str`<br/>
    chinese_name : ������<br/>
    ����ֵ: ƴ�����ַ�����<br/>
    e.g. ���� -> "zhang san"

+ �����Զ�ʶ���ղ����ո��յĸ�ʽ���
+ ���ַ�����������ܱ�֤�����ȷ e.g. ��(shan)������(chanyu)
