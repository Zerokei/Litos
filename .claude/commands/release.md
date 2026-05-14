---
description: 发布新版本：同步 manifest 版本、打 tag、push、创建 GitHub release 并附 theme.css/manifest.json
argument-hint: <version> [release notes...]
---

# 发布 Obsidian 主题新版本

参数：`$ARGUMENTS`

第一个 token 是版本号（不带 `v` 前缀，遵循 manifest.json 风格，例如 `1.0.2`），其余是可选的 release notes 文本。

## 前置检查（任一失败立即中止）

1. 当前分支必须是 `main`
2. 工作树必须干净（`git status --porcelain` 无输出）
3. 本地 `main` 与 `origin/main` 同步（先 `git fetch`，再比对 HEAD）
4. 目标 tag 不存在（`git tag -l <version>` 为空，且 `gh release view <version>` 返回 not found）

## 执行步骤

### 1. 同步 manifest.json 版本

读取 `manifest.json` 的 `version` 字段：

- 若已是目标版本，跳过
- 若不一致，用 Edit 工具更新 `version`（**不要动** `minAppVersion`），然后：
  ```
  git add manifest.json
  git commit -m "Bump version to <version>"
  git push origin main
  ```

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
