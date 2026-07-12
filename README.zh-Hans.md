# clreq-skills

[English](README.md) | 简体中文

为智能体提供有来源依据的中文文案、国际化与排版检查。

`clreq` 可以帮助 Codex、Claude Code 和其他支持 Agent Skills 格式的编程智能体审查 HTML、JSX、TSX、Vue、Svelte、Markdown、MDX、本地化资源及 CSS 中面向用户的中文内容。每条审查结果包含建议操作、置信度，以及相关标准或指南的来源。

## 30 秒了解效果

假设页面中包含：

```html
<html lang="zh">
  <p>今天下单, 明天发货.</p>
</html>
```

同时使用CSS旋转了中文文字：

```css
.vertical-label {
  transform: rotate(90deg);
}
```

向智能体发送：

```text
使用 $clreq 审查 samples/web-smoke/index.html 和 samples/web-smoke/styles.css。
```

可以查看[完整smoke示例](samples/web-smoke/README.md)及其[预期审查结果](samples/web-smoke/expected-review.md)。

## 安装

全局安装：

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --global
```

为当前项目安装：

```sh
npx skills@latest add xfq/clreq-skills --skill clreq
```

可安装的技能包是自包含的 `skills/clreq/` 目录。

## 使用

审查指定文件：

```text
使用 $clreq 审查 src/components/Checkout.tsx 里的中文文本和排版问题。
```

审查改动的文件：

```text
使用 $clreq 审查当前 diff 中变更的文件。
```

审查本地化资源：

```text
/clreq review src/locales/zh-Hant.json
```

技能只处理已经明确指定或位于当前任务范围内的文件与diff，默认不会扫描整个仓库。

## 项目结构

项目把通用规则包与平台接入层分开维护：

- `skills/clreq/`：自包含、可直接安装的技能包。
- `rules/`：原子规则卡的内容编写源。
- `fixtures/`：聚焦单项规则的输入与预期审查示例。
- `schema/`：规则卡使用的 JSON Schema。
- `adapters/`：不同平台的开发参考适配器。
- `samples/`：端到端审查示例。

## 开发

根目录中的 `rules/`、`fixtures/`、`schema/` 和参考适配器是内容编写时的事实来源。修改后需要同步更新技能包内的副本，并检查可安装版本是否一致：

```sh
./scripts/check-packaged-skill.sh
```

## 来源

每条规则都必须注明依据。基于 CLReq 的规则会链接至[《中文排版需求》](https://www.w3.org/TR/clreq/)或密切相关的 W3C 国际化资料；涉及 Web 实现的指南会引用相应的 HTML、CSS、Unicode 或其他权威来源。

## 许可证

本项目采用 W3C Software and Document License，详见 [LICENSE.md](LICENSE.md)。
