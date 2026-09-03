# cloudrobo-skills

CloudRobo AI Agent Skills，为 cloudrobo-client 提供业务编排指导。

## 目录结构

```
cloudrobo-skills/
├── skills/                                      # 11 个功能包 Skill（使用官方命名格式）
│   ├── huawei-cloud-cloudrobo-asset/            # 资产管理
│   ├── huawei-cloud-cloudrobo-dataset/          # 数据集处理（v3 格式）
│   ├── huawei-cloud-cloudrobo-dispatch/         # 智能体调度
│   ├── huawei-cloud-cloudrobo-eval/             # 模型评测
│   ├── huawei-cloud-cloudrobo-infer/            # 推理服务
│   ├── huawei-cloud-cloudrobo-model-workflow/   # 编排型 Skill（asset→train→infer→dispatch）
│   ├── huawei-cloud-cloudrobo-r2c/              # 数据面 SDK（Zenoh + mTLS）
│   ├── huawei-cloud-cloudrobo-resource/         # 资源管理
│   ├── huawei-cloud-cloudrobo-robot/            # 机器人管理
│   ├── huawei-cloud-cloudrobo-train/            # 模型训练（v3 格式）
│   └── huawei-cloud-cloudrobo-workspace/        # 工作空间
├── scripts/
│   └── migrate-to-huaweicloud.sh                # 迁移到 huaweicloud-skills 官方仓的脚本
└── docs/
    └── migration-guide.md                       # 迁移到官方仓的操作指南
```

## 命名规范

Skill 目录使用华为云官方命名格式 `huawei-cloud-cloudrobo-{function}`，符合官方正则 `^huawei-cloud-[a-z0-9]+(-[a-z0-9]+)*$`。目录名与 SKILL.md frontmatter 中的 `name` 字段和 `tags` 首元素保持一致。

## 与 cloudrobo-client 的关系

本仓库从 cloudrobo-client 分离，独立维护 Skill 内容。cloudrobo-client 保留加载器代码（`skill_loader.py` + `skill_cli.py`），通过以下方式关联本仓库：

```bash
# 方式一：环境变量
export CLOUDROBO_SKILLS_DIR=/path/to/cloudrobo-skills/skills
cloudrobo skill list

# 方式二：install 命令
cloudrobo skill install --source /path/to/cloudrobo-skills/skills --target claude-code

# 安装到 JiuwenSwarm
cloudrobo skill install --source /path/to/cloudrobo-skills/skills --target jiuwenswarm
```

`jiuwenswarm` 默认写入 `~/.jiuwenswarm/agent/workspace/skills`；如果 JiuwenSwarm
设置了 `JIUWENSWARM_DATA_DIR`，则写入该数据目录下的 `agent/workspace/skills`。

## 后续迁移到 huaweicloud-skills

本仓库是中间过渡，后续将迁移到华为云官方 Skill 仓库 `huaweicloud-skills` 的 `skills/ai/cloudrobo/` 子目录。由于 skill 已使用官方命名格式，迁移时无需改名，可直接复制。

- 迁移脚本：`scripts/migrate-to-huaweicloud.sh`
- 操作指南：`docs/migration-guide.md`
