# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.3",
# ]
# ///
import yaml
import pprint

# 读取 YAML 文件
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# 打印原始配置
print("修改前，YAML文件内容：")
pprint.pprint(config)

# 修改 YAML 配置
config['settings']['model']['name'] = 'Sonnet 4.6'

# 写回 YAML 文件
with open('config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

# 读取 修改后的 YAML 文件
with open('config.yaml', 'r') as f:
    new_config = yaml.safe_load(f)

# 打印修改后的配置
print("\n修改后，YAML文件内容：")
pprint.pprint(new_config)

