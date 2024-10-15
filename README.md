# Ollama 聊天界面

这是一个轻量级的单页面应用程序,为 Ollama 框架提供了一个用户友好的聊天界面。它允许用户与本地运行的大型语言模型进行交互,支持实时流式响应。

![Ollama聊天界面截图](images/ollama-chat-interface.png)

## 功能特点

- 自动检测并连接本地 Ollama 服务
- 动态加载可用的语言模型列表
- 支持实时流式文本生成
- 响应式设计,适配各种设备屏幕
- Markdown 渲染支持,包括代码高亮
- 显示每次响应的生成时间
- 简洁界面,专注于对话内容
- 代码块右下角的复制功能,方便用户复制代码

## 快速开始

1. 确保本地 Ollama 服务正在运行
2. 下载 `index.html` 文件
3. 在浏览器中打开 `index.html`
4. 选择模型,开始聊天!

![快速开始步骤](images/quick-start-steps.gif)

## 系统要求

- 现代网络浏览器 (推荐 Chrome, Firefox, Safari 或 Edge 的最新版本)
- 本地运行的 Ollama 服务 (版本 0.1.14 或更高)
- 可选: 用于托管静态文件的简单 HTTP 服务器

## 安装和使用

1. 确保 Ollama 服务已在本地安装并运行:
   - 安装说明: [Ollama 官方文档](https://github.com/ollama/ollama)
   - Ollama 服务应在默认端口 11434 上运行

2. 下载本项目的 `index.html` 文件。

3. 使用方法 (选择其一):

   a. 直接在浏览器中打开:
      - 双击 `index.html` 文件在浏览器中打开
      - 注意: 某些浏览器可能会因安全策略限制而阻止直接访问本地 Ollama API

   b. 使用本地 HTTP 服务器 (推荐):
      - 使用 Python 的内置 HTTP 服务器:
        ```
        python -m http.server 8000
        ```
      - 或使用 Node.js 的 `http-server`:
        ```
        npx http-server
        ```
      - 在浏览器中访问 `http://localhost:8000` 或相应的地址

4. 在界面上选择一个可用的模型,输入消息,然后点击发送或按 Ctrl+Enter。

## 界面说明

![界面说明](images/interface-explanation.png)

1. 模型选择下拉菜单
2. 消息输入框
3. 发送按钮
4. 聊天历史记录区域
5. Ollama 服务状态指示

## 常见问题解答

Q: 如何切换不同的语言模型?
A: 在界面底部的下拉菜单中选择所需的模型即可。

![切换模型演示](images/switch-model-demo.gif)

Q: 如何清除聊天记录?
A: 目前需要刷新页面来清除聊天记录。我们计划在未来版本中添加一键清除功能。

## 配置

- Ollama API 地址: 默认设置为 `http://localhost:11434`。如需更改,请修改 `index.html` 文件中的 `apiBaseUrl` 变量。

## 故障排除

- 如果界面无法连接到 Ollama 服务:
  1. 确保 Ollama 服务正在运行
  2. 检查防火墙设置,确保允许本地连接到端口 11434
  3. 如果使用了自定义端口,更新 `apiBaseUrl`

- 如果模型列表为空:
  1. 确保已经在 Ollama 中下载了至少一个模型
  2. 可以通过 Ollama CLI 下载模型,例如: `ollama pull llama2`

## 开发和贡献

欢迎贡献代码、报告问题或提出改进建议。请访问我们的 GitHub 仓库 [链接待添加] 参与项目。

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。

## 致谢

- [Ollama](https://github.com/ollama/ollama) - 为大型语言模型提供了优秀的本地运行框架
- [Marked.js](https://marked.js.org/) - 用于 Markdown 渲染
- [Prism.js](https://prismjs.com/) - 用于代码高亮
