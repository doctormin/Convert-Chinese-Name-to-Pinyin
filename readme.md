Created in December 2019 by MinoZhao


API:
1. detailed_convert("汉字名")
    将会print一个namedtuple显示姓和名的拼音 e.g. Pinyin(surname='zhao', name='mino')
2. lazy_convert("汉字名")
    输出字符串 e.g. zhao mino

+ 类的实现依据为`pypinyin`
+ 经过优化，可以自动识别复姓并按照复姓的格式输出
+ 经过优化，部分发音特殊的姓能保证输出正确 e.g. 单(shan)、单于(chanyu)

特殊发音
```python
                if cname[0] == '单':
                    self.__surname = 'shan'
                if cname[0] == '乐':
                    self.__surname = 'yue'
                if cname[0] == '区':
                    self.__surname = 'ou'
                if cname[0] == '芮':
                    self.__surname = 'rui'
                if cname[0] == '恽':
                    self.__surname = 'yun'
                if cname[0] == '朴':
                    self.__surname = 'piao'
                if cname[0] == '黑':
                    self.__surname = 'he'
                if cname[0] == '秘':
                    self.__surname = 'bi'
                if cname[0] == '艮':
                    self.__surname = 'gen'
                if cname[0] == '能':
                    self.__surname = 'nai'
                if cname[0] == '繁':
                    self.__surname = 'po'
                if cname[0] == '句':
                    self.__surname = 'gou'
                if cname[0] == '缪':
                    self.__surname = 'miao'
                if cname[0] == '盖':
                    self.__surname = 'ge'
                if cname[0] == '查':
                    self.__surname = 'zha'
                if cname[0] == '仇':
                    self.__surname = 'qiu'
                if cname[0] == '翟':
                    self.__surname = 'zhai'
                if cname[0] == '瞿':
                    self.__surname = 'qu'
                if cname[0] == '员':
                    self.__surname = 'yun'
                if cname[0] == '刀':
                    self.__surname = 'diao'
                if cname[0] == '种':
                    self.__surname = 'chong'
                if cname[0] == '便':
                    self.__surname = 'pian'
                if cname[0] == '折':
                    self.__surname = 'she'
                if cname[0] == '不':
                    self.__surname = 'fou'
                if cname[0] == '祭':
                    self.__surname = 'zhai'

                if cname[0:2] == '单于':
                     self.__surname = 'chanyu'
                if cname[0:2] == '乐正':
                     self.__surname = 'yuezheng'
                if cname[0:2] == '澹台':
                     self.__surname = 'tantai'
                if cname[0:2] == '长孙':
                     self.__surname = 'changsun'
                if cname[0:2] == '尉迟':
                     self.__surname = 'yuchi'
                if cname[0:2] == '万俟':
                     self.__surname = 'moqi'
```
与单姓存在冲突的复姓：
```python
                if cname[0] == '司':
                    if cname[1] == '马':
                        break
                    if cname[1] == '徒':
                        break
                    if cname[1] == '空':
                        break
                    if cname[1] == '寇':
                        break
                if cname[0] == '张':
                    if cname[1] == '廖':
                        break
                '''
                    太少见且容易跟单字姓搞错 故默认不识别
                    if cname[1] == '简':
                        break
                '''
                if cname[0] == '南':
                    if cname[1] == '宫':
                        break
                    if cname[1] == '门':
                        break
                if cname[0] == '东':
                    if cname[1] == '方':
                        break
                    if cname[1] == '郭':
                        break
                    if cname[1] == '门':
                        break
                if cname[0] == '公':
                    if cname[1] == '孙':
                        break
                    if cname[1] == '羊':
                        break
                    if cname[1] == '冶':
                        break
                    if cname[1] == '良':
                        break
                    if cname[1] == '西':
                        break
                if cname[0] == '赫':
                    if cname[1] == '连':
                        break
                    if cname[1:3] == '舍里':
                        break
                if cname[0] == '萨':
                    if cname[1:3] == '克达':
                        break
                    if cname[1:3] == '嘛喇':
                        break
                if cname[0] == '欧' and cname[1] == '阳':
                    break
                if cname[0] == '万' and cname[1] == '俟':
                    break
                if cname[0] == '夏' and cname[1] == '侯':
                    break
                if cname[0] == '诸' and cname[1] == '葛':
                    break
                if cname[0] == '闻' and cname[1] == '人':
                    break
                if cname[0] == '尉' and cname[1] == '迟':
                    break
                if cname[0] == '宗' and cname[1] == '政':
                    break
                if cname[0] == '单' and cname[1] == '于':
                    break
                if cname[0] == '申' and cname[1] == '屠':
                    break
                if cname[0] == '令' and cname[1] == '狐':
                    break
                if cname[0] == '钟' and cname[1] == '离':
                    break
                if cname[0] == '那' and cname[1] == '拉':
                    break
                if cname[0] == '纳' and cname[1] == '喇':
                    break
                if cname[0] == '左' and cname[1] == '丘':
                    break
                if cname[0] == '梁' and cname[1] == '丘':
                    break
                if cname[0] == '羊' and cname[1] == '舌':
                    break
                if cname[0] == '呼' and cname[1] == '延':
                    break
                if cname[0] == '夏' and cname[1] == '侯':
                    break
                if cname[0] == '百' and cname[1] == '里':
                    break
                if cname[0] == '谷' and cname[1] == '梁':
                    break
                if cname[0] == '宰' and cname[1] == '父':
                    break
                if cname[0] == '乐' and cname[1] == '正':
                    break
                if cname[0] == '漆' and cname[1] == '雕':
                    break
                if cname[0] == '巫' and cname[1] == '马':
                    break
                if cname[0] == '端' and cname[1] == '木':
                    break
                if cname[0] == '亓' and cname[1] == '官':
                    break
                if cname[0] == '鲜' and cname[1] == '于':
                    break
                if cname[0] == '锺' and cname[1] == '离':
                    break
                if cname[0] == '闾' and cname[1] == '丘':
                    break
                if cname[0] == '段' and cname[1] == '干':
                    break
                if cname[0] == '爱' and cname[1:4] == '新觉罗':
                    break
                if cname[0] == '叶' and cname[1:4] == '赫那拉':
                    break
                if cname[0] == '喜' and cname[1:3] == '塔腊':
                    break
                if cname[0] == '钮' and cname[1:3] == '祜禄':
                    break
                if cname[0] == '库' and cname[1:3] == '雅喇':
                    break
                if cname[0] == '舒' and cname[1:3] == '穆禄':
                    break
                if cname[0] == '索' and cname[1:3] == '绰络':
                    break

                '''
                太少见且容易跟单字姓搞错 故默认不识别
                if cname[0] == '费' and cname[1] == '莫': break
                if cname[0] == '佟' and cname[1] == '佳': break
                if cname[0] == '马' and cname[1] == '佳': break
                if cname[0] == '范' and cname[1] == '姜': break
                if cname[0] == '章' and cname[1] == '佳': break
                '''
```# Convert-Chinese-Name-to-Pinyin
