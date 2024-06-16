# Personalized LLM Research Assistent (个性化大语言模型领域研究助理)

随着大语言模型(LLMs)
在自然语言处理领域取得显著进展,其在人机交互方面展现出巨大潜力。然而,当前LLMs主要对齐整体人类偏好,难以充分满足用户的个性化需求。
鉴于人类价值观和偏好的多样性,以及语用在人际交互中的重要性,我们认为LLMs的发展需要从对齐群体偏好转向个性化。个性化大语言模型(
Personalized LLM)被认为是LLMs发展历程中的下一个重要步骤,但目前尚未在大规模应用中得到充分实现[1]
。作为一个前沿研究领域,学者们迫切需要一个可靠的工具来回答与该领域相关的专业问题。
我们的目标是开发一个定制化的问答机器人,专注于为学者提供个性化大语言模型领域的专业知识和有价值的参考资料。
该机器人将具备以下特点:

1. 专业性:深入了解个性化大语言模型领域的最新进展,提供权威、可靠的信息。
2. 交互性:通过自然语言交互,营造友好、高效的问答体验,鼓励学者深入探讨。
3. 可扩展性:随着研究的深入,不断更新知识库,确保信息与时俱进。

我们相信,这样一个专注于个性化大语言模型领域的定制化问答机器人,将为学者们提供强有力的支持,促进该领域的研究和创新。

[1] Personalisation within bounds: A risk taxonomy and policy framework for the alignment of large language models
with personalised feedback HR Kirk, B Vidgen, P Röttger, SA Hale - arXiv preprint arXiv:2303.05453, 2023

## NEWs

- [2024.06.16] Counterfactual 发布 Personalized LLM Research Assistent V0.1. 
- [2024.06.10] Personalized LLM Research
  Assistent [GPT Agent](https://chatgpt.com/share/30ba0ff4-2986-4d40-9db6-0a97b10a0b82) & [茴香豆创建的助手](https://openxlab.org.cn/apps/detail/tpoisonooo/huixiangdou-web)
  测试发现效果一般.
![img.png](asset/PLMM.png)


## 技术路线

具体来说,我们将采用以下技术框架:

![Personalized LLM Research Assistent](asset/framework.jpg)

如上图所示,我们的系统由以下几个模块组成:

- Dataset: 个性化大语言模型领域的专业知识和有价值的参考资料。
- Model: 个性化大语言模型,用于回答用户提出的问题, 包括 InternLM2, Llamm3, DeepseekV2等。
- Method: 探索多种方法, 包括 RAG, 增量预训练, SFT, 偏好学习等, 帮助模型获得领域专业知识, 成为个性化大模型领域研究助理.
- Application: 模型评估, 推理优化, 模型部署等.

### 1. Dataset

我们的数据集是从个性化大语言模型领域的专业知识和有价值的参考资料中提取的, 通过专业人员的筛选, 整理, 生成的。

- [论文资料收集](https://swze06osuex.feishu.cn/docx/VvfbdgciDohaNDxKnj0ccTBTnad?from=from_copylink)
- ....

### 2. Model

我们将采用多种大语言模型, 包括 InternLM2, Llamm3, DeepseekV2等, 用于回答用户提出的问题。

### 3. Method

我们将探索多种方法, 包括 RAG, 增量预训练, SFT, 偏好学习等, 帮助模型获得领域专业知识, 成为个性化大模型领域研究助理.

### 4. Application

我们将对模型进行评估, 推理优化, 模型部署等, 以提供更好的服务.

## 开发计划

想要开发出来对于领域知识有深入理解的研究助理, 不会是什么容易的事情. 我们要考虑很多维度, 包括数据集的质量, 模型的性能,
方法的有效性, 应用的实用性等等. 我们的开发计划如下:

- [x] 数据集的构建(论文等)
- [x] 模型的选择(InternLM2, Llamm3, DeepseekV2等)
- [x] 方法的探索(RAG, 增量预训练, SFT, 偏好学习等)
- [x] 应用的开发


## 常见问题 QA

Q1. 为什么要开发这个机器人?

A1. 个性化大语言模型领域是一个前沿研究领域,学者们迫切需要一个可靠的工具来回答与该领域相关的专业问题。更加具体的来说,
是我们正在进行一个个性化大语言模型的研究项目, 所以需要一个该领域的研究助理, 帮助整理文献, 写作论文, 启发思考等.

Q2. 直接使用茴香豆或者其他做 RAG 不就够了吗? 为什么还在考虑微调?

A2. RAG 技术很好, 但是模型没有深入理解个性化大语言模型领域的专业知识和有价值的参考资料, 所以需要微调. 当下最强大的
RAG 技术(我们制作的 GPT Agent for Personalized LLM Research)依旧效果完全达不到我们的预期. 所以我们的目的是希望大模型能真正的掌握这个领域的专业知识,
这样或许能成为我们更好的科研助理。

Q3. 微调数据集如何获得?

A3. 我们的数据集是从个性化大语言模型领域的专业知识和有价值的参考资料中提取的, 通过专业人员的筛选, 整理, 生成的.

Q4. 和书生·浦语大模型实战营什么关系?

A4. 书生·浦语大模型实战营是学习大模型全链路开发的系统化课程, 个性化大语言研究助理项目的开发依赖于这些知识的掌握.



