# Demo Monorepo

演示 Python Monorepo 自动发布到 PyPI。

## 仓库结构

```
demo/
├── .github/workflows/
│   └── publish-to-pypi.yml   # GitHub Actions 自动发布
├── packages/
│   ├── pkg_core/             # → PyPI: pkg-core-zhuzhe-test
│   └── pkg_utils/            # → PyPI: pkg-utils-zhuzhe-test
└── pyproject.toml            # 根配置（仅开发用，不发布）
```

## 发布方式

### Tag 触发（推荐）

```bash
# 发布 pkg-core-zhuzhe-test
git tag pkg-core-v0.1.0 && git push --tags

# 发布 pkg-utils-zhuzhe-test
git tag pkg-utils-v0.1.0 && git push --tags
```

### 手动触发

Actions → Publish to PyPI → Run workflow → 选择包目录

## PyPI Trusted Publishers 配置

本项目使用 **OIDC Trusted Publishers**，无需 API Token。

### GitHub 侧

Settings → Environments → 创建 `pypi` 和 `testpypi` 两个 environment。

### PyPI 侧（每个包分别配置）

Account settings → Publishing → Add a new publisher：

| 字段 | pkg_core | pkg_utils |
|---|---|---|
| PyPI Project Name | `pkg-core-zhuzhe-test` | `pkg-utils-zhuzhe-test` |
| Owner | `<你的 GitHub 用户名>` | `<你的 GitHub 用户名>` |
| Repository name | `demo` | `demo` |
| Workflow name | `publish-to-pypi.yml` | `publish-to-pypi.yml` |
| Environment name | `pypi` | `pypi` |

在 TestPyPI (test.pypi.org) 上同样配置，Environment name 填 `testpypi`。

## 本地构建

```bash
cd packages/pkg_core
python -m build
```