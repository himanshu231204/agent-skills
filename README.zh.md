# oss-ready

[![skills.sh](https://skills.sh/b/himanshu231204/oss-ready)](https://skills.sh/himanshu231204/oss-ready)

一个将任意仓库转变为专业、对贡献者友好的开源项目的 AI 技能。它分析你的实际代码库并生成仓库特定的产物——而非通用模板。

## 功能概览

| 能力 | 描述 |
|------|------|
| 仓库分析 | 检测语言、框架、架构、成熟度和就绪差距 |
| 文档生成 | 创建 README、CONTRIBUTING、SECURITY 及所有必要文档 |
| GitHub 社区 | Issue 模板、PR 模板、CODEOWNERS、标签策略 |
| 贡献机会 | 从代码分析中识别真实、有意义的 issue |
| 架构映射 | 记录结构、依赖和模块关系 |
| CI/CD 工作流 | 生成构建、测试、lint 和发布流水线 |
| 开发者体验 | 设置指南、编码规范、提交约定 |
| 发布管理 | 版本策略、变更日志、发布检查清单 |
| 就绪报告 | 六个维度的评分评估 |

## 快速开始

```
在此仓库上运行 oss-ready，使其准备好接受贡献。
```

### 命令

| 命令 | 功能 |
|------|------|
| `oss-ready audit` | 分析仓库，生成就绪报告（不修改文件） |
| `oss-ready generate` | 仅创建缺失的文件 |
| `oss-ready improve` | 就地增强现有文档 |
| `oss-ready issues` | 从代码分析中识别真实的贡献机会 |
| `oss-ready full` | 审计、生成、issue、报告——完整流水线 |

## 工作原理

1. **分析** — 检测项目类型、语言、框架、工具链和当前开源就绪状态
2. **评分** — 使用加权评分对六个维度进行评级
3. **生成** — 使用模板和仓库特定内容创建缺失的产物
4. **报告** — 生成包含评分、生成产物和优先级下一步的就绪报告

## 就绪维度

| 维度 | 权重 | 检查内容 |
|------|------|----------|
| 文档 | 25% | README、CONTRIBUTING、CODE_OF_CONDUCT、SECURITY、SUPPORT、CHANGELOG、LICENSE |
| GitHub 社区 | 20% | Issue 模板、PR 模板、CODEOWNERS、标签、讨论区 |
| CI/CD | 15% | 构建、测试、lint 和发布工作流 |
| 测试 | 15% | 测试框架、测试文件、CI 集成、覆盖率 |
| 开发者体验 | 15% | 设置说明、开发指南、编码规范、提交约定 |
| 安全 | 10% | SECURITY.md、依赖扫描、密钥扫描 |

## 技术支持

### 语言

Python、JavaScript、TypeScript、Go、Rust、Java、C#、C++、PHP、Ruby、Swift、Kotlin、Dart、Elixir、Scala、Haskell、Zig、Lua、R

### 框架

React、Next.js、Vue、Angular、Svelte、Nuxt、Astro、Remix、Express、NestJS、Fastify、Koa、FastAPI、Django、Flask、Sanic、Spring Boot、Quarkus、Laravel、Rails、Sinatra、Gin、Echo、Fiber、Actix Web、Axum、Rocket、Flutter、Electron、React Native

### 项目类型

CLI 工具、库、SDK、API、Web 应用、monorepo、Chrome 扩展、VS Code 扩展、AI 代理、MCP 服务器、RAG 应用

## 安全模式

此技能默认以安全模式运行：

- 除非明确请求，否则从不覆盖现有文件
- 从不生成占位符内容
- 从不在未检测的情况下假设技术栈
- 始终在可能时改进现有文档
- 始终生成仓库特定的输出

## 代理兼容性

适用于任何遵循 Markdown 指令的 AI 编码代理：

- Claude Code / Opencode
- Cursor / Codex CLI
- Gemini CLI / Cline
- Aider / Continue

## 架构

```
oss-ready/
├── skill.md              # 入口文件和使用指南
├── AGENT.md              # 代理编排和命令路由
├── prompt.md             # 技能的系统提示词
├── reference.md          # 检测、评分、输出格式（唯一事实来源）
├── checklist.md          # 就绪评分管线表
├── validation.md         # 技能质量维护检查清单
├── agents/               # 专用代理指令
│   ├── audit.md          # 仓库分析
│   ├── docs.md           # 文档生成
│   ├── github.md         # GitHub 社区文件
│   ├── issues.md         # 贡献机会
│   ├── architecture.md   # 架构映射
│   ├── roadmap.md        # 路线图生成
│   ├── ci.md             # CI/CD 工作流
│   ├── devex.md          # 开发者体验
│   ├── release.md        # 发布管理
│   └── report.md         # 就绪报告
├── templates/            # 可复用的文档模板
│   ├── README.md
│   ├── CONTRIBUTING.md
│   ├── CODE_OF_CONDUCT.md
│   ├── SECURITY.md
│   ├── SUPPORT.md
│   ├── ROADMAP.md
│   ├── CHANGELOG.md
│   ├── DEVELOPMENT.md
│   ├── ARCHITECTURE.md
│   ├── ISSUE_TEMPLATE.md
│   └── PR_TEMPLATE.md
└── examples/             # 技术特定指南
    ├── python.md
    ├── fastapi.md
    ├── react.md
    ├── nextjs.md
    ├── go.md
    ├── rust.md
    ├── cli.md
    ├── library.md
    └── chrome-extension.md
```

## 设计原则

1. **唯一事实来源** — `reference.md` 包含所有检测表、评分方法和输出格式。所有其他文件引用它。
2. **技术无关** — 不假设包管理器、CI 平台或语言。一切通过检测确定。
3. **仓库特定** — 每个生成的产物反映实际代码库，而非通用模板。
4. **默认安全** — 从不覆盖现有文件。始终解释生成了什么以及为什么。
5. **模块化** — 每个代理有清晰的输入/输出契约。无重复逻辑。

## 相关技能

- `opensource-pipeline` — 分支、清理和打包私有项目以供公开发布
- `security-review` — 新项目安全检查清单
- `coding-standards` — 基线编码规范
- `repo-scan` — 仓库审计和资产分类

## 许可证

MIT
