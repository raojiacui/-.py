# 作业4 自动测试系统

## 使用方法

### 1. 安装依赖
```bash
pip install watchdog
```

### 2. 启动监控
```bash
cd homework4_auto_test
python watch_test.py
```

### 3. 修改代码
- 打开 `作业四.py` 进行修改
- 保存后，测试会自动运行
- 查看测试结果

## 文件说明

| 文件 | 说明 |
|------|------|
| `watch_test.py` | Watchdog 监控脚本，启动后自动监控文件变化 |
| `test_homework4.py` | 测试用例文件，包含14个作业的测试 |

## 单独运行测试
```bash
cd homework4_auto_test
python test_homework4.py
```

## 当前测试结果

```
[PASS] Passed: 55
[FAIL] Failed: 1
```

**需要修复的问题：**
- HW7 `encode2` 函数：当 shift 较大时会越界
  - 问题代码：`if index + shift == 25` 应改为 `new_index = (index + shift) % 26`
