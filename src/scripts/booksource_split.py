"""
书源拆分脚本

此脚本用于将合并的书源JSON文件拆分为单独的书源文件。
主要功能：
1. 读取合并的书源JSON文件
2. 将每个书源拆分为独立的JSON文件
3. 使用书源名称作为文件名保存

使用场景：
- 将旧版本的合并书源文件拆分为新的目录结构
- 方便单独维护和管理各个书源

注意：此脚本需要手动配置INPUT_FILE和OUTPUT_DIR变量
"""

import json
import pathlib

# 定义书源根目录
ROOT_DIR = pathlib.Path(__file__).parent.parent
BOOKSOURCE_ROOT_DIR = ROOT_DIR / "BookSource"

# 全局变量：指定输入文件路径和输出目录
# 使用示例：
# INPUT_FILE = ROOT_DIR.parent / "old_ver/2024.2.19-62bbe48" / "Japanese_original_bookSource.json"
INPUT_FILE = ROOT_DIR / "build" /"Japan_based_bookSource.json"
OUTPUT_DIR = BOOKSOURCE_ROOT_DIR / "Japan_based_bookSource"

def split_json_file(input_file, output_dir):
    """将指定的JSON文件拆分成多个单独的JSON文件"""
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    output_dir = pathlib.Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)  # 创建输出目录

    for item in data:
        # # 清空 bookSourceGroup
        # if "bookSourceGroup" in item:
        #     item["bookSourceGroup"] = ""

        # 使用 bookSourceName 作为文件名
        book_source_name = item.get("bookSourceName", "unknown")
        output_file = output_dir / f"{book_source_name}.json"
        
        # 将单个对象放入列表中
        item_list = [item]
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(item_list, f, ensure_ascii=False, indent=4)
        print(f"Saved {output_file}")

def main():
    split_json_file(INPUT_FILE, OUTPUT_DIR)

if __name__ == "__main__":
    main()
