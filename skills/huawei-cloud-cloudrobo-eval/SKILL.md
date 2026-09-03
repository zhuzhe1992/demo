---
name: huawei-cloud-cloudrobo-eval
description: 模型技能仿真评测任务管理。用于创建评测任务、查询结果、批量管理评测任务和获取VNC地址。
---

# CloudRobo Eval

## Purpose

使用此 Skill 管理模型技能仿真评测任务，支持创建评测任务、查询执行结果、批量删除任务、获取仿真环境VNC地址。

不要使用此 Skill 处理模型训练或数据预处理。

## Workflow

1. 确定要评测的模型和虚拟世界
2. 准备推理服务 ID 和模型来源
3. 创建评测任务
4. 等待评测完成并获取结果

## Create Evaluation Job

```python
from cloudrobo_eval.client import EvalClient
from cloudrobo_core.sdk import Config, HttpClient

config = Config()
http = HttpClient(config)
client = EvalClient(http)

job = client.create_eval_job({
    "name": "skill-eval-1",
    "virtual_world_id": "d6e7f8a9-b0c1-2345-defa-456789012345",
    "infer_server_id": "f8a9b0c1-d2e3-4567-fabc-678901234567",
    "model_source": "CLOUDROBO_SQUARE"
})
print(f"Evaluation started: {job['id']}")
```

CLI:
```bash
cloudrobo eval create-job \
  --name skill-eval-1 \
  --virtual-world-id d6e7f8a9-b0c1-2345-defa-456789012345 \
  --infer-server-id f8a9b0c1-d2e3-4567-fabc-678901234567 \
  --model-source CLOUDROBO_SQUARE
```

## List Evaluation Jobs

```python
all_jobs = client.list_eval_jobs()
running_jobs = client.list_eval_jobs(status="running")
completed_jobs = client.list_eval_jobs(status="completed")
```

CLI:
```bash
cloudrobo eval list-jobs --status completed
```

## Show Job Detail

```python
result = client.show_eval_job(job_id="e1f2a3b4-c5d6-7890-efab-901234567890")
print(f"Status: {result['status']}")
```

CLI:
```bash
cloudrobo eval show-job --job-id e1f2a3b4-c5d6-7890-efab-901234567890
```

## Batch Delete Jobs

```python
client.batch_delete_eval_jobs([
    "f2a3b4c5-d6e7-8901-fabc-012345678901",
    "a3b4c5d6-e7f8-9012-abcd-123456789012"
])
```

CLI:
```bash
cloudrobo eval batch-delete-jobs --job-ids f2a3b4c5-d6e7-8901-fabc-012345678901,a3b4c5d6-e7f8-9012-abcd-123456789012
```

## Constraints

- 模型和推理服务必须事先存在且可访问
- 任务状态: pending, running, completed, failed
- 删除任务会同时删除评测结果

## Verification

确认评测任务创建成功、结果分数合理、批量操作正确执行。
