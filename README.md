# RdpRemoteManagement  
通过Discord机器人来远程管理你的Windows服务器。
`/startcmd` 进入远程cmd模式
`/stopcmd` 退出远程cmd模式
~~`/getfile <路径>` 远程获取指定路径文件~~
### TODO  
* [x]可以远程执行简单的cmd命令
* [x]可保存上文的cmd命令执行结果
* [ ]权限检查
* [ ]在有用户使用rdp登录服务器时发送提醒
* [ ]显示登录rdp服务器的计算机名
* [ ]可使用`/getfile <路径>`让机器人将指定目录文件发送至Discord
### 已知问题
* [ ]ANSI编码在某些电脑上可能无法工作
* [ ]可能会将机器人本体发送的消息传给cmd
* [ ]在进入cmd模式后，在其他频道发送消息也会被机器人回应
