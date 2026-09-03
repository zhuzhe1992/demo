# Verification Method 验证方法

## Specification Compliance Verification 规范合规验证

### Structure Validation 结构验证

```bash
# Verify skill directory structure
ls -la skills/huawei-cloud-cloudrobo-workspace/
ls -la skills/huawei-cloud-cloudrobo-workspace/references/
ls -la skills/huawei-cloud-cloudrobo-workspace/scripts/
ls -la skills/huawei-cloud-cloudrobo-workspace/templates/
```

### Frontmatter Validation Frontmatter验证

```bash
# Check frontmatter exists
grep '^---$' skills/huawei-cloud-cloudrobo-workspace/SKILL.md | head -2

# Check name field
grep '^name:' skills/huawei-cloud-cloudrobo-workspace/SKILL.md

# Check description field with triggers
grep 'Triggers include:' skills/huawei-cloud-cloudrobo-workspace/SKILL.md

# Check tags field
grep '^tags:' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
```

### Section Validation 章节验证

```bash
# Required sections (bilingual headers)
grep '##.*概述' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
grep '##.*前置条件' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
grep '##.*工作流' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
grep '##.*核心命令' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
grep '##.*参考文档' skills/huawei-cloud-cloudrobo-workspace/SKILL.md
```

### File Size Constraint 文件大小约束

```bash
# Total skill directory size must not exceed 40 MB
du -sh skills/huawei-cloud-cloudrobo-workspace/
```

### File Count Constraint 文件数量约束

```bash
# Total files must not exceed 30
find skills/huawei-cloud-cloudrobo-workspace/ -type f | wc -l
```

## Functional Testing 功能测试

### CLI Testing CLI测试

```bash
bash skills/huawei-cloud-cloudrobo-workspace/scripts/test-cli-commands.sh skills/huawei-cloud-cloudrobo-workspace --executor cli
```

### SDK Testing SDK测试

```bash
bash skills/huawei-cloud-cloudrobo-workspace/scripts/test-cli-commands.sh skills/huawei-cloud-cloudrobo-workspace --executor sdk
```

### API Testing API测试

```bash
bash skills/huawei-cloud-cloudrobo-workspace/scripts/test-cli-commands.sh skills/huawei-cloud-cloudrobo-workspace --executor api
```

## Test Case List 测试用例列表

See `templates/test-vars.json` for the full test case list.

## Verification Flow 验证流程

```
Each test case → Try CLI execution
  ├── ✅ Success → Record PASS
  └── ❌ Failure → Check syntax issues
       ├── ✅ Syntax issue → Fix and retry
       └── ❌ Non-syntax issue → Fallback to SDK
            ├── ✅ Success → Record PASS (SDK)
            └── ❌ Failure → Fallback to API
                 ├── ✅ Success → Record PASS (API)
                 └── ❌ Failure → Record FAIL ⛔ requires manual verification
```

## Verification Checklist 验证清单

- After creating a workspace, verify via `show --workspace-id <id>` that `asset_catalog_id` is populated
- After `use --workspace-id <id>`, verify `current` outputs the correct workspace config
- After adding members, verify via `list-members` that new members appear with correct roles
- After deleting a workspace, verify it no longer appears in `list`
- Verify `overview` returns consistent `workspace_used` count with `list` results
- Verify `workspace.json` file has `0o600` permissions after `workspace use`
- Verify default workspace appears in `list` even if not explicitly created
- Verify `last_count` in list response matches `workspace_available` in overview
