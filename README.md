** 主要内容是读取配置，启动数据记录类
** child and parent process 可以从1.0版本里面参考
** 应该还是需要app的概念，不过是没有ui的app
** engine是最底层的结构


配置放置在./vntrader/下就可以了（数据库和datarecorder的setting）
ctp的配置应该也可以以此类推----现在还是直接写在程序里面。
需要创建新的数据库用于存放生产的数据。
并不需要去写关于包装引擎的类，其他的app应该也可以按照同样的思路进行
pycharm对于调试还是有莫大的作用的。
