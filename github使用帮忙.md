如果你是一枚Coder，但是你不知道Github，那么我觉的你就不是一个菜鸟级别的Coder，因为你压根不是真正Coder，你只是一个Code搬运工。说明你根本不善于突破自己！为什么这么说原因很简单，很多优秀的代码以及各种框架源码都存放于github当中！

目录
github登录与注册
gitbash安装步骤详解
gitbash常用命令
获取ssh密钥
绑定ssh密钥
代码克隆
测试提交文件
首先，我先对GitHub来一个简单介绍，GitHub他就是一个远程仓库，远程仓库通俗的理解就是一个可以保存自己代码的地方，在实际开发当中一个项目往往是有多个人来共同协作开发完成的，那么就需要一个统一代码保存的地方，而GitHub就是起到一个共享和汇总代码的作用。

github登录与注册
github属于国外的平台，所以我们打开的时候有时候比较慢，这里我写了一个解决打开慢的解决方案：https://blog.csdn.net/weixin_43888891/article/details/131546020

官方登录页: https://github.com/login



注册页: https://github.com/join?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home

相对来说注册还是很简单的，只需要一个邮箱即可，邮箱写qq邮箱就行了，假如以后忘记密码了，是可以靠邮箱来找回密码的。



官网全是英文的，目前的话，暂未发现有中文版的，对于英语不好的同学建议使用谷歌浏览器，谷歌浏览器可以翻译网页变为中文使用起来十分方便。

登录进去之后，在这里我们可以创建一个自己的库。



翻译成中文之后创建库的一些解释已经写得很清楚了哦

这里无非需要注意的就是库分为两种，分为了公有的私有的，上面解释的很清楚了，大家自行选择即可。



在创建完成自己的库之后，下面就要让自己的电脑克隆一个自己所创建的库，方面自己电脑上的代码同步到GitHub你所创建的库当中。为了实现，就需要安装一个软件，Git Bash。

gitbash安装步骤详解
git bash是Windows下的命令行工具。
基于msys GNU环境，有git分布式版本控制工具。
主要用于git版本控制，上传下载项目代码。

GitHub官网: http://git-scm.com/download/win
首先进入GitHub官网，下载适合自己电脑的版本

下载的时候有的时候特别慢，这里我给大家一个我下载好的，虽然不是最新版本但是绝对是可以用的。

链接: https://pan.baidu.com/s/1sN5a26sMOEVSGhD9G33Pwg
提取码：aunu

   

往下我就不给大家截图了，总之就是一路Next就可以了！

下载好之后随便找个文件夹右键会发现有个git bash这就证明安装好了



gitbash常用命令
git init 初始化 git，只有初始化了以后才可以使用 git 相关命令。
git clone 获取远程项目，并下载到本地。远程库的地址在 GITHUB 项目中会有提供。
git status 查看本地修改与服务器的差异。
git add . 将这些差异文件添加，这样就可以提交了。
git commit –m “这里是注释” 提交更改到服务器。
git checkout master 更改到master库。
git pull 将服务器最新的更改获取到本地。
git merge local master 将本地的local合并到远程的master上。
git push origin master 正式提交到远程的master服务器上。
还有“git tag”，“git diff”，“git show”，“git log”，“git remote”等。

获取ssh密钥
打开输入：ssh-keygen -t rsa -C “git账号”
输入之后一路Enter（确认）就可以了



以上截图就证明成功了，这个时候打开以下地址：
id_rsa.pub就是我们需要的ssh密钥了



注意：有的可能以前生成过，就会报这个错了。



报错解决: https://blog.csdn.net/weixin_43888891/article/details/112429980

绑定ssh密钥
现在你就需要登录到你的GitHub上边添加这个密匙



将整个id_rsa.pub内容复制



添加成功



之后你就可以回到你的Git bash上边了
输入：ssh -T git@github.com
然后输入上边的代码，来检查是否成功绑定。如果输入之后选择yes出来是这样说明就成功了。



接下来还需要简单的设置一些东西。
git config --global user.name “git账号”
git config --global user.email “git邮箱，注册时候的邮箱”



代码克隆
下面就要将你的库克隆下来到本地电脑中，方便以后进行上传代码。

链接: https://github.com/



下面就要将你的库克隆下来到本地电脑中，方便以后进行上传代码。

在库创建完成之后 会有一个网址出现在网页中，这个地址就是代码地址。
git clone 命令会用的到



接下来就开始选择文件存储地方了。



git clone后边的网址就是你创建库成功之后的网址

git clone 地址（这个地址就是刚刚创建的库那个页面上代码地址）

在执行命令过程有时候会让你输入账号密码啥的，这个不要输错了就行！



可以看到，指定目录已经存在了我们的库文件



测试提交文件
打开这个文件夹，然后在其中创建一个任意格式，任意名称的文件。



然后在这个文件里面右键git bash进黑框框
git add我们新增的文件



之后输入然后git commit -m “cc” 引号内的内容可以随意改动，这个语句的意思是 给你刚刚上传的文件一个备注，方便查找记忆而已



然后在输入git push origin master
这个就代表成功了



现在打开你的GitHub网站，找到你创建的库。
文件上传成功。



点个赞吧！

希望更多的人看得到！
————————————————

                            版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/Innocence_0/article/details/133698054