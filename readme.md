Created in December 2019 by MinoZhao


API:
1. detailed_convert("������")
    ����printһ��namedtuple��ʾ�պ�����ƴ�� e.g. Pinyin(surname='zhao', name='mino')
2. lazy_convert("������")
    ����ַ��� e.g. zhao mino

+ ���ʵ������Ϊ`pypinyin`
+ �����Ż��������Զ�ʶ���ղ����ո��յĸ�ʽ���
+ �����Ż������ַ�����������ܱ�֤�����ȷ e.g. ��(shan)������(chanyu)

���ⷢ��
```python
                if cname[0] == '��':
                    self.__surname = 'shan'
                if cname[0] == '��':
                    self.__surname = 'yue'
                if cname[0] == '��':
                    self.__surname = 'ou'
                if cname[0] == '��':
                    self.__surname = 'rui'
                if cname[0] == '�':
                    self.__surname = 'yun'
                if cname[0] == '��':
                    self.__surname = 'piao'
                if cname[0] == '��':
                    self.__surname = 'he'
                if cname[0] == '��':
                    self.__surname = 'bi'
                if cname[0] == '��':
                    self.__surname = 'gen'
                if cname[0] == '��':
                    self.__surname = 'nai'
                if cname[0] == '��':
                    self.__surname = 'po'
                if cname[0] == '��':
                    self.__surname = 'gou'
                if cname[0] == '��':
                    self.__surname = 'miao'
                if cname[0] == '��':
                    self.__surname = 'ge'
                if cname[0] == '��':
                    self.__surname = 'zha'
                if cname[0] == '��':
                    self.__surname = 'qiu'
                if cname[0] == '��':
                    self.__surname = 'zhai'
                if cname[0] == '��':
                    self.__surname = 'qu'
                if cname[0] == 'Ա':
                    self.__surname = 'yun'
                if cname[0] == '��':
                    self.__surname = 'diao'
                if cname[0] == '��':
                    self.__surname = 'chong'
                if cname[0] == '��':
                    self.__surname = 'pian'
                if cname[0] == '��':
                    self.__surname = 'she'
                if cname[0] == '��':
                    self.__surname = 'fou'
                if cname[0] == '��':
                    self.__surname = 'zhai'

                if cname[0:2] == '����':
                     self.__surname = 'chanyu'
                if cname[0:2] == '����':
                     self.__surname = 'yuezheng'
                if cname[0:2] == '�̨':
                     self.__surname = 'tantai'
                if cname[0:2] == '����':
                     self.__surname = 'changsun'
                if cname[0:2] == 'ξ��':
                     self.__surname = 'yuchi'
                if cname[0:2] == '��ٹ':
                     self.__surname = 'moqi'
```
�뵥�մ��ڳ�ͻ�ĸ��գ�
```python
                if cname[0] == '˾':
                    if cname[1] == '��':
                        break
                    if cname[1] == 'ͽ':
                        break
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                if cname[0] == '��':
                    if cname[1] == '��':
                        break
                '''
                    ̫�ټ������׸������ո�� ��Ĭ�ϲ�ʶ��
                    if cname[1] == '��':
                        break
                '''
                if cname[0] == '��':
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                if cname[0] == '��':
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                if cname[0] == '��':
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                    if cname[1] == 'ұ':
                        break
                    if cname[1] == '��':
                        break
                    if cname[1] == '��':
                        break
                if cname[0] == '��':
                    if cname[1] == '��':
                        break
                    if cname[1:3] == '����':
                        break
                if cname[0] == '��':
                    if cname[1:3] == '�˴�':
                        break
                    if cname[1:3] == '����':
                        break
                if cname[0] == 'ŷ' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == 'ٹ':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == 'ξ' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == 'ľ':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1] == '��':
                    break
                if cname[0] == '��' and cname[1:4] == '�¾���':
                    break
                if cname[0] == 'Ҷ' and cname[1:4] == '������':
                    break
                if cname[0] == 'ϲ' and cname[1:3] == '����':
                    break
                if cname[0] == 'ť' and cname[1:3] == '��»':
                    break
                if cname[0] == '��' and cname[1:3] == '����':
                    break
                if cname[0] == '��' and cname[1:3] == '��»':
                    break
                if cname[0] == '��' and cname[1:3] == '����':
                    break

                '''
                ̫�ټ������׸������ո�� ��Ĭ�ϲ�ʶ��
                if cname[0] == '��' and cname[1] == 'Ī': break
                if cname[0] == '١' and cname[1] == '��': break
                if cname[0] == '��' and cname[1] == '��': break
                if cname[0] == '��' and cname[1] == '��': break
                if cname[0] == '��' and cname[1] == '��': break
                '''
```# Convert-Chinese-Name-to-Pinyin
