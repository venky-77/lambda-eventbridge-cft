from jinja2 import Environment, FileSystemLoader
import yaml
import os

env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template('lambda-eventbridge-template.yaml.j2')

with open('parameters.yaml') as f:
    configs = yaml.safe_load(f)

os.makedirs('output', exist_ok=True)

for config in configs:
    base_name = f"{config['schema_name']}-{config['table_name']}"

    output = template.render(**configs[0])  # Use first config
    with open("output/lambda-eb-cases_base-alert_comment.yaml", "w") as f:
        f.write(output)
    # output = template.render(**config)
    # with open(f"output/lambda-eb-{base_name}.yaml", 'w') as f:
    #     f.write(output)
    print(f"✅ Generated: lambda-eb-{base_name}.yaml")
