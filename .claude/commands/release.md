---
description: 发布新版本：同步 manifest 版本、打 tag、push、创建 GitHub release 并附 theme.css/manifest.json
argument-hint: <version> [release notes...]
---

# 发布 Obsidian 主题新版本

参数：`$ARGUMENTS`

第一个 token 是版本号（不带 `v` 前缀，遵循 manifest.json 风格，例如 `1.0.2`），其余是可选的 release notes 文本。

## 版本分级

版本号使用 `主版本.次版本.补丁版本`，根据自上次发布以来的最高改动级别选择目标版本：

- 三级：样式调整、排版打磨与问题修复，递增补丁版本，例如 `1.2.3 → 1.2.4`。内外链样式与窗口底色修复均属此级。
- 二级：新增特性，递增次版本并将补丁归零，例如 `1.2.3 → 1.3.0`。
- 一级：非常大的整体调整、架构重构或破坏兼容约定，递增主版本并将次版本、补丁归零，例如 `1.2.3 → 2.0.0`。

按产品影响定级，不按改动行数判断。普通内部整理、测试和文档变更不单独要求产品升版；开发提交可以积累到同一版本发布。Litos 与 Companion 独立定级和发布，主题改动不要求插件跟随升版。新增可选 CSS 变量保留 API 1；破坏既有接口时另行执行配套接口升级。

## 前置检查（任一失败立即中止）

1. 当前分支必须是 `main`
2. 工作树必须干净（`git status --porcelain` 无输出）
3. 本地 `main` 与 `origin/main` 同步（先 `git fetch`，再比对 HEAD）
4. 目标 tag 不存在（`git tag -l <version>` 为空，且 `gh release view <version>` 返回 not found）
5. 目标版本符合上述分级，并高于上一个已发布版本；清单已提前升版时仍须检查该版本包含的全部改动

## 执行步骤

### 1. 同步产品版本并检查

检查并同步以下位置为目标版本（**不要动** `minAppVersion`）：

- `manifest.json` 的 `version`
- `package.json` 的 `version`
- `package-lock.json` 的根 `version` 和 `packages[""].version`，保留依赖解析结果
- `theme.css` 的 `--litos-theme-version`

运行 `npm run lint:compat`，并核对上述声明一致。在 Litos-dev 开发库中发布时，同时更新父仓库 `tools/compatibility.json` 中的主题版本并运行根目录 `npm run check`。新增可选变量不升级 Companion API；接口变化按开发库的接口升级流程处理。

- 所有位置已是目标版本且检查通过时，跳过版本提交
- 有版本声明需要更新时，仅暂存对应文件，再执行：
  ```
  git add manifest.json package.json package-lock.json theme.css
  git commit -m "Bump version to <version>"
  git push origin main
  ```

在 Litos-dev 中，先提交主题，再暂存父仓库的新子模块指针和组合声明；运行 `npm run check:staged` 并提交父仓库，遵守子仓库先于父仓库的推送顺序。

### 2. 打 tag

```
git tag -a <version> -m "Release <version>" HEAD
git push origin <version>
```

Tag 名称**不带 `v` 前缀**——Obsidian 主题约定与 manifest 的 `version` 字段一致。

### 3. 生成 release notes

- 若用户在参数中提供了 notes 文本，直接使用
- 否则用 `git log <上一个 tag>..HEAD --oneline` 收集 commits，整理成简洁列表（imperative、聚焦 user-facing 变更，按 fix/feat/perf/docs 分类；首次 release 用 `git log --oneline` 取全部）

### 4. 创建 GitHub release

```
gh release create <version> theme.css manifest.json \
  --title "<version>" \
  --notes "$(cat <<'EOF'
<整理好的 notes>
EOF
)"
```

**资产必须包含 `theme.css` 和 `manifest.json`**——Obsidian 的主题更新机制依赖这两个文件直接挂在 release 上。

### 5. 输出 release URL

`gh release create` 的输出就是 URL，原样返回给用户。

## 失败处理

- 若 push tag 失败（如远端已存在），删除本地 tag (`git tag -d <version>`) 并报错
- 若 `gh release create` 失败但 tag 已 push，提示用户是否删除远端 tag 再重试 (`git push origin :refs/tags/<version>`)
- **不要静默重试**任何 git push 或 gh 命令

## 不要做的事

- 不要修改 `minAppVersion`
- 不要打带 `v` 前缀的 tag（破坏 Obsidian 兼容）
- 不要在工作树脏的时候发版（先让用户处理）
- 不要跳过 push manifest commit 就直接打 tag（tag 会指向远端没有的 commit）
