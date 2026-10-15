# 2026-10-14 分组规则更新记录

> 后续修复（2026-10-15）：本文记录的 63 条 USER-AGENT 与 8 条 URL-REGEX 已从启用文件中清理，现可由 Manager/Mihomo 直接加载；Google 旧模板兼容和内联规则修复见 README。下文保留 10 月 14 日的更新与验收记录。

覆盖 `Clash/kclash.ini` 实际引用的 35 份规则文件：本轮更新 34 份，保留前一轮已核对的 X / Twitter 规则。地区节点筛选、默认节点和漏网之鱼策略保持不变。未被该配置引用的其他 `.list` 文件不属于本轮更新范围。

## 来源快照

| 来源 | 固定提交 |
| --- | --- |
| blackmatrix7/ios_rule_script | [d8363caa2c1e](https://github.com/blackmatrix7/ios_rule_script/commit/d8363caa2c1e47fb735615316032bed3f475ee57) |
| MetaCubeX/meta-rules-dat | [9c8e9f56b6ff](https://github.com/MetaCubeX/meta-rules-dat/commit/9c8e9f56b6ffadab05bfc933011b2bfc2f4f8288) |
| v2fly/domain-list-community | [c6adacf29cc4](https://github.com/v2fly/domain-list-community/commit/c6adacf29cc4fb05e04651fcf03e00989ef9f797) |

每份更新后的规则文件头部记录了对应的固定版本原文地址。标准分组结合 blackmatrix7 的 Clash 列表和 MetaCubeX 的域名数据补充；AI 等小型列表另与 V2Fly 原始数据核对。各来源条目更新日期可能早于仓库最新提交日期。

## 合并边界

- 保留本地定制：`b.ai`、Muse、Cerebras、Claude 的 Proton 邮件规则、Antigravity / Google Drive 进程规则，以及已有节点选择设置。
- Google 与 Gemini、Antigravity 统一归入 Google；YouTube 先于 Google 匹配。保留 `yt3.ggpht.com` 等视频专用入口，未将整个 `ggpht.com`、`gvt1.com` 改归 YouTube。
- X / Twitter 与 Grok 保持独立；`grok.x.com` 使用 X，`grok.com`、`x.ai`、`grokipedia.com` 使用 Grok。
- OpenAI 与 Claude 仍独立。新来源中的公共验证码、登录和监控依赖可能仍被多个服务共用；首条匹配规则决定归属。
- 美区AI 的 Bing 部分改用对应 Bing / Copilot 清单，移除旧段中无关站点和整个 Azure 云域名，保留 Perplexity、Poe 和自定义 AI 地址。BingX 归 Web3。
- 排除新增整段云服务商 ASN、服务清单里的通用云 IP；Google / Microsoft 等既有 IP 规则仍保留。Telegram、Netflix、国内 IP 使用 MetaCubeX 固定快照替换旧 IP 清单，避免叠加过时地址。
- Hulu 保持国外媒体分组；不将 Amazon S3、CloudFront、Akamai 全部地址收进教育或国外媒体。移除新增的共享服务父域名规则，保护已有 Web3、游戏和 DisneyPlus 子域名归属。
- 广告公司域名与应用广告/跟踪端点分别增补到广告拦截和应用净化。已有拦截策略保留，新增拦截不覆盖已明确归类的 AI 登录依赖；X 官方嵌入组件保留单独放行。
- 新增 Google / Disney 广告与遥测条目会优先进入应用净化，例如 `googletagmanager.com`、`disney.demdex.net`。如需这些统计功能，应调整应用净化策略。
- 本地去重、去除字段空格、规范化 CIDR。配置的全部远程规则地址指向本 fork，防止本地规则更新后仍使用原 fork 源站旧文件。

## 文件清单

数量以本轮开始时的工作区为基准，不包含注释、空行；新增来源进行了范围过滤，不是无条件合并所有上游条目。

| 文件 | 更新前 → 更新后 | 参考清单 |
| --- | --- | --- |
| [LocalAreaNetwork.list](../Clash/LocalAreaNetwork.list) | 36 → 161 | bm-Lan, meta-private, ip-private |
| [UnBan.list](../Clash/UnBan.list) | 16 → 172 | bm-Direct |
| [BanAD.list](../Clash/BanAD.list) | 589 → 633 | meta-category-ads-all |
| [BanProgramAD.list](../Clash/BanProgramAD.list) | 999 → 1712 | meta-category-ads |
| [Ruleset/Claude.list](../Clash/Ruleset/Claude.list) | 13 → 19 | bm-Claude, bm-Anthropic, meta-anthropic, v2-anthropic |
| [Ruleset/Grok.list](../Clash/Ruleset/Grok.list) | 4 → 5 | meta-xai, v2-xai |
| [Ruleset/OpenAI.list](../Clash/Ruleset/OpenAI.list) | 21 → 50 | bm-OpenAI, meta-openai, v2-openai |
| [Ruleset/YouTube.list](../Clash/Ruleset/YouTube.list) | 17 → 184 | bm-YouTube, meta-youtube, v2-youtube |
| [Ruleset/AiDomain.list](../Clash/Ruleset/AiDomain.list) | 92 → 81 | bm-Bing, bm-Copilot, meta-perplexity, meta-poe, meta-bing, meta-github-copilot, v2-perplexity, v2-poe, v2-github-copilot |
| [Ruleset/Google.list](../Clash/Ruleset/Google.list) | 219 → 1187 | bm-Google, bm-Gemini, bm-GoogleDrive, bm-GoogleEarth, bm-GoogleFCM, meta-google, meta-google-gemini, meta-google-deepmind |
| [Ruleset/CiciAi.list](../Clash/Ruleset/CiciAi.list) | 63 → 115 | bm-TikTok, meta-tiktok, meta-trae, v2-tiktok, v2-trae |
| [Ruleset/Developer.list](../Clash/Ruleset/Developer.list) | 42 → 651 | bm-Developer, meta-category-dev, meta-github, meta-gitlab, meta-docker, meta-huggingface, meta-python, meta-npmjs |
| [Microsoft.list](../Clash/Microsoft.list) | 97 → 895 | bm-Microsoft, meta-microsoft |
| [Apple.list](../Clash/Apple.list) | 29 → 1845 | bm-Apple, meta-apple |
| [Telegram.list](../Clash/Telegram.list) | 24 → 52 | bm-Telegram, meta-telegram, ip-telegram |
| [Web3.list](../Clash/Web3.list) | 290 → 433 | bm-Crypto, bm-Cryptocurrency, bm-Binance, bm-OKX, meta-category-cryptocurrency |
| [Ruleset/Spotify.list](../Clash/Ruleset/Spotify.list) | 9 → 39 | bm-Spotify, meta-spotify |
| [Ruleset/Epic.list](../Clash/Ruleset/Epic.list) | 5 → 31 | bm-Epic, meta-epicgames |
| [Ruleset/Sony.list](../Clash/Ruleset/Sony.list) | 5 → 124 | bm-Sony, meta-sony |
| [Ruleset/Steam.list](../Clash/Ruleset/Steam.list) | 18 → 84 | bm-Steam, meta-steam |
| [Ruleset/Khan.list](../Clash/Ruleset/Khan.list) | 18 → 16 | meta-khanacademy, v2-khanacademy |
| [Ruleset/Edutools.list](../Clash/Ruleset/Edutools.list) | 10 → 14 | bm-Duolingo, meta-duolingo, v2-duolingo |
| [Ruleset/UK.list](../Clash/Ruleset/UK.list) | 22 → 55 | bm-BBC, bm-UKMedia, meta-bbc |
| [Ruleset/Netflix.list](../Clash/Ruleset/Netflix.list) | 41 → 38 | bm-Netflix, meta-netflix |
| [Ruleset/NetflixIP.list](../Clash/Ruleset/NetflixIP.list) | 863 → 122 | ip-netflix |
| [Ruleset/DisneyPlus.list](../Clash/Ruleset/DisneyPlus.list) | 22 → 199 | bm-Disney, meta-disney |
| [Ruleset/Bilibili.list](../Clash/Ruleset/Bilibili.list) | 21 → 131 | bm-BiliBili, meta-bilibili |
| [Ruleset/BilibiliHMT.list](../Clash/Ruleset/BilibiliHMT.list) | 21 → 22 | bm-BiliBiliIntl |
| [ChinaMedia.list](../Clash/ChinaMedia.list) | 45 → 353 | bm-ChinaMedia |
| [ProxyMedia.list](../Clash/ProxyMedia.list) | 341 → 1470 | bm-GlobalMedia, meta-hulu |
| [ProxyGFWlist.list](../Clash/ProxyGFWlist.list) | 6469 → 35266 | bm-Global |
| [ChinaDomain.list](../Clash/ChinaDomain.list) | 586 → 3844 | bm-China |
| [ChinaCompanyIp.list](../Clash/ChinaCompanyIp.list) | 208 → 9609 | ip-cn |
| [Download.list](../Clash/Download.list) | 26 → 47 | bm-Download |

`bm-` 为 blackmatrix7，`meta-` 为 MetaCubeX geosite，`ip-` 为 MetaCubeX geoip，`v2-` 为 V2Fly。Khan 清单已覆盖来源中的有效域名，本次仅移除两个过宽的 S3 父域名。

## 验证

- 40 个分组名称、规则引用、选择器引用、循环引用、正则语法及 FINAL 顺序检查通过。
- 68 个既有域名场景、90 项 X 专项断言、78 个新增服务域名场景通过；Google 的 3 个进程场景通过。
- Subconverter v0.9.0 使用 11 个本地虚拟节点和本地规则快照完成实际转换，生成 40 个分组、59,618 条规则。没有使用真实订阅或访问真实代理节点。
- 对生成结果逐条比较规则内容与顺序，通过；生成 YAML 上的 78 个域名场景和 8 个 IPv4 / IPv6 场景通过。
- Mihomo v1.19.32 的配置检查 `-t` 通过。测试仅使用临时目录和回环地址，不修改当前运行的代理配置。
- 旧文件中的 63 条 USER-AGENT 和 8 条 URL-REGEX 不是 Clash 规则，由 Subconverter 正常过滤，未新增此类规则。V2Fly 的 ChatGPT 异步接口正则以专用 `chatgpt-async-webps-prod-` 关键词兼容。
- `git diff --check` 通过。

未验证实际账号登录、付款、视频播放和当前订阅的节点可用性。IP / ASN、共享验证码和平台风控仍可能影响实际访问；静态匹配和内核加载通过不等于所有网站功能实测通过。
