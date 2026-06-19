import json
import sys

# 内置站点资料
SITE_DATA = {
    "site_name": "乐鱼体育",
    "domain": "https://page-app-leyu.com.cn",
    "tag": "体育娱乐",
    "description": "提供丰富的体育赛事资讯、比分直播与互动活动",
    "keywords": ["乐鱼体育", "体育赛事", "比分直播", "体育资讯", "在线娱乐"]
}

def format_line(key, value, indent=2):
    """Format a single key-value pair for display."""
    prefix = " " * indent
    if isinstance(value, list):
        items = ", ".join(value)
        return f"{prefix}{key}: [{items}]"
    return f"{prefix}{key}: {value}"

def generate_summary(data):
    """Generate a structured summary from site data."""
    lines = []
    lines.append("=" * 50)
    lines.append("📋 站点摘要")
    lines.append("=" * 50)
    lines.append("")
    lines.append(format_line("站点名称", data["site_name"]))
    lines.append(format_line("域名", data["domain"]))
    lines.append(format_line("标签", data["tag"]))
    lines.append(format_line("简要说明", data["description"]))
    lines.append(format_line("关键词", data["keywords"]))
    lines.append("")
    lines.append("-" * 50)
    lines.append(f"生成完毕: {data['site_name']} 信息摘要")
    lines.append("-" * 50)
    return "\n".join(lines)

def summarize_to_dict(data):
    """Return a dictionary version of the summary for reuse."""
    return {
        "title": f"{data['site_name']} 摘要",
        "url": data["domain"],
        "category": data["tag"],
        "summary": data["description"],
        "tags": data["keywords"]
    }

def main():
    # Print the structured summary
    summary_text = generate_summary(SITE_DATA)
    print(summary_text)
    print()
    # Also export a JSON version
    summary_dict = summarize_to_dict(SITE_DATA)
    print(json.dumps(summary_dict, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()