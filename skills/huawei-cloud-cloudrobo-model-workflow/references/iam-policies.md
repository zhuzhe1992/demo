# IAM Policies — CloudRobo Model Workflow

## Required IAM Permissions

The CloudRobo model workflow pipeline requires the following IAM permissions across asset management, training, inference, and dispatch services:

```json
{
  "Version": "1.1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudrobo:asset:list",
        "cloudrobo:asset:get",
        "cloudrobo:asset:create",
        "cloudrobo:asset:update",
        "cloudrobo:asset:import",
        "cloudrobo:workspace:get",
        "cloudrobo:workspace:list",
        "cloudrobo:train:createTask",
        "cloudrobo:train:getTask",
        "cloudrobo:train:getStages",
        "cloudrobo:train:getEvents",
        "cloudrobo:infer:create",
        "cloudrobo:infer:get",
        "cloudrobo:infer:start",
        "cloudrobo:infer:list",
        "cloudrobo:infer:listLogs",
        "cloudrobo:resource:listPools",
        "cloudrobo:resource:getPool",
        "cloudrobo:robot:list",
        "cloudrobo:dispatch:createTask",
        "cloudrobo:dispatch:getTask",
        "cloudrobo:dispatch:listTasks",
        "cloudrobo:dispatch:getTaskResult",
        "cloudrobo:dispatch:cancelTask"
      ]
    }
  ]
}
```

## Permission Breakdown by Stage

| Stage | Operations | Permissions |
|-------|-----------|-------------|
| Stage 0-1: Asset Query | `asset search-assets`, `asset show-asset`, `asset list-publication-assets` | `cloudrobo:asset:list`, `cloudrobo:asset:get` |
| Stage 1: Dataset Processing | `asset create-asset`, `asset create-version`, `asset update-version`, `asset import-asset` | `cloudrobo:asset:create`, `cloudrobo:asset:update`, `cloudrobo:asset:import` |
| Stage 1: Workspace | `workspace current`, `workspace use` | `cloudrobo:workspace:get`, `cloudrobo:workspace:list` |
| Stage 2: Training | `train create-task`, `train show-task`, `train get-stages`, `train get-events` | `cloudrobo:train:createTask`, `cloudrobo:train:getTask`, `cloudrobo:train:getStages`, `cloudrobo:train:getEvents` |
| Stage 3: Inference | `infer create`, `infer show`, `infer start`, `infer list`, `infer list-logs` | `cloudrobo:infer:create`, `cloudrobo:infer:get`, `cloudrobo:infer:start`, `cloudrobo:infer:list`, `cloudrobo:infer:listLogs` |
| Stage 3: Resource Pool | `resource list-pools`, `resource show-pool` | `cloudrobo:resource:listPools`, `cloudrobo:resource:getPool` |
| Stage 4: Robot | `robot list` | `cloudrobo:robot:list` |
| Stage 4: Dispatch | `dispatch create-task`, `dispatch show-task`, `dispatch list-tasks`, `dispatch show-task-result`, `dispatch cancel-task` | `cloudrobo:dispatch:createTask`, `cloudrobo:dispatch:getTask`, `cloudrobo:dispatch:listTasks`, `cloudrobo:dispatch:getTaskResult`, `cloudrobo:dispatch:cancelTask` |

## Least Privilege Principle

- Only grant specific permissions needed for the pipeline operations
- Separate read operations (List/Show/Get) from write operations (Create/Update/Delete)
- For query-only workflows, omit write permissions
- IAM policy uses JSON format with policy descriptions
