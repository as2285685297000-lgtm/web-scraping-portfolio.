"""
超级简单的GitHub爬虫 - 适合初学者
"""

import requests

print("🐱 简单GitHub信息查询")
print("=" * 40)

# 要查询的用户名
username = "torvalds"  # Linux创始人

# 构建API链接
url = f"https://api.github.com/users/{username}"

print(f"正在查询用户: {username}")
print(f"请求地址: {url}")

try:
    # 发送请求
    response = requests.get(url)
    
    if response.status_code == 200:
        print("✅ 查询成功！")
        print("-" * 30)
        
        # 解析JSON数据
        data = response.json()
        
        # 显示基本信息
        print(f"用户名: {data.get('login')}")
        print(f"昵称: {data.get('name', '未知')}")
        print(f"粉丝数: {data.get('followers', 0)}")
        print(f"仓库数: {data.get('public_repos', 0)}")
        print(f"创建时间: {data.get('created_at')[:10]}")  # 只取日期
        
        # 显示头像URL
        avatar = data.get('avatar_url')
        print(f"头像链接: {avatar}")
        
        print("\n🌟 试试修改第8行的用户名，查询其他用户！")
        
    else:
        print(f"❌ 查询失败，状态码: {response.status_code}")
        
except Exception as e:
    print(f"⚠️ 发生错误: {str(e)}")

print("=" * 40)
print("🎉 程序运行结束！")
