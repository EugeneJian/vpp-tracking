# 澳洲三方平台兼容性跟踪

> 区域：AU
> 最后更新：2026-03-12
> 数据源：主数据 YAML
> 主线品牌：Growatt
> 说明：本文档由 YAML 自动生成，请勿作为主数据直接维护。

<div class="card">

## 1. PM / PLM 总览

| 平台 | 优先级 | Growatt 状态 | 匹配度 | 当前阶段 | 当前阶段说明 | 下一任务 |
|---|---|---|---:|---|---|---|
| Switch DIN | 中 | √ | 74 | 已在对方清单 | 兼容已确认，暂无新增推进动作 | 补全 Switch DIN 官方兼容页面并确认是否可对外引用 |
| CovaU | 中 | √ | 73 | 已在对方清单 | 兼容已确认，尚未展开深度商务动作 | 确认 CovaU 对 Growatt 的具体接入范围和对外说法 |
| Evergen | 高 | 未进入 | 92 | 已在对方清单 | 停留在外部兼容清单观察阶段 | 获取 Evergen 技术接口和认证流程，启动首次对接 |
| Amber | 高 | 测试中 | 88 | 沟通中 | 已约 2026-03-16 16:00-16:30 技术交流 | 完成与 Amber 的 2026-03-16 16:00-16:30 技术交流并确认对接范围 |
| Origin | 高 | 待排期 | 86 | 沟通中 | 等待三方 kick-off meeting 排期确认 | 锁定三方 kick-off 时间并确认参会角色 |
| Globird | 中 | 未进入 | 80 | 沟通中 | 等待测试环境和接入样本准备 | 组织 100 个客户接入样本并搭建测试环境 |
| ShineHub | 中 | 未进入 | 58 | 报价阶段 | 报价评估阶段 | 评估报价投入产出并确认是否进入采购/商务谈判 |
| AGL | 中 | 未进入 | 69 | 沟通中 | 已约 2026-03-16 12:00-12:30 面对面交流 | 完成与 AGL 的 2026-03-16 12:00-12:30 面对面交流并确认下一步动作 |
| Manta | 中 | 沟通中 | 76 | 沟通中 | 等待下周会议确认真实接入路径 | 完成与 Manta 的下周会议并确认产品、接口和测试需求 |
| Future X Power | 低 | 未进入 | 35 | 生态合作 | 生态关系记录 | 保持生态关系备注，不单独投入推进 |
| Ecotricity | 低 | 未进入 | 28 | 区域关联 | 区域关联备注 | 继续保持关联记录，无需单独推进 |

</div>

<div class="card">

## 2. Competitor Analysis

| 平台 | Growatt | Sigen Energy | FOXESS | Sungrow | SolaX | Goodwe | Alpha | 竞品亮点 |
|---|---|---|---|---|---|---|---|---|
| Switch DIN | √ |  |  | √ | √ | √ | √ | Sungrow / SolaX / Goodwe / Alpha 已兼容；Growatt 已具备进入条件，适合作为已完成样板 |
| CovaU | √ |  | √ |  |  |  | √ | FOXESS / Alpha 已兼容；Growatt 已兼容，可作为轻量参考样板 |
| Evergen | 未进入 | √ | √ | √ | √ | √ | √ | 六个主竞品品牌均已兼容；属于最明显的 Growatt 覆盖缺口 |
| Amber | 测试中 | √ | √ | √ |  |  | √ | Sigen / FOXESS / Sungrow / Alpha 已兼容；Growatt 已从空白进入测试推进 |
| Origin | 待排期 | √ |  | √ | √ | √ | √ | Sigen / Sungrow / SolaX / Goodwe / Alpha 已兼容；Growatt 已进入排期等待 |
| Globird | 未进入 | √ |  | √ | √ |  | √ | Sigen / Sungrow / SolaX / Alpha 已兼容；Growatt 尚未形成公开兼容 |
| ShineHub | 未进入 | √ |  |  |  |  |  | Sigen Energy 已具备合作信息；当前更偏报价和商务判断 |
| AGL | 未进入 | √ |  | √ |  |  | √ | Sigen / Sungrow / Alpha 已兼容；Growatt 尚无明确信号 |
| Manta | 沟通中 |  |  |  |  | √ |  | 已知 Goodwe 兼容；Growatt 已进入直接沟通状态 |
| Future X Power | 未进入 | √ |  |  |  |  |  | 与 Amber 存在合作关系 |
| Ecotricity | 未进入 | √ |  |  |  |  |  | 与 Amber 存在区域运营关联说明 |

</div>

## 3. 平台详情

<div class="card">

### Switch DIN

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-switch-din</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>VPP / Aggregator</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 74 / 100（中匹配）
- **匹配判断**: Growatt 已在兼容面内，可作为已拿下平台案例；但对新品导入和商务增量的拉动有限。
- **Growatt 定位**: 已兼容，可作为存量案例维护

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | unknown |
| FOXESS | unknown |
| Sungrow | compatible |
| SolaX | compatible |
| Goodwe | compatible |
| Alpha | compatible |
| Growatt | compatible |

**其他品牌**: Solaredge

#### 推进状态

- **当前阶段**: 已在对方清单
- **当前阶段说明**: 兼容已确认，暂无新增推进动作
- **下一步动作**: 补全平台资料，沉淀为 Growatt 参考案例。
- **下一任务**: 补全 Switch DIN 官方兼容页面并确认是否可对外引用
- **任务 Owner**: 内部产品运营
- **成功标准**: 获得完整链接并确认案例可复用

#### Competitor Highlights

- Sungrow / SolaX / Goodwe / Alpha 已兼容
- Growatt 已具备进入条件，适合作为已完成样板

#### 备注

- 平台链接仍为截断状态，后续建议补全。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 桌面研究 | 复核 Switch DIN 兼容清单 | 确认 Growatt 已在兼容面内 |


#### 链接

- **平台链接**: [https://support.switchdin.com/hc/en-](https://support.switchdin.com/hc/en-) (截图截断/待补全)

- **需求文档**: 无

#### 标签

<span class="tag">Growatt 已兼容</span>

</div>
<div class="card">

### CovaU

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-covau</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>Retailer / VPP</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 73 / 100（中匹配）
- **匹配判断**: Growatt 已兼容，但竞品覆盖面不算广，价值偏验证型，不是当前主攻资源位。
- **Growatt 定位**: 已兼容，后续以运营维护为主

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | unknown |
| FOXESS | compatible |
| Sungrow | unknown |
| SolaX | unknown |
| Goodwe | unknown |
| Alpha | compatible |
| Growatt | compatible |


#### 推进状态

- **当前阶段**: 已在对方清单
- **当前阶段说明**: 兼容已确认，尚未展开深度商务动作
- **下一步动作**: 补充完整兼容证据，确认是否有业务放量空间。
- **下一任务**: 确认 CovaU 对 Growatt 的具体接入范围和对外说法
- **任务 Owner**: 内部产品运营
- **成功标准**: 形成可复用的兼容说明

#### Competitor Highlights

- FOXESS / Alpha 已兼容
- Growatt 已兼容，可作为轻量参考样板

#### 备注

- 平台链接为截断状态，建议后续补全。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 桌面研究 | 复核 CovaU 兼容名单 | 确认 Growatt 已兼容 |


#### 链接

- **平台链接**: [https://www.covau.com.au/docs/vpp/how-do-i-know-if-my-](https://www.covau.com.au/docs/vpp/how-do-i-know-if-my-) (截图截断/待补全)

- **需求文档**: 无

#### 标签

<span class="tag">Growatt 已兼容</span>

</div>
<div class="card">

### Evergen

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-evergen</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>VPP / EMS</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-high">高</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 92 / 100（高匹配）
- **匹配判断**: 典型高价值缺口平台。竞品覆盖完整，但 Growatt 尚未进入，适合作为主战场优先突破。
- **Growatt 定位**: 高优先级补位目标

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | compatible |
| Sungrow | compatible |
| SolaX | compatible |
| Goodwe | compatible |
| Alpha | compatible |
| Growatt | unknown |

**其他品牌**: Anker、Deye、Solaredge

#### 推进状态

- **当前阶段**: 已在对方清单
- **当前阶段说明**: 停留在外部兼容清单观察阶段
- **下一步动作**: 发起对接，确认 Growatt 进入兼容/测试的门槛。
- **下一任务**: 获取 Evergen 技术接口和认证流程，启动首次对接
- **任务 Owner**: Growatt BD + 产品
- **成功标准**: 明确接入门槛、所需资料和测试路径

#### Competitor Highlights

- 六个主竞品品牌均已兼容
- 属于最明显的 Growatt 覆盖缺口

#### 备注

- OEM requirement 文档链接为截断状态，建议补全。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 桌面研究 | 复核 Evergen integrated partners 清单 | 确认六大主竞品均已兼容，Growatt 仍为空白 |


#### 链接

- **平台链接**: [https://evergen.energy/integrated-partners/](https://evergen.energy/integrated-partners/) (有效)

- **需求文档**: [https://evergen-public.notion.site/OEM-](https://evergen-public.notion.site/OEM-) (截图截断/待补全)

#### 标签

<span class="tag">重点平台</span>
<span class="tag">竞品领先</span>
<span class="tag">Growatt 缺口</span>

</div>
<div class="card">

### Amber

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-amber</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>Retailer / VPP</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-high">高</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 88 / 100（高匹配）
- **匹配判断**: Growatt 已进入测试前后阶段，平台价值高、反馈链路清晰，属于近期最应推进落地的平台之一。
- **Growatt 定位**: 在途重点项目

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | compatible |
| Sungrow | compatible |
| SolaX | incompatible |
| Goodwe | incompatible |
| Alpha | compatible |
| Growatt | testing |

**其他品牌**: Solaredge、Anker

#### 推进状态

- **当前阶段**: 沟通中
- **当前阶段说明**: 已约 2026-03-16 16:00-16:30 技术交流
- **下一步动作**: 完成 2026-03-16 技术交流并确认接口人、评审范围和后续测试安排。
- **下一任务**: 完成与 Amber 的 2026-03-16 16:00-16:30 技术交流并确认对接范围
- **任务 Owner**: Growatt BD + Amber
- **成功标准**: 完成技术交流并明确接口人、技术范围和下一步测试安排

#### Competitor Highlights

- Sigen / FOXESS / Sungrow / Alpha 已兼容
- Growatt 已从空白进入测试推进

#### 备注

- 已完成统一 API 文档投递。
- Amber 于 2026-03-12 回复并确认下周一下午技术交流。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-06 | 外部触达 | 发送统一 API 文档 | 进入技术对接等待阶段 |
| 2026-03-12 | 会议/排期 | Amber 回复并确认 2026-03-16 16:00-16:30 技术交流 | 已从等待回复进入已约技术交流阶段 |


#### 链接

- **平台链接**: [https://www.amber.com.au/smartshift-compatibility-checker](https://www.amber.com.au/smartshift-compatibility-checker) (有效)

- **需求文档**: 无

#### 标签

<span class="tag">重点推进</span>
<span class="tag">Growatt 主线</span>

</div>
<div class="card">

### Origin

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-origin</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>Retailer / VPP</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-high">高</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 86 / 100（高匹配）
- **匹配判断**: Origin 对 Growatt 已有明确排期意向，且多竞品已兼容，适合作为高层资源协调的重点机会。
- **Growatt 定位**: 高价值待排期机会

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | compatible |
| SolaX | compatible |
| Goodwe | compatible |
| Alpha | compatible |
| Growatt | pending_schedule |

**其他品牌**: Solaredge、Anker

#### 推进状态

- **当前阶段**: 沟通中
- **当前阶段说明**: 等待三方 kick-off meeting 排期确认
- **下一步动作**: 推动三方 kick-off 会议确定时间。
- **下一任务**: 锁定三方 kick-off 时间并确认参会角色
- **任务 Owner**: Growatt BD
- **成功标准**: 会议落档并进入接口评审

#### Competitor Highlights

- Sigen / Sungrow / SolaX / Goodwe / Alpha 已兼容
- Growatt 已进入排期等待

#### 备注

- 已完成统一 API 文档投递。
- 当前关键动作是把会议排起来。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-06 | 外部触达 | 发送统一 API 文档 | Origin 表达进入 kick-off 排期意向 |
| 2026-03-12 | 会议/排期 | 跟进三方 kick-off 进展 | 仍待对方确认时间窗口 |


#### 链接

- **平台链接**: [https://www.originenergy.com.au/solar/battery-plans/lite/#tinverter](https://www.originenergy.com.au/solar/battery-plans/lite/#tinverter) (有效)

- **需求文档**: 无

#### 标签

<span class="tag">重点推进</span>
<span class="tag">Growatt 主线</span>

</div>
<div class="card">

### Globird

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-globird</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>Retailer / VPP</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 80 / 100（高匹配）
- **匹配判断**: 平台价值和可推进性都不错，缺点是 Growatt 仍未明确进入，且测试环境和样本池准备成本较高。
- **Growatt 定位**: 可推进但需准备测试资源

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | compatible |
| SolaX | compatible |
| Goodwe | unknown |
| Alpha | compatible |
| Growatt | unknown |


#### 推进状态

- **当前阶段**: 沟通中
- **当前阶段说明**: 等待测试环境和接入样本准备
- **下一步动作**: 准备 100 个客户接入 poll 和测试环境。
- **下一任务**: 组织 100 个客户接入样本并搭建测试环境
- **任务 Owner**: Growatt 产品 + 测试
- **成功标准**: 测试环境 ready，样本池满足接入条件

#### Competitor Highlights

- Sigen / Sungrow / SolaX / Alpha 已兼容
- Growatt 尚未形成公开兼容

#### 备注

- 需要准备 100 个客户接入 poll。
- 测试环境准备是当前关键依赖。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-06 | 外部触达 | 发送统一 API 文档 | 进入测试资源准备阶段 |
| 2026-03-12 | 测试推进 | 复核 Globird 接入前置条件 | 确认需要 100 个客户样本和测试环境 |


#### 链接

- **平台链接**: [https://www.globirdenergy.com.au/join-vpp/](https://www.globirdenergy.com.au/join-vpp/) (有效)

- **需求文档**: 无

#### 标签

<span class="tag">Growatt 主线</span>
<span class="tag">资源依赖</span>

</div>
<div class="card">

### ShineHub

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-shinehub</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>渠道 / 聚合信息</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 58 / 100（中匹配）
- **匹配判断**: ShineHub 更偏商务渠道入口，不是典型 VPP 主平台。对 Growatt 的价值更多在商业导入而非技术卡位。
- **Growatt 定位**: 商业机会评估中

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | unknown |
| SolaX | unknown |
| Goodwe | unknown |
| Alpha | unknown |
| Growatt | unknown |


#### 推进状态

- **当前阶段**: 报价阶段
- **当前阶段说明**: 报价评估阶段
- **下一步动作**: 评估报价 ROI，决定是否继续投入。
- **下一任务**: 评估报价投入产出并确认是否进入采购/商务谈判
- **任务 Owner**: Growatt 商务
- **成功标准**: 形成 go / no-go 结论

#### Competitor Highlights

- Sigen Energy 已具备合作信息
- 当前更偏报价和商务判断



#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 商务推进 | 整理 ShineHub 报价方案 | 进入 ROI 评估 |

#### 商务信息

- **报价说明**: 5万澳币一个机型，超过四个机型，每4万澳币

#### 链接

- **平台链接**: [https://www.solarquotes.com.au/battery-storage/vpp-comparison/](https://www.solarquotes.com.au/battery-storage/vpp-comparison/) (有效)

- **需求文档**: 无

#### 标签

<span class="tag">商务评估</span>

</div>
<div class="card">

### AGL

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-agl</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>Retailer / VPP</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 69 / 100（中匹配）
- **匹配判断**: AGL 平台影响力不错，但当前 Growatt 信号不强，且公开证据不完整，更适合作为次级机会持续观察。
- **Growatt 定位**: 次级观察机会

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | compatible |
| SolaX | unknown |
| Goodwe | unknown |
| Alpha | compatible |
| Growatt | unknown |

**其他品牌**: Solaredge

#### 推进状态

- **当前阶段**: 沟通中
- **当前阶段说明**: 已约 2026-03-16 12:00-12:30 面对面交流
- **下一步动作**: 完成 2026-03-16 面对面交流并确认后续技术或商务推进路径。
- **下一任务**: 完成与 AGL 的 2026-03-16 12:00-12:30 面对面交流并确认下一步动作
- **任务 Owner**: Growatt BD + AGL
- **成功标准**: 完成面对面交流并拿到明确的后续对接方向

#### Competitor Highlights

- Sigen / Sungrow / Alpha 已兼容
- Growatt 尚无明确信号

#### 备注

- 平台链接仍为截断状态。
- AGL 已从公开清单观察进入直接沟通阶段。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 会议/排期 | AGL 回复并确认 2026-03-16 12:00-12:30 面对面交流 | 已从公开观察进入已约会议阶段 |


#### 链接

- **平台链接**: [https://www.agl.com.au/residential/solar-and-](https://www.agl.com.au/residential/solar-and-) (截图截断/待补全)

- **需求文档**: 无


</div>
<div class="card">

### Manta

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-manta</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>VPP / Platform</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-medium">中</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 76 / 100（高匹配）
- **匹配判断**: Manta 当前虽公开兼容信息少，但 Growatt 已进入沟通，且平台背景值得持续推进。
- **Growatt 定位**: 探索型在途机会

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | unknown |
| FOXESS | unknown |
| Sungrow | unknown |
| SolaX | unknown |
| Goodwe | compatible |
| Alpha | unknown |
| Growatt | discussing |


#### 推进状态

- **当前阶段**: 沟通中
- **当前阶段说明**: 等待下周会议确认真实接入路径
- **下一步动作**: 完成下周会议并确认接入路径。
- **下一任务**: 完成与 Manta 的下周会议并确认产品、接口和测试需求
- **任务 Owner**: Growatt BD + 产品
- **成功标准**: 拿到明确接入路径和责任人

#### Competitor Highlights

- 已知 Goodwe 兼容
- Growatt 已进入直接沟通状态

#### 备注

- 官网没有完整兼容清单。
- Manta 属于 OSW 旗下子公司。
- 已预约下周开会。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 会议/排期 | 确认与 Manta 下周会议安排 | Growatt 保持沟通中状态 |


#### 链接

- **平台链接**: 无

- **需求文档**: 无

#### 标签

<span class="tag">Growatt 主线</span>
<span class="tag">会议待执行</span>

</div>
<div class="card">

### Future X Power

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-future-x-power</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>合作生态</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-low">低</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 35 / 100（低匹配）
- **匹配判断**: 更偏生态关系映射，不是 Growatt 当前主线 VPP 平台。
- **Growatt 定位**: 生态观察项

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | unknown |
| SolaX | unknown |
| Goodwe | unknown |
| Alpha | unknown |
| Growatt | unknown |


#### 推进状态

- **当前阶段**: 生态合作
- **当前阶段说明**: 生态关系记录
- **下一步动作**: 仅在 Amber 主线需要时引用。
- **下一任务**: 保持生态关系备注，不单独投入推进
- **任务 Owner**: 内部产品运营
- **成功标准**: 作为 Amber 生态背景信息可引用

#### Competitor Highlights

- 与 Amber 存在合作关系

#### 备注

- 该第三方与 Amber 合作。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 阶段备注 | 记录 Future X Power 与 Amber 的生态关系 | 保留为背景信息 |


#### 链接

- **平台链接**: 无

- **需求文档**: 无

#### 标签

<span class="tag">生态背景</span>

</div>
<div class="card">

### Ecotricity

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>au-ecotricity</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>澳洲</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>区域合作</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-low">低</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: 28 / 100（低匹配）
- **匹配判断**: 偏区域关联线索，不构成 Growatt 当前澳洲主线推进对象。
- **Growatt 定位**: 低优先级背景信息

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | compatible |
| FOXESS | unknown |
| Sungrow | unknown |
| SolaX | unknown |
| Goodwe | unknown |
| Alpha | unknown |
| Growatt | unknown |


#### 推进状态

- **当前阶段**: 区域关联
- **当前阶段说明**: 区域关联备注
- **下一步动作**: 作为区域背景信息保留。
- **下一任务**: 继续保持关联记录，无需单独推进
- **任务 Owner**: 内部产品运营
- **成功标准**: 为区域分析提供背景

#### Competitor Highlights

- 与 Amber 存在区域运营关联说明

#### 备注

- 该第三方主要在新西兰运营，与 Amber 有关联说明。


#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
| 2026-03-12 | 阶段备注 | 记录 Ecotricity 区域关系信息 | 保留为区域背景线索 |


#### 链接

- **平台链接**: 无

- **需求文档**: 无

#### 标签

<span class="tag">区域背景</span>

</div>

---

## 维护说明

- 所有数据修改应先更新主数据 YAML。
- Dashboard 与文档应优先消费 `analysis`、`progress.current_phase`、`progress.next_task`、`progress.log_entries`。
- Growatt 为主线品牌，其他品牌用于 competitor analysis。