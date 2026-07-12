# clreq-skills

[English](README.md) | 简体中文

`clreq-skills` 把中文文本的排版指南封装为可供编程智能体使用的规则与skill。本项目基于 [《中文排版需求》（CLReq）](https://github.com/w3c/clreq)及相关资料构建。

## 项目结构

项目核心是一套通用规则包，平台适配器负责将其接入不同的智能体。

## 安装

从GitHub安装 `clreq` 技能：

```sh
npx skills@latest add xfq/clreq-skills --skill clreq
```

全局安装：

```sh
npx skills@latest add xfq/clreq-skills --skill clreq --global
```

## 在智能体中使用

安装技能后，可以向智能体发送类似下面的提示词：

```text
使用 $clreq 审查这个页面里的中文文本和排版。
```

可安装的技能包位于 `skills/clreq/`。该目录是自包含的，因此复制安装后不依赖技能目录之外的文件。`adapters/` 下的内容是针对不同平台的开发参考，不作为安装入口。

根目录中的 `rules/`、`fixtures/`、`schema/` 和参考适配器是内容编写时的事实来源。修改这些文件后，需要同步更新技能包内的副本，并运行以下脚本检查两者是否一致：

```sh
./scripts/check-packaged-skill.sh
```

## 规则范围

当前规则涵盖以下方向：

- 中文语言与地区元数据；
- 中文标点符号；
- 中文与西文混排；
- 简繁转换中的语境判断；
- Web 竖排实现；
- Ruby、拼音等注音标记的语义化实现。

技能默认给出简洁、带来源依据的审查建议，不会在用户未明确要求时修改文件。

## 来源标注

每条规则都必须注明其依据。基于CLReq的规则应链接至CLReq、Chinese Gap Analysis或相关中文排版需求资料；涉及Web实现的指南应引用相应的HTML、CSS、Unicode或其他权威来源。

## 许可证

本项目采用W3C Software and Document License，详见[LICENSE.md](LICENSE.md)。
