title: SSR搭建从零到一
date: 2018-07-13 07:58:01
tags: 科学上网 SSR 教程

原文: [http://xycong.cn/2018/07/13/ssr搭建从零到一/](http://xycong.cn/2018/07/13/ssr搭建从零到一/)　　作者: icetong

>现在网上已经能找到很多SSR小白搭建教程了，我觉得我来写也不能写的更好，但之前在群里面答应着要写一篇的，自己挖的坑自己填完吧。

# 厘清概念（可跳过）:
- 什么是vps, vpn？</br>
vps（Virtual Private Server），虚拟专用服务器，就是用虚拟技术，将一台物理主机按需求划分成多台用，所以vps是服务器。比如你的笔记本电脑，二十四小时不断电不断网不关机，那他可以作为一台服务器用，在你这台笔记本上开个虚拟机，这个虚拟机可以当作vps来用。</br>
vpn(Virtual Private Network), 虚拟专用网络，日常大多数谈到的vpn就是翻Q用的梯子，当然广义的梯子可不只是这样。原理了解不多，大概就是你的本地网络数据先通过国外的vps作为中转，然后送达到目标网站服务器这样子。

- 什么是SS，SSR?</br>
SSR是ShadowsocksR的缩写，一种代理工具，由SS(Shadowsocks)衍生而来。所以SSR是一种实现vpn的工具，也是目前较为流行的一种方式。</br>看看维基百科上的说明：
	>ShadowsocksR是breakwa11发起的Shadowsocks分支，在Shadowsocks的基础上增加了一些数据混淆方式，称修复了部分安全问题并可以提高QoS优先级。</br>
	>Shadowsocks的运行原理与其他代理工具基本相同，使用特定的中转服务器完成数据传输。</br>
	>在服务器端部署完成后，用户需要按照指定的密码、加密方式和端口，使用客户端软件与其连接。在成功连接到服务器后，客户端会在本机上构建一个本地Socks5代理（或VPN、透明代理）。浏览网络时，网络流量会被分到本地Socks5代理，客户端将其加密之后发送到服务器，服务器以同样的加密方式将流量回传给客户端，以此实现代理上网。</br>

# 搭建SSR的基本思路：
1. 服务端
---
	1. 购买一台海外vps
	2. 获取vps的ip地址，ssh端口（一般为22），root密码。
	3. 使用ssh工具远程登陆你所购买的vps
	4. 下载逗比一键脚本
	5. 执行脚本，安装SSR服务端，配置端口和密码。

2. 客户端
---
- windows客户端 
- 安卓客户端
- ios客户端
- mac客户端

# 搭建一个SSR服务的示例：
1. vps的购买
---
&emsp;&emsp;首先需要购买一台海外的vps，选择vps比较直接的一个标准就是看vps所在机房的位置，离大陆越近延迟越低，当然相应价格也就越贵，所以香港的vps很贵的。</br>
&emsp;&emsp;我们需要从vps服务商那里购买一台vps，现在有很多vps服务商，比如vultr，搬瓦工，nfp，三个我都用过的，还有更多其他的服务商我就不多说了。另外的，选择vps服务商最好考虑下他们是否提供支付宝或微信支付，这大大的方便了我们。</br>
&emsp;&emsp;我以[nfp（点我）](https://www.nfphosting.com/)为例讲一下。</br>
&emsp;&emsp;首先买别人的vps服务器，总得先注册一个账号吧。这个是nfp的[注册页面](https://portal.nfphosting.com/register.php?language=chinese)，支持繁体中文，还行。</br>
注册时候，除了邮箱地址和密码以外，其他的都可以随便填，注意邮政编码和手机号码要符合格式，然后输入验证码，勾选阅读条款，就可以点击注册了。

![注册示例](https://i.imgur.com/bMoX0mE.png)

</br>
&emsp;&emsp;注册好之后，就去购买一台vps。我现在选择一台月付三美元的vps: https://portal.nfphosting.com/cart.php?a=confproduct&i=0 ，如下图，root密码旁边的主机名字随便填一个,确认无误后，点击右侧的继续：：

![月付2.95刀](https://i.imgur.com/5JzMXcZ.png)
</br>
&emsp;&emsp;点击右侧的checkou:

![点击checkout](https://i.imgur.com/8zaQbGo.png)
选择AliPay(支付宝)，然后点击完成订单。

![点击完成订单](https://i.imgur.com/ejgmDDX.png)
点击paynow
![paynow](https://i.imgur.com/epyhW2b.png)
可以看到月付19.77人民币，拿出你的手机点开支付宝扫一扫点击付款就行了。
![pay](https://i.imgur.com/FZWvIrN.png)
</br>
</br>
### &emsp;&emsp;然后，nfp会发送一封邮件到你的邮箱里面，注意查收，邮件里面有你所购买的vps信息，包括服务器ip，root密码，接下来需要这两样东西。

2. ssh登陆vps服务器
---
### 利用ssh，远程登陆你购买的vps服务器。ssh工具有很多，Windows下常用的有putty，xshell，我这里使用putty。
putty下载，百度网盘链接：链接: [https://pan.baidu.com/s/13Yw8g0j9H0mrBvkZEBtSCg](https://pan.baidu.com/s/13Yw8g0j9H0mrBvkZEBtSCg) 密码: 8ang
![](https://i.imgur.com/J8TDm9F.png)
![](https://i.imgur.com/qAG0B60.png)
![](https://i.imgur.com/WnbSFHz.png)

### 到此为止，登陆成功，需要注意的是，登陆成功后，如果一段时间内没有操作putty的话，他会自动断开，需要重新登陆一下。

3. 下载逗比一键脚本

### 输入命令：`wget -N --no-check-certificate https://softs.loan/Bash/ssrmu.sh && chmod +x ssrmu.sh`
</br>
</br>
![](https://i.imgur.com/iz9Yqtv.png)
</br>
4. 运行脚本，安装并配置SSR

### 输入命令，运行脚本：`bash ssrmu.sh`
</br>
输入1回车，开始安装以及配置账户信息，详情可访问 https://doub.io/ss-jc60/查看。

![](https://i.imgur.com/6or1bh7.png)


最后得到如下：

![](https://i.imgur.com/QYkLHjK.png)

</br>
### 其中，SSR二维码可以直接复制到浏览器打开，然后用SSR客户端扫一扫添加配置信息。

5. SSR客户端

- windows客户端：</br>
	- [在iceeeee频道有下载(点我)](https://t.me/TumblrSpider/474)</br>
	- 百度网盘：链接: [https://pan.baidu.com/s/1kdCzxqxQxUaI46chXh2C9g](https://pan.baidu.com/s/1kdCzxqxQxUaI46chXh2C9g) 密码: 48r3
- 安卓客户端：</br>
	- 百度网盘：链接: [https://pan.baidu.com/s/1sBS3PfaIFYLQX_gg8XwTZQ](https://pan.baidu.com/s/1sBS3PfaIFYLQX_gg8XwTZQ) 密码: k7rx
- ios客户端: </br>
	- 美区appstore下载Shadowrocket，收费。
	- workflow规则下载，[点我获取规则](https://workflow.is/workflows/7cfe68e029c84da39a2c25eb90a41bd5).
- mac客户端：
	- 我没用过，详情参考这篇博文， [https://workflow.is/workflows/7cfe68e029c84da39a2c25eb90a41bd5](https://workflow.is/workflows/7cfe68e029c84da39a2c25eb90a41bd5)

6. 其他
---
- vps ip 有时容易被Q，所以建议买月付，被Q就换一台，不然换ip有时候要钱的。
- windows的客户端基于.net框架，win7以下的系统若无法运行，先安装 .net框架。
- SSR的本地端口是1080，开启PAC模式的时候，其他进程想要使用SSR代理，可以添加本地代理： `127.0.0.1:1080`， 或者直接开启全局模式。
- 手机开着vpn是玩不了游戏的。

