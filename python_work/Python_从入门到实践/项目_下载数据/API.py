import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"          #只查超过10000星的Python仓库（Github）

headers = {"Accept":"application/vnd.github.v3+json"}  #我们要使用 GitHub v3 版本的 API 格式（JSON）
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")                 #200为正常

response_dict = r.json()                               #转换为json字典

print(response_dict.keys())

print(f"Total repositories:{response_dict["total_count"]}")  #返回的符合条件的总仓库数
print(f"Complete results: {not response_dict["incomplete_results"]}")

repo_dicts = response_dict["items"]     #30个符合查询条件的仓库
print(f"Repositories returned:{len(repo_dicts)}")

repo_dict = repo_dicts[0] #取第一个仓库的信息
print(f"\nKeys: {len(repo_dict)}")
for key in sorted (repo_dict.keys()):
    print(key)

print("\nSelected information about first repository") #调取第一个仓库的具体数据
print(f"Name: {repo_dict["name"]}")
print(f"Owner: {repo_dict["owner"]["login"]}")
print(f"Stars:{repo_dict["stargazers_count"]}")

print("\nSelected information about each repository")  #调取所有仓库的具体数据
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict["name"]}")
    print(f"Owner: {repo_dict["owner"]["login"]}")
    print(f"Stars:{repo_dict["stargazers_count"]}")



repo_links, stars, hover_texts = [],[],[]
for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    
    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)
    
title = "Most-Starred Python Projects on Github"
labels= {"x" : "Repository", "y" : "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)


fig.update_layout(title_font_size = 28, xaxis_title_font_size=20,yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()


