# PTSFD 后端代码

- [PTSFD 后端代码](#ptsfd-后端代码)
  - [接口文档](#接口文档)
    - [注册](#注册)
    - [登录](#登录)
    - [刷新认证令牌](#刷新认证令牌)
    - [获取用户信息](#获取用户信息)
    - [更新用户信息](#更新用户信息)
    - [请求（基础）题库](#请求基础题库)
    - [查询分数](#查询分数)
    - [存储分数](#存储分数)
  - [部署要求](#部署要求)
    - [环境](#环境)
  - [项目技术](#项目技术)

## 接口文档

### 注册

**`POST` `user/`**

- 请求参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`username`|string|用户名|
  |`password`|string|密码|
  |`repassword`|string|确认密码|

- 响应参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`access`|string|认证令牌|
  |`refresh`|string|刷新令牌|

### 登录

**`POST` `auth/`**

- 请求参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`username`|string|用户名|
  |`password`|string|密码|

- 响应参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`access`|string|认证令牌|
  |`refresh`|string|刷新令牌|

### 刷新认证令牌

**`POST` `auth/refresh/`**

- 请求参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`refresh`|string|刷新令牌|

- 响应参数

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`access`|string|认证令牌|

### 获取用户信息

**`GET` `info/`**

- 请求头

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |`Authorization`|string|Bearer \<Your Token Key\>|

- 请求参数

  |参数名|类型|描述|
  | --- | - | - |
  |nickname|string|昵称|
  |image|file|头像,文件|
  |sex|string|性别|
  |birthday|string|生日|
  |introduction|string|简介|
  |contact|string|联系方式|
  |area|string|地区|

### 更新用户信息

**`PUT/PATCH` `info/`**

- 请求头

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |Authorization|string|Bearer \<Your Token Key\>|

- 请求参数

  |参数名|类型|描述|
  | --- | - | - |
  |nickname|string|昵称|
  |image|file|头像,文件|
  |sex|string|性别|
  |birthday|string|生日|
  |introduction|string|简介|
  |contact|string|联系方式|
  |area|string|地区|

### 请求（基础）题库

**`GET` `question/`**

- 请求头

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |Advanced|string|非空：进阶题库，空值：基础题库|
  |Authorization|string|Bearer \<Your Token Key\>|

- 响应参数

  |参数名|类型|描述|
  | --- | - | - |
  |number|int|题号|
  |question|int|题目|
  |order|bool|选项正序|

### 查询分数

**`GET` `score/`**

- 请求头

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |Authorization|string|Bearer \<Your Token Key\>|

- 响应参数

  |参数名|类型|描述|
  | --- | - | - |
  |times|int|次|
  |score|int|分数|

### 存储分数

**`POST` `score/`**

- 请求头

  |参数名|类型|描述|
  | -------- | ---- | --- |
  |Authorization|string|Bearer \<Your Token Key\>|

- 请求参数

  |参数名|类型|描述|
  | --- | - | - |
  |score|int|分数|

## 部署要求

### 环境

- Python: 3.10.7
- Dependence: [requirements.txt](requirements.txt)

## 项目技术

- 框架：Django
- 接口：Django REST Framework
- 认证：Django REST Framework SimpleJWT
- 跨域：Django CORS Headers
- 美化：Django SimpleUI
