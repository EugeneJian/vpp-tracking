#!/usr/bin/env python3
"""
AU VPP 平台兼容性跟踪 - 生成脚本
从 YAML 源数据生成 Markdown 和 HTML

使用:
    python generate.py
"""

import os
import yaml
from jinja2 import Environment, FileSystemLoader, pass_eval_context
import markdown


# 路径配置
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
TEMPLATE_DIR = os.path.join(PROJECT_ROOT, 'templates')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')


def render_compatibility(value):
    """渲染普通品牌兼容状态"""
    if value == 'compatible':
        return '√'
    return ''


def render_process_compatibility(value):
    """渲染过程态品牌兼容状态"""
    render_map = {
        'compatible': '√',
        'testing': '测试中',
        'pending_schedule': '待排期',
        'discussing': '沟通中',
        'incompatible': '未兼容',
        'unknown': '未进入'
    }
    return render_map.get(value, '')


def load_yaml_data():
    """加载YAML源数据"""
    yaml_file = os.path.join(DATA_DIR, 'au_vpp_partners.yaml')
    with open(yaml_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_markdown(data):
    """生成Markdown文件"""
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        trim_blocks=True,
        lstrip_blocks=True
    )

    # 注册自定义过滤器
    env.filters['render_compatibility'] = render_compatibility
    env.filters['render_process_compatibility'] = render_process_compatibility

    template = env.get_template('markdown_template.md')

    # 将渲染函数也传递给模板上下文
    context = dict(data)
    context['render_compatibility'] = render_compatibility
    context['render_process_compatibility'] = render_process_compatibility

    return template.render(**context)


def markdown_to_html(md_content, data):
    """将Markdown转换为HTML"""
    # 扩展功能
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'nl2br']
    )

    # 添加HTML头部和样式
    html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --bg: #fafafa;
            --card: #ffffff;
            --text: #1a1a1a;
            --text-secondary: #666666;
            --border: #e5e5e5;
            --accent: #2563eb;
            --accent-light: #eff6ff;
            --success: #16a34a;
            --warning: #d97706;
            --danger: #dc2626;
            --muted: #9ca3af;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.5;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        header {{
            margin-bottom: 32px;
        }}
        h1 {{
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 8px;
            letter-spacing: -0.5px;
        }}
        .meta {{
            color: var(--text-secondary);
            font-size: 14px;
        }}
        .card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
        }}
        h2 {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
            color: var(--text);
        }}
        h3 {{
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 12px;
            color: var(--text);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 14px;
        }}
        th, td {{
            padding: 10px 12px;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }}
        th {{
            font-weight: 500;
            color: var(--text-secondary);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        tr:hover {{ background: #fafafa; }}
        .platform-name {{
            font-weight: 500;
        }}
        .priority {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 500;
        }}
        .priority-high {{ background: #fef2f2; color: var(--danger); }}
        .priority-medium {{ background: #fffbeb; color: var(--warning); }}
        .priority-low {{ background: #f0fdf4; color: var(--success); }}
        .compat {{
            font-size: 12px;
        }}
        .compat-yes {{ color: var(--success); }}
        .compat-no {{ color: var(--muted); }}
        .compat-testing {{ color: var(--warning); }}
        .compat-pending {{ color: var(--text-secondary); }}
        .tag {{
            display: inline-block;
            background: var(--accent-light);
            color: var(--accent);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 12px;
            margin-right: 4px;
        }}
        .status {{
            font-size: 13px;
        }}
        .detail-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin-bottom: 20px;
        }}
        .detail-item label {{
            font-size: 12px;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .detail-item p {{
            margin-top: 4px;
        }}
        .info-row {{
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
        }}
        .info-item {{ margin-bottom: 8px; }}
        .info-item label {{
            font-size: 12px;
            color: var(--text-secondary);
            margin-right: 8px;
        }}
        .link {{
            color: var(--accent);
            text-decoration: none;
        }}
        .link:hover {{ text-decoration: underline; }}
        .empty {{ color: var(--muted); font-style: italic; }}
        blockquote {{
            border-left: 3px solid var(--accent);
            padding-left: 16px;
            margin: 16px 0;
            color: var(--text-secondary);
        }}
        code {{
            background: var(--bg);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 13px;
        }}
        hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 24px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
{content}
    </div>
</body>
</html>"""

    return html_template.format(
        title=data.get('dataset_name', 'AU VPP 平台兼容性跟踪'),
        content=html_content
    )


def main():
    """主函数"""
    print("开始生成 AU VPP 平台兼容性跟踪文档...")

    # 确保输出目录存在
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 加载数据
    print("加载 YAML 数据...")
    data = load_yaml_data()

    # 生成 Markdown
    print("生成 Markdown...")
    md_content = generate_markdown(data)

    # 保存 Markdown
    md_file = os.path.join(OUTPUT_DIR, 'au_vpp_partners.md')
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Markdown 已保存: {md_file}")

    # 生成 HTML
    print("生成 HTML...")
    html_content = markdown_to_html(md_content, data)

    # 保存 HTML
    html_file = os.path.join(OUTPUT_DIR, 'au_vpp_partners.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML 已保存: {html_file}")

    print("\n生成完成!")
    print(f"  - Markdown: {md_file}")
    print(f"  - HTML: {html_file}")


if __name__ == '__main__':
    main()
