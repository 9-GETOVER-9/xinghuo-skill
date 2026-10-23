<div align="center">

# 星火 · 跨平台经验调研 Skill

**从前人经验找到可行路线，让每个结论都有来源、有验证范围。**

`可追溯来源` · `按需跨平台` · `先实测再推荐` · `可中断续接`

[![Stars](https://img.shields.io/github/stars/9-GETOVER-9/xinghuo-skill?style=for-the-badge&color=d6a85c&label=Stars)](https://github.com/9-GETOVER-9/xinghuo-skill/stargazers)
[![Version](https://img.shields.io/badge/version-v1.0.0-607d8b?style=for-the-badge)](https://github.com/9-GETOVER-9/xinghuo-skill/releases)
[![License](https://img.shields.io/badge/license-MIT-6b8f71?style=for-the-badge)](LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/9-GETOVER-9/xinghuo-skill/check.yml?branch=main&style=for-the-badge&label=Checks)](https://github.com/9-GETOVER-9/xinghuo-skill/actions/workflows/check.yml)

[快速安装](#install) · [使用示例](#usage) · [配置](#configuration) · [维护与测试](docs/maintenance.md)

</div>

---

> 适合想借鉴前人经验、寻找已有方案、比较实现路线的人。把“搜到一个答案”推进到“知道它是否适合当前问题，以及还缺什么证据”。

## 能做什么

| 能力 | 你会得到什么 |
|:---|:---|
| 按需选渠道 | 根据问题与预算选择平台，广泛调研时记录覆盖和受限项 |
| 比较入口 | 先比较导出、API、网页等候选，再决定实现路线 |
| 证据分级 | 区分已实测、资料声称和尚未验证 |
| 私密输入处理 | 搜索前脱敏，不跟随网页内夹带的操作指令 |
| 长任务恢复 | 保留来源、反例、版本和下一步，不把旧结果冒充新实测 |

<a id="install"></a>
## 快速安装

需要支持 `SKILL.md` 的宿主。以下命令安装到 Codex 默认位置；已存在同名个人 Skill 时不要覆盖，请保留原目录。克隆安装无需 Python；运行校验脚本需要 Python 3.10+，维护环境依赖见说明。

<details open>
<summary><b>macOS / Linux</b></summary>

```bash
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$skill_root"
git clone https://github.com/9-GETOVER-9/xinghuo-skill.git "$skill_root/xinghuo"
```

</details>

<details>
<summary><b>Windows PowerShell</b></summary>

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
New-Item -ItemType Directory -Force $skillRoot | Out-Null
git clone https://github.com/9-GETOVER-9/xinghuo-skill.git (Join-Path $skillRoot 'xinghuo')
```

</details>

也可从 [Releases](https://github.com/9-GETOVER-9/xinghuo-skill/releases) 下载 ZIP，解压后将顶层 `xinghuo` 文件夹放到自己的 Skill 目录。入口应为 `xinghuo/SKILL.md`，避免套多一层。开启新对话加载。

<a id="configuration"></a>
## 按你的习惯配置

无需配置即可使用。需要自定义平台、预算和输出目录时，复制 `research.config.example.json` 为 `research.config.local.json`，按 [配置说明](docs/configuration.md) 修改。

本地配置已被 Git 和打包清单排除，别把 token 放进配置。仓库链接中的账号只是项目地址，不是运行身份。

<a id="usage"></a>
## 使用示例

```text
用 $xinghuo 帮我找批量导出的已有方案。
这轮只查 GitHub，先给有证据的候选和未验证项，不安装软件。
```

你会得到：适用的候选入口、原始来源、验证范围、访问限制和下一步。没有实测就不会宣称已经可用。

## 工作流

```text
明确目标与范围 → 选择来源 → 比较候选入口 → 最小验证 → 带证据交付 / 保存恢复点
```

## 能力边界

它依赖宿主实际可用的搜索/浏览能力，不保证每个平台都可登录或检索。`agent-reach` 是可选入口；付费内容、交易和不在授权范围内的操作不会自动执行。

## 文档与维护

- [Skill 入口](SKILL.md)：实际执行指令。
- [配置](docs/configuration.md)：适配自己的环境和偏好。
- [维护与测试](docs/maintenance.md)：本地检查、打包、升级和回滚。
- [贡献与反馈](CONTRIBUTING.md) · [安全反馈](SECURITY.md) · [变更记录](CHANGELOG.md)。
- [来源与公开范围](NOTICE.md) · [MIT License](LICENSE)。

自动检查覆盖辅助脚本和交付边界；不能用通过的测试数量推断模型任务成功率。GitHub Actions 展示当前提交的真实检查状态。
