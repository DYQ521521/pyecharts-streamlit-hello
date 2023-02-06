# 存储基本的数据、列表等必要信息


coures8List = ['语文', '数学', '英语', '物理', '化学', '历史', '政治', '总分']  # 所有 学科名
ranking8List = list(i + '排名' for i in coures8List)  # 学科排名 列表

coures6List = ['3000m跑', '单杠屈臂悬垂', '俯卧撑', '仰卧起坐', '400m跑', '总分']  # 所有 学科名
ranking6List = list(i + '排名' for i in coures6List)  # 学科排名 列表

vipCount = 150  # 分析多少名之前的学生数据？

excelFilePath = './excelData/二模成绩.xlsx'  # 使用的excel源文件

classesNumber = 4  # 按多少名1个梯度来观察数据
classList = list(str(i) + '班' for i in range(1, classesNumber + 1))  # 学科排名 列表
