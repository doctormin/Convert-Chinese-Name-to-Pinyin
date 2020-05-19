from pypinyin import lazy_pinyin  # 可将汉字转为不带声调的拼音  type: list
from collections import namedtuple


class NamePinyin:
    __detailed_name: namedtuple
    __lazy_name: str

    def __init__(self):
        self.__surname = ''
        self.__name = ''
        self.__matched = False
        self.__detailed_name = ''
        self.__lazy_name = ''
        self.surname_list1 = '''
        赵 钱 孙 李 周 吴 郑 王 冯 陈 褚 卫
        蒋 沈 韩 杨 朱 秦 尤 许 何 吕 施 张
        孔 曹 严 华 金 魏 陶 姜 戚 谢 邹 喻
        柏 水 窦 章 云 苏 潘 葛 奚 范 彭 郎
        鲁 韦 昌 马 苗 凤 花 方 俞 任 袁 柳
        酆 鲍 史 唐 费 廉 岑 薛 雷 贺 倪 汤
        滕 殷 罗 毕 郝 邬 安 常 乐 于 时 傅
        皮 卞 齐 康 伍 余 元 卜 顾 孟 平 黄
        和 穆 萧 尹 姚 邵 湛 汪 祁 毛 禹 狄
        米 贝 明 臧 计 伏 成 戴 谈 宋 茅 庞
        熊 纪 舒 屈 项 祝 董 梁 杜 阮 蓝 闵
        席 季 麻 强 贾 路 娄 危 江 童 颜 郭
        梅 盛 林 刁 锺 徐 邱 骆 高 夏 蔡 田
        樊 胡 凌 霍 虞 万 支 柯 昝 管 卢 莫
        经 房 裘 缪 干 解 应 宗 丁 宣 贲 邓
        郁 单 杭 洪 包 诸 左 石 崔 吉 钮 龚
        程 嵇 邢 滑 裴 陆 荣 翁 荀 羊 於 惠
        甄 麴 家 封 芮 羿 储 靳 汲 邴 糜 松
        井 段 富 巫 乌 焦 巴 弓 牧 隗 山 谷
        车 侯 宓 蓬 全 郗 班 仰 秋 仲 伊 宫
        宁 仇 栾 暴 甘 钭 历 戎 祖 武 符 刘
        景 詹 束 龙 叶 幸 司 韶 郜 黎 蓟 溥
        印 宿 白 怀 蒲 邰 从 鄂 索 咸 籍 赖
        卓 蔺 屠 蒙 池 乔 阳 郁 胥 能 苍 双
        闻 莘 党 翟 谭 贡 劳 逄 姬 申 扶 堵
        冉 宰 郦 雍 却 璩 桑 桂 濮 牛 寿 通
        边 扈 燕 冀 僪 浦 尚 农 温 别 庄 晏
        柴 瞿 阎 充 慕 连 茹 习 宦 艾 鱼 容
        向 古 易 慎 戈 廖 庾 终 暨 居 衡 步
        都 耿 满 弘 匡 国 文 寇 广 禄 阙 东
        欧 殳 沃 利 蔚 越 夔 隆 师 巩 厍 聂
        晁 勾 敖 融 冷 訾 辛 阚 那 简 饶 空 
        曾 毋 沙 乜 养 鞠 须 丰 巢 关 蒯 相 
        查 后 荆 红 游 竺 权 逮 盍 益 桓 公 
        召 有 舜 丛 岳 寸 贰 皇 侨 彤 竭 端 
        赫 实 甫 集 象 翠 狂 辟 典 良 函 芒 
        苦 其 京 中 夕 之 冠 宾 香 果 蹇 称 
        诺 来 多 繁 戊 朴 回 毓 鉏 税 荤 靖 
        绪 愈 硕 牢 买 但 巧 枚 撒 泰 秘 亥
        绍 以 壬 森 斋 释 奕 姒 朋 求 羽 用 
        占 真 穰 翦 闾 漆 贵 代 贯 旁 崇 栋 
        告 休 褒 谏 锐 皋 闳 在 歧 禾 示 是 
        委 钊 频 嬴 呼 大 威 昂 律 冒 保 系 
        抄 定 化 莱 校 么 抗 祢 綦 悟 宏 功 
        庚 务 敏 捷 拱 兆 丑 丙 畅 苟 随 类
        卯 俟 友 答 乙 允 甲 留 尾 佼 玄 乘 
        裔 延 植 环 矫 赛 昔 侍 度 旷 遇 偶
        前 由 咎 塞 敛 受 泷 袭 衅 叔 圣 御 
        夫 仆 镇 藩 邸 府 掌 首 员 焉 戏 可 
        智 尔 凭 悉 进 笃 厚 仁 业 肇 资 合 
        仍 九 衷 哀 刑 俎 仵 圭 夷 徭 蛮 汗
        孛 乾 帖 罕 洛 淦 洋 邶 郸 郯 邗 邛
        剑 虢 隋 蒿 茆 菅 苌 树 桐 锁 钟 机
        盘 铎 斛 玉 线 针 箕 庹 绳 磨 蒉 瓮
        弭 刀 疏 牵 浑 恽 势 世 仝 同 蚁 止 
        戢 睢 冼 种 涂 肖 己 泣 潜 卷 脱 谬
        蹉 赧 浮 顿 说 次 错 念 夙 斯 完 丹
        表 聊 源 姓 吾 寻 展 出 不 户 闭 才 
        无 书 学 愚 本 性 雪 霜 烟 寒 少 字 
        桥 板 斐 独 千 诗 嘉 扬 善 揭 祈 析 
        赤 紫 青 柔 刚 奇 拜 佛 陀 弥 阿 素 
        长 僧 隐 仙 隽 宇 祭 酒 淡 塔 琦 闪 
        始 星 南 天 接 波 碧 速 禚 腾 潮 镜 
        似 澄 潭 謇 纵 渠 奈 风 春 濯 沐 茂 
        英 兰 檀 藤 枝 检 生 折 登 驹 骑 貊 
        虎 肥 鹿 雀 野 禽 飞 节 宜 鲜 粟 栗 
        豆 帛 官 布 衣 藏 宝 钞 银 门 盈 庆
        喜 及 普 建 营 巨 望 希 道 载 声 漫 
        犁 力 贸 勤 革 改 兴 亓 睦 修 信 闽 
        北 守 坚 勇 汉 练 尉 士 旅 五 令 将 
        旗 军 行 奉 敬 恭 仪 母 堂 丘 义 礼 
        慈 孝 理 伦 卿 问 永 辉 位 让 尧 依 
        犹 介 承 市 所 苑 杞 剧 第 零 谌 招
        续 达 忻 六 鄞 战 迟 候 宛 励 粘 萨 
        邝 覃 辜 初 楼 城 区 局 台 原 考 妫 
        纳 泉 老 清 德 卑 过 麦 曲 竹 百 福 
        言 佟 爱 年 笪 谯 哈 墨 连 赏 伯 佴 
        佘 牟 商 琴 后 况 亢 缑 帅 海 归 钦 
        鄢 汝 法 闫 楚 晋 督 仉 盖 逯 库 郏
        逢 阴 薄 厉 稽 开 光 操 瑞 眭 泥 运 
        摩 伟 铁 迮 禅 鬼 死 宗 单
        '''.split()  # 一个字的姓
        self.surname_list2 = '''
        万俟 司马 上官 欧阳 夏侯 诸葛 闻人 东方 赫连 皇甫 尉迟 公羊
        澹台 公冶 宗政 濮阳 淳于 单于 太叔 申屠 公孙 仲孙 轩辕 令狐
        钟离 宇文 长孙 慕容 司徒 司空 章佳 那拉 纳喇 乌雅 范姜 碧鲁 
        张廖 张简 图门 太史 公叔 乌孙 完颜 马佳 佟佳 富察 费莫 第五 
        南宫 西门 东门 左丘 梁丘 微生 羊舌 呼延 南门 东郭 百里 谷梁 
        宰父 夹谷 拓跋 壤驷 乐正 漆雕 公西 巫马 端木 颛孙 子车 司寇 
        亓官 三小 鲜于 锺离 闾丘 公良 段干
        '''.split()  # 两个字的姓
        self.surname_list3 = '''
        萨克达 钮祜禄 他塔喇 喜塔腊 库雅喇 瓜尔佳 舒穆禄 萨嘛喇 赫舍里 
        索绰络
        '''.split()  # 三个字的姓
        self.surname_list4 = '''
        依尔觉罗  额尔德特 讷殷富察 叶赫那兰  爱新觉罗  叶赫那拉
        '''.split()  # 四个字的姓
        self.surname_list5 = '''
        依尔根觉罗
        '''.split()  # 五个字的姓
        self.clash_1_2 = '''
        
        '''

    def detailed_convert(self, cname : str) -> tuple:
        # cname : chinese name
        # returned tuple : (surname, name)
        for each in self.surname_list1:
            if cname[0] == each:
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
                self.__surname = "".join(lazy_pinyin(cname[0]))
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
                self.__name = "".join(lazy_pinyin(cname[1:]))
                self.__matched = True
                break
        if not self.__matched:
            for each in self.surname_list2:
                if cname[0:2] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:2]))
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
                    self.__name = "".join(lazy_pinyin(cname[2:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list3:
                if cname[0:3] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:3]))
                    self.__name = "".join(lazy_pinyin(cname[3:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list4:
                if cname[0:4] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:4]))
                    self.__name = "".join(lazy_pinyin(cname[4:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list5:
                if cname[0:5] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:5]))
                    self.__name = "".join(lazy_pinyin(cname[5:]))
                    self.__matched = True
                    break
        Pinyin = namedtuple('Pinyin', ['surname', 'name'])
        self.__detailed_name = Pinyin(surname=self.__surname, name=self.__name)
        return self.__detailed_name

    def lazy_convert(self, cname : str) -> str:
        # cname : chinese name (e.g. 张三)
        # returned str : chinese name in pinyin (e.g. Zhang San)
        for each in self.surname_list1:
            if cname[0] == each:
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
                self.__surname = "".join(lazy_pinyin(cname[0]))
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
                self.__name = "".join(lazy_pinyin(cname[1:]))
                self.__matched = True
                break
        if not self.__matched:
            for each in self.surname_list2:
                if cname[0:2] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:2]))
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
                    self.__name = "".join(lazy_pinyin(cname[2:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list3:
                if cname[0:3] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:3]))
                    self.__name = "".join(lazy_pinyin(cname[3:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list4:
                if cname[0:4] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:4]))
                    self.__name = "".join(lazy_pinyin(cname[4:]))
                    self.__matched = True
                    break
        if not self.__matched:
            for each in self.surname_list5:
                if cname[0:5] == each:
                    self.__surname = "".join(lazy_pinyin(cname[0:5]))
                    self.__name = "".join(lazy_pinyin(cname[5:]))
                    self.__matched = True
                    break
        self.__lazy_name = self.__surname + " " + self.__name
        return self.__lazy_name


# for testing
p = NamePinyin()
while True:
    i = input("please type in a name")
    print(p.detailed_convert(i))
    print(p.lazy_convert(i))
