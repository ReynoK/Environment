## Tmux的使用

ommand | Des |
| --- | --- |
| `tmux ls`  | 显示所有session |
| `tmux list-session` | 同上 |
| `tmux new (-s session-name)` | 新建session |
| `tmux new -s session-name -n window-name` | 新建一个session并创建一个命名窗口 |
| `tmux new-session (-s session-name)` | 同上 |
| `tmux a (-t session-name)` | 接入之前的session |
| `tmux attach (-t session-name)` | 同上 |
| `tmux detach` | 断开当前session（稍后可重新接入）|
| `tmux kill-session -t session-name` | 关闭session |
| `tmux killall` | 同时关闭会话 |
| `tmux list-keys` | 查看所有快捷键 |
| `tmux list-commands` | 列出所有的tmux命令 |



#### Session
以下命令均要加上**命令快捷键**

| Shortcut | Des |
| --- | --- |
| ? | 列出所有快捷键 |
| s  | 显示所有session，可以进行切换session用 |
| $ | 重命名session |
| d | 断开当前session |
| Ctrl + z | 挂起当前session |
| : | 进入命令模式 |
| [ | 进入复制模式，按空格开始进行选择文本(需要开启vi模式) |
| ] | 粘贴复制的文本 |
| t | 显示时间 |

#### Window
以下命令均要加上**命令快捷键**

| Shortcut | Des |
| --- | --- |
| c | 创建一个新窗口 |
| , | 重命名一个窗口 |
| $ | 重命名一个session|
| p | 切换到上一个窗口(previous) |
| num(0~9) | 切换到第几个窗口 |
| & | 关闭当前窗口，tmux会进行提问 |
| w | 显示当前session的所有窗口 |
| f | 在当前session通过名称查找 |

#### pannel
以下命令均要加上**命令快捷键**，每个window默认只有一个pannel

| Shortcut | self-define | Des |
| --- | --- | --- |
| % |\|| 水平切割当前pannel |
| " |-| 垂直分隔当前pannel |
| o || 在pannel间切换焦点 |
| x || 关闭当前pannel，如果window只有一个pannel，那同时关闭window |
| ~~prefix~~ exit || 关闭当前面板 |
| 方向键 || 在pannel间切换焦点 |


#### 命令模式
在`prefix :`会进入命令模式

| Command | Des |
| --- | --- |
| new-window -n window-name ("command") | 在当前session创建一个新window，可以指定要执行的命令 |
| kill-session | 关闭当前session |
| source-file file-name | 导入配置文件 |
| new-window | 打开新窗口 |

#### layout模式

| Shourtcut | self-define| Des |
| --- | --- | --- |
| Ctrl + left || 调整pannel大小，**往左位移1个单元格** |
| Ctrl + right || 调整pannel大小， **往右位移1个单元格** |
| Ctrl + up | | 调整pannel大小，**往上位移1个单元格** |
| Ctrl + down | |调整pannel大小，**往下位移1个单元格** |
| Alt  + left || 调整pannel大小，**往左位移5个单元格** |
| Alt + right || 调整pannel大小， **往右位移5个单元格** |
| Alt + up | | 调整pannel大小，**往上位移5个单元格** |
| Alt + down | |调整pannel大小，**往下位移5个单元格** |
| SPACE || 循环使用默认的pannel布局 | 
| { || 向前置换当前pannel |
| } || 向后置换当前pannel |
| Ctrl + o | | 顺时针置换当前pannel |
| Alt + o ||逆时针置换当前pannel

#### Tips
1. 让tmux支持鼠标选择，`option+鼠标移动`即可选择本文

#### 支持复制系统剪切板

1. `brew install reattach-to-user-namespace`
2. 在`~/.tmux.conf`加入以下配置

```
set-option -g default-command "reattach-to-user-namespace -l zsh"
bind y run "tmux save-buffer - | reattach-to-user-namespace pbcopy" \; display-message "已复制到剪切板"  #display-message "Copied tmux buffer to system cl    ipboard"  # 按y复制到系统剪切板
bind C-v run "reattach-to-user-namespace pbpaste | tmux load-buffer - && tmux paste-buffer" #按prefix Ctrl+v粘贴
```


