# Clash 分流规则，重点分流 AI 服务、字节海外 AI 服务 、 WEB3 应用、教育类 APP、开发者常用下载节点等分流服务

> 本项目基于 ACL4SSR 项目进行修改，用于个人使用

# 重点个性化分流规则介绍

| 分流规则名称 | 说明                                                                                  |
| ------------ | ------------------------------------------------------------------------------------- |
| 🟠 Claude    | Claude 与 Anthropic 服务，可独立选择代理节点                                           |
| 🤖 Grok      | Grok 与 xAI 服务，可独立选择代理节点                                                   |
| 🧠 OpenAI   | OpenAI、ChatGPT、Sora 及相关依赖，可独立选择代理节点                                 |
| 🇺🇲 美区AI    | 需美国节点的其他 AI 服务，包括 Perplexity、Bing / Copilot、Muse 等            |
| 🔎 Google | Google、Gemini、Antigravity、Drive 等服务独立选择节点，默认美国节点；YouTube 保持独立 |
| 🐦 X / Twitter | X、Twitter、短链及图片视频资源独立选择节点；Grok / xAI 保持独立 |
| 🌈 CiciAI    | 建议使用新加坡节点，确保字节海外版的 APP 和 AI 服务可正常使用                         |
| 👨‍💻 Developer | 建议使用流量大或免费节点，各种 docker 镜像、模型文件下载专用                          |
| 🔒 Web3      | 建议使用自建的安全节点，避免出现安全风险                                              |
| 🫙 自定义    | 放自建节点，搭配上方分流规则使用                                                      |

> **为什么将 `*.proton.me` 和 `*.protonweb.com` 加入 Claude 分组？**
>
> 当前使用 Proton Mail 接收 Claude 邮件。为降低打开邮件时因追踪器导致 IP 或 DNS 出口不一致的风险，`proton.me`、`protonweb.com` 及其所有子域名与 Claude、Anthropic 服务使用同一代理分组，确保查看 Claude 邮件时的 IP 和 DNS 出口与访问 Claude 时保持一致。

其他分流规则，包括 哔哩哔哩,Khan,海外媒体,Spotify,Netflix, YouTube, DisneyPlus, 游戏平台等常用规则。

## 重要提醒

部分AI网站和APP优先使用了 `HTTP/3 (QUIC)`协议，导致即使分流和TUN 模式下都可能无法使用服务，在确保IP干净也无法使用的情况下，请添加下面的自定义规则（可能会影响部分游戏服务）并启用。

```
AND,((NETWORK,UDP),(DST-PORT,443)),REJECT
```

特别说明：为什么要加第一行 REJECT？
hysteria2，这是一个基于 UDP 的暴力传输协议。

误区：很多人以为用了 UDP 协议的节点，就必须让所有 UDP 流量都通畅。

真相：

Hysteria2 协议本身确实是用 UDP 发包给服务器的（这是底层的车）。

但是，浏览器里的 HTTP/3 (QUIC) 也是 UDP。

当我们加了 - AND,((NETWORK,UDP),(DST-PORT,443)),REJECT 这一行时，我们并没有掐断 Hysteria2 的连接。我们只是在本地告诉浏览器：“别尝试用 QUIC 直连或者乱发 UDP 包了，老老实实把数据包封装成 TCP 给我”。

一旦浏览器转为 TCP，Clash 就会把它接管过来，完美地通过 Hysteria2 协议封装发出去。

# 使用方式

在订阅的 URL 上增加 config=[替换成下面 ini,或自定义]

[https://raw.githubusercontent.com/DASungta/ClashRuleSet/main/Clash/kclash.ini](https://raw.githubusercontent.com/DASungta/ClashRuleSet/main/Clash/kclash.ini)

订阅地址后面增加：`&config=https%3A%2F%2Fraw.githubusercontent.com%2FDASungta%2FClashRuleSet%2Frefs%2Fheads%2Fmain%2FClash%2Fkclash.ini`

更新订阅后，在 `🧠 OpenAI` 分组中选择所需节点。原 OpenAI 规则段中的共享登录、验证与监控域名也随该分组路由。

分流顺序：X / Twitter 优先于 Grok 和美区AI；YouTube 优先于 Google；专用服务规则优先于通用代理规则。广告拦截与白名单仍优先匹配；X 官方嵌入组件 `syndication.twitter.com` 在应用净化前单独放行。

2026-10-14 已按 V2Fly、MetaCubeX 和 blackmatrix7 的固定快照更新全部启用分组规则，来源、过滤范围及测试结果见[更新记录](docs/rule-refresh-2026-10-14.md)。
