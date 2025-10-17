# 轻小说阅读书源合集
`Light-Novel-Yuedu-Source`

> [!IMPORTANT]
> **该项目目前处在半维护周期内**
> 
> 目前由 [@洛初](https://github.com/gongfuture) 转入半维护周期。由于能力不足和精力有限等原因，任何对于书源的issue，可能都不会及时进行解决。
> 
> **欢迎 fork 本仓库修复维护后提出 PR 进行合并。**

> [!CAUTION]
> **转载声明**
> - 内容转载请保持原说明
> - 书源转载整合请保持原源名称以及原源注释

## 介绍

本仓库收集整理了适用于阅读APP的轻小说书源，包括日轻、国轻及日语原版轻小说等多种类型。由于项目处在半维护周期，不保证所有书源的持续有效性。

## 书源文件说明

| 文件名 | 说明 |
| --- | --- |
| `Japan_based_bookSource.json` | 日轻小说书源文件 |
| `China_based_bookSource.json` | 国轻小说书源文件 |
| `Japanese_original_bookSource.json` | 日语原版轻小说书源文件 |
| `All_bookSource.json` | 日轻、国轻、日语原版书源合集文件 |

> [!TIP]
> 部分书源的完整注释内容请参考 [`/docs/original_comment.md`](/docs/original_comment.md) 文件

## 使用说明

### 基本说明

1. 使用这些书源时不需要额外的净化规则
2. 由于该项目处在半维护周期内，不保证书源的持续有效性

### 需要登录的书源

以下书源需要登录后方可正常使用：
- `真白萌`
- `轻小说文库(.cc)`
- `轻小说文库(.net)`
- `有度轻小说`

### 搜索问题解决方案

部分书源搜索功能存在问题。如遇到搜索不准确的情况，建议：
1. 前往原网站找到所需阅读书籍的网址
2. 在阅读APP主页面右上角菜单 ⠇ 中使用 `添加网址` 功能导入书籍

### 更多说明

- 日语原版轻小说书源的详细说明请见：[日本Web小说 Book Source](https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases/tag/JA)
- 详细的原使用说明请见：[原README文件](/old_ver/README.md)

## 导入方法

### 方式一：直接导入书源

1. 访问 [Release发行版](https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases)
2. 复制所需书源/书源合集的JSON文件链接或下载对应文件
3. 打开阅读APP
4. 进入 `我的` → `书源管理`
5. 点击右上角菜单 ⠇
6. 选择 `网络导入` 或 `本地导入`
7. 粘贴链接或选择文件
8. 确认导入

### 方式二：订阅源导入（推荐）

> [!TIP]
> 使用规则订阅可以便于后续更新书源

#### 订阅步骤

1. 从下方表格复制对应订阅源的链接
2. 打开阅读APP
3. 进入 `订阅` → `规则订阅`
4. 点击右上角添加 `+`
5. 类型选择 `书源`，填写任意名称，在 `Url` 框内粘贴链接
6. 确认添加

#### 订阅源链接

| 订阅源类型 | 订阅链接 |
| --- | --- |
| 日轻小说 | `https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases/latest/download/Japan_based_bookSource.json` |
| 国轻小说 | `https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases/latest/download/China_based_bookSource.json` |
| 日语原版轻小说 | `https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases/latest/download/Japanese_original_bookSource.json` |
| 所有书源 | `https://github.com/gongfuture/Light-Novel-Yuedu-Source/releases/latest/download/All_bookSource.json` |

> [!TIP]
> 可以直接订阅所有书源，然后仅打开所需的对应分组

## 登录方法

对于需要登录的书源，可以通过以下任意位置进行登录：
- 发现页菜单中的"登录"
- 管理书源菜单中的"登录"
- 编辑书源菜单中的"登录"

> [!NOTE]
> 登录完成后，请点击右上方的 √ 保存返回，即可正常使用

## 贡献者

<a href="https://github.com/gongfuture/Light-Novel-Yuedu-Source/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gongfuture/Light-Novel-Yuedu-Source"  alt="Light-Novel-Yuedu-Source Contributors"/>
</a>

## 备注说明

### 书源维护历史

1. **哔哩轻小说**：原始源缝合了源仓库里**叶落岚起+关耳/乃星**改的灰色章节可阅的规则脚本，后续又由**酷安@吉王义昊**以及**柚屿☆**等多位进行多次修正维护。由于原网站使用了各种防爬措施以及字体混淆等，基本无法长期正常使用
2. **轻之国度(LK)**：（2022年前）维护完毕后网站有所改动，先前的源全部失效，由 [酷安@转义字符](http://www.coolapk.com/u/2060038) 以及 [酷安@金01461](http://www.coolapk.com/u/1208939) 重新编写，新源可正常使用
3. **ESJ**：源来自 [酷安@户山香澄Official](http://www.coolapk.com/u/614507) 的[帖子](https://www.coolapk.com/feed/33474742)并做了更新，详细使用说明请看[另一原帖](https://www.coolapk.com/feed/32715700)。发现功能若需正常使用请科学上网后登录

### 替代方案

- **动漫之家**：轻小说站如有需要可使用 [动漫之家Flutter客户端](https://github.com/xiaoyaocz/dmzj_flutter)

### 其他说明

- 本仓库内书源的发现功能使用了 [酷安@关耳010225](http://www.coolapk.com/u/2379204) 提供的方法进行了美化，大部分源的发现均有进行增加
- 内容来源于酷安评论区、源仓库，未发帖公开的源均已得到原作者许可公开
- ~~筛选、修复解析和发现保证使用有效~~ 由于该项目处在半维护周期内，不保证书源的持续有效性
