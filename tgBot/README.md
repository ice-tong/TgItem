
title: 小白教程，创建一个自己的tg机器人，用于保存图片和视频到电脑。
date: 2018-07-14 19:33:54
tags: telegram, python, tg机器人
原文链接: http://xycong.cn/2018/07/14/小白教程，创建一个自己的tg机器人，用于保存图片和视频到电脑。/　作者: icetong

## 基本思路

1. 创建一个机器人，获取机器人的apitoken。
2. 安装python3，切记将pip添加进环境变量。
3. pip安装第三方库，requests和pyTelegramBotAPI。
4. 下载这个文件 --> [点我](https://github.com/ice-tong/TgItem/blob/master/tgBot/tgbot_for_download_media.py)
5. 将自己机器人的apitoken填入。
6. ssr开启全局模式，运行 tgbot_for_download_media.py。

<!--more-->

## 创建机器人，获取apitoken。

telegrm创建机器人特别简单，直接在tg上搜索一个叫做BotFather的机器人，看它的名字就知道了，他是所有tg机器人的爸爸。输入命令/start开始，然后新建一个点击/newbot机器人，接着输入机器人昵称，然后输入机器人的用户名。用户名要以 bot 结尾，而且用户名是唯一的，所以如果用户名已存在，会提示你重新换一个。用户名输入成功后，他会提示你创建机器人成功，然后会把这个机器人的apitoken给你，apitoken是每个机器人的唯一身份令牌，相当于密码了，要妥善保管。可以通过 /revoke 命令删除apitoken。</br>


![搜索 BotFather](https://i.imgur.com/c18Rctp.png)
</br>

![/start 开始](https://i.imgur.com/GwQ6tNf.png)
</br>

![输入机器人昵称和用户名](https://i.imgur.com/flK17Gj.jpg)
</br>

到此，机器人算是创建成功了，你有了一个非常简陋的机器人，想要添加命令或者其他，可以自行探索。

## 安装python3（若已安装，请跳过。）

去python官网下载 [点我](https://www.python.org/downloads/) ，需要下载python3.x。
安装时候切记勾选上将python添加到环境变量，然后点击 install Now，安装完成后，在cmd从输入 python -V, pip -V，查看python和pip版本，检查是否成功安装。</br>

![ 下载python3 ](https://i.imgur.com/qqin2Mf.png)
</br>

![安装](https://i.imgur.com/tW0IZRD.jpg)
</br>

![打开cmd](https://i.imgur.com/NCAhQgf.png)
</br>

![查看是否成功安装](https://i.imgur.com/RtAUDFi.png)
</br>

## 安装requests和pyTelegramBotApi

在cmd里面输入：

`
pip install requests
`
</br>
`
pip install pyTelegramBotAPI
`
</br>


![安装requests](https://i.imgur.com/lp8vgz7.png)
</br>

![安装pytelegrambotapi](https://i.imgur.com/y6yxco0.png)
</br>

## 将你自己机器人的apitoken填入代码里面

下载这个文件 --> [点我](https://github.com/ice-tong/TgItem/blob/master/tgBot/tgbot_for_download_media) 右键点击，用idle打开如图，然后复制自己的apitoken到代码里面。然后开启SSR全局模式，按f5键运行代码。</br>


![SSR全局模式](https://i.imgur.com/26SE196.png)</br>
</br>

![idle打开](https://i.imgur.com/zFxQMFX.png).py) 
</br>

![填入apitoken](https://i.imgur.com/naw7oVl.png)
</br>

![运行结果](https://i.imgur.com/oQQkf6z.png)</br>
</br>

## 其他

- telegram Bot 只能保存最近24小时的消息，所以可以每天运行一遍程序，把接收到的图片视频下载下来。
- 大部分群组是不允许非管理员的群员拉机器人进群的，所以靠机器人自动收集别人群里面的图片和视频到电脑不太可行，只能是自己手动转发给机器人。
- 有待完善。
