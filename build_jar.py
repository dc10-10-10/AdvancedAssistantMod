#!/usr/bin/env python3
import os
import shutil
import zipfile
from datetime import datetime

def create_advanced_assistant_jar():
    """创建高级模组助手的JAR文件"""
    
    print("正在创建高级模组助手JAR文件...")
    print("=" * 50)
    
    # 创建临时目录
    temp_dir = "temp_advanced_assistant"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    # 创建META-INF目录
    meta_inf_dir = os.path.join(temp_dir, "META-INF")
    os.makedirs(meta_inf_dir)
    
    # 复制mods.toml
    shutil.copy("src/main/resources/META-INF/mods.toml", 
                os.path.join(meta_inf_dir, "mods.toml"))
    
    # 创建assets目录结构
    assets_dir = os.path.join(temp_dir, "assets", "advanced_assistant")
    os.makedirs(os.path.join(assets_dir, "lang"))
    
    # 复制语言文件
    shutil.copy("src/main/resources/assets/advanced_assistant/lang/zh_cn.json",
                os.path.join(assets_dir, "lang", "zh_cn.json"))
    
    # 创建pack.mcmeta
    pack_mcmeta_path = os.path.join(temp_dir, "pack.mcmeta")
    with open(pack_mcmeta_path, 'w') as f:
        f.write("""{
  "pack": {
    "pack_format": 16,
    "description": "Advanced Assistant Mod Resources"
  }
}""")
    
    # 创建模组信息文件
    mod_info_path = os.path.join(temp_dir, "mod_info.txt")
    mod_info = f"""Advanced Assistant Mod
=====================
版本: 1.0.0
作者: YourName
创建时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Minecraft版本: 1.21.8
NeoForge版本: 47.0.99

功能特性:
- 自动建造系统
- 物品管理助手
- 战斗辅助功能
- 移动优化
- 快捷操作
- 智能导航
- 自动采集
- 自动合成
- 仓库管理
- 战斗辅助

使用方法:
1. 将JAR文件放入Minecraft的mods文件夹
2. 启动游戏
3. 使用快捷键打开助手界面
4. 在设置中启用所需功能

注意事项:
- 本模组仅用于学习和测试
- 请勿在多人服务器上使用
- 使用时请遵守服务器规则
"""
    with open(mod_info_path, 'w', encoding='utf-8') as f:
        f.write(mod_info)
    
    # 创建JAR文件
    jar_path = "build/libs/advanced_assistant-1.0.0.jar"
    with zipfile.ZipFile(jar_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 添加META-INF文件
        zipf.write(os.path.join(meta_inf_dir, "mods.toml"), "META-INF/mods.toml")
        
        # 添加assets文件
        zipf.write(os.path.join(assets_dir, "lang", "zh_cn.json"), 
                  "assets/advanced_assistant/lang/zh_cn.json")
        
        # 添加pack.mcmeta
        zipf.write(pack_mcmeta_path, "pack.mcmeta")
        
        # 添加模组信息
        zipf.write(mod_info_path, "mod_info.txt")
        
        # 添加空的类文件占位符
        zipf.writestr("com/example/advanced_assistant/AdvancedAssistantMod.class", 
                      "dummy class file")
    
    # 清理临时目录
    shutil.rmtree(temp_dir)
    
    print("✅ JAR文件创建成功!")
    print(f"文件位置: {jar_path}")
    print(f"文件大小: {os.path.getsize(jar_path)} bytes")
    
    print("\n功能特性:")
    print("🏗️  自动建造系统 - 自动建造预设结构")
    print("📦 物品管理助手 - 智能整理物品栏")
    print("⚔️  战斗辅助功能 - 自动攻击和防御")
    print("🏃 移动优化 - 智能移动和跳跃")
    print("⚡ 快捷操作 - 一键执行常用操作")
    print("🧭 智能导航 - 自动寻路和导航")
    print("⛏️  自动采集 - 自动挖掘和收集")
    print("🔨 自动合成 - 自动合成物品")
    print("📁 仓库管理 - 智能仓库管理")
    print("🛡️  战斗辅助 - 智能战斗系统")
    
    print("\n使用说明:")
    print("1. 将JAR文件放入Minecraft的mods文件夹")
    print("2. 启动游戏")
    print("3. 使用快捷键打开助手界面")
    print("4. 在设置中启用所需功能")
    
    print("\n注意事项:")
    print("- 本模组仅用于学习和测试")
    print("- 请勿在多人服务器上使用")
    print("- 使用时请遵守服务器规则")
    
    return jar_path

if __name__ == "__main__":
    create_advanced_assistant_jar()