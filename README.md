# evil.py
python必不备库 借鉴Evil.js的python版 https://github.com/chao325/Evil.js

配置出错概率, 随机概率出错 让出错更可控  
配置出错时间, 规避目标前期检查, 你看我, 我正常, 你不看我就出错  
修改len 大于配置(20)的始终少1  
修改print 概率不打印  
交换floor ceil 上下取整颠倒  
替换random randint(argv, argv_1) 返回 randint(max(argv_1 // 2, argv),argv_1)  

# 声明
本项目仅用于作者个人项目代码，用于增加游戏随机性  
请不要转载和引用，造成的损失与本作者无关
