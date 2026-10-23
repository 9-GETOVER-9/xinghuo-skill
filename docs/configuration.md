# 可选研究偏好

不配置也能使用。需要稳定偏好时，复制 `research.config.example.json` 为 `research.config.local.json`，再让 Agent 读取你选定的文件。它已被 Git 和安装包排除，不需要账号或 token。

| 配置 | 默认与含义 |
|---|---|
| `preferred_platforms` | GitHub、X、YouTube、小红书、知乎；按任务选用，可换成自己的常用平台 |
| `research_mode` | `adaptive` 按问题选渠道；`broad` 安排常用渠道的广泛调研 |
| `output_directory` | `null` 沿用用户项目约定；自定义相对路径按当前任务项目解析，`~` 按用户目录解析 |
| `time_budget_minutes` | `null` 表示没有自定时长；有预算就填正数，不能据此承诺后台运行 |
| `language` | 默认 `zh-CN`；用户本轮明确语言优先 |

校验：`python scripts/check_preferences.py --config research.config.local.json`。这只检查格式，不执行研究，不创建输出目录。

使用哪个连接器、能否登录以及可访问数据取决于用户环境。配置不授予第三方平台权限，也不把私人资料自动变成可公开搜索的输入。
