# {{ dataset_name }}

> 区域：{{ region }}
> 最后更新：{{ last_updated }}
> 数据源：主数据 YAML
> 主线品牌：{{ brands.tracked_brands | selectattr("key", "equalto", dashboard.primary_brand) | map(attribute="display_name") | first }}
> 说明：本文档由 YAML 自动生成，请勿作为主数据直接维护。

<div class="card" markdown="1">

## 1. PM / PLM 总览

| 平台 | 优先级 | Growatt 状态 | 匹配度 | 当前阶段 | 当前阶段说明 | 下一任务 |
|---|---|---|---:|---|---|---|
{% for r in records %}
| {{ r.partner_name }} | {{ enums.priority_level[r.priority] }} | {{ r.compatibility.growatt | render_process_compatibility }} | {{ r.analysis.matching_score or 0 }} | {{ enums.integration_stage[r.progress.overall_stage] }} | {{ r.progress.current_phase or r.progress.summary or "-" }} | {{ r.progress.next_task.task or r.progress.next_action or "-" }} |
{% endfor %}

</div>

<div class="card" markdown="1">

## 2. Competitor Analysis

| 平台 | Growatt | Sigen Energy | FOXESS | Sungrow | SolaX | Goodwe | Alpha | 竞品亮点 |
|---|---|---|---|---|---|---|---|---|
{% for r in records %}
| {{ r.partner_name }} | {{ r.compatibility.growatt | render_process_compatibility }} | {{ r.compatibility.sigen_energy | render_compatibility }} | {{ r.compatibility.foxess | render_compatibility }} | {{ r.compatibility.sungrow | render_compatibility }} | {{ r.compatibility.solax | render_compatibility }} | {{ r.compatibility.goodwe | render_compatibility }} | {{ r.compatibility.alpha | render_compatibility }} | {{ r.analysis.competitor_highlights | join("；") }} |
{% endfor %}

</div>

## 3. 平台详情

{% for r in records %}
<div class="card" markdown="1">

### {{ r.partner_name }}

<div class="detail-grid">

<div class="detail-item">
<label>ID</label>
<p><code>{{ r.id }}</code></p>
</div>

<div class="detail-item">
<label>国家</label>
<p>{{ r.country }}</p>
</div>

<div class="detail-item">
<label>类别</label>
<p>{{ r.category }}</p>
</div>

<div class="detail-item">
<label>优先级</label>
<p><span class="priority priority-{{ r.priority }}">{{ enums.priority_level[r.priority] }}</span></p>
</div>

</div>

#### 决策摘要

- **匹配度**: {{ r.analysis.matching_score or 0 }} / 100（{{ enums.matching_band[r.analysis.matching_band] if r.analysis.matching_band else "-" }}）
- **匹配判断**: {{ r.analysis.matching_summary or "-" }}
- **Growatt 定位**: {{ r.analysis.growatt_position or "-" }}

#### 品牌兼容情况

| 品牌 | 状态 |
|---|---|
| Sigen Energy | {{ r.compatibility.sigen_energy | render_detail_compatibility }} |
| FOXESS | {{ r.compatibility.foxess | render_detail_compatibility }} |
| Sungrow | {{ r.compatibility.sungrow | render_detail_compatibility }} |
| SolaX | {{ r.compatibility.solax | render_detail_compatibility }} |
| Goodwe | {{ r.compatibility.goodwe | render_detail_compatibility }} |
| Alpha | {{ r.compatibility.alpha | render_detail_compatibility }} |
| Growatt | {{ r.compatibility.growatt | render_detail_process_compatibility }} |

{% if r.other_brands and r.other_brands | length > 0 %}
**其他品牌**: {{ r.other_brands | join("、") }}
{% endif %}

#### 推进状态

- **当前阶段**: {{ enums.integration_stage[r.progress.overall_stage] }}
- **当前阶段说明**: {{ r.progress.current_phase or r.progress.summary or "-" }}
- **下一步动作**: {{ r.progress.next_action or "-" }}
- **下一任务**: {{ r.progress.next_task.task if r.progress.next_task else "-" }}
- **任务 Owner**: {{ r.progress.next_task.owner if r.progress.next_task else (r.progress.owner or "-") }}
- **成功标准**: {{ r.progress.next_task.success_metric if r.progress.next_task else "-" }}

{% if r.analysis.competitor_highlights and r.analysis.competitor_highlights | length > 0 %}
#### Competitor Highlights

{% for item in r.analysis.competitor_highlights %}
- {{ item }}
{% endfor %}
{% endif %}

{% if r.progress.remarks and r.progress.remarks | length > 0 %}
#### 备注

{% for item in r.progress.remarks %}
- {{ item }}
{% endfor %}
{% endif %}

{% if r.progress.blockers and r.progress.blockers | length > 0 %}
#### 阻塞项

{% for item in r.progress.blockers %}
- {{ item }}
{% endfor %}
{% endif %}

{% if r.progress.log_entries and r.progress.log_entries | length > 0 %}
#### 全过程日志

| 日期 | 类型 | 事件 | 结果 |
|---|---|---|---|
{% for item in r.progress.log_entries %}
| {{ item.date or "-" }} | {{ enums.log_type[item.type] if item.type else "-" }} | {{ item.summary or "-" }} | {{ item.outcome or "-" }} |
{% endfor %}
{% endif %}

{% if r.commercial.pricing_note or r.commercial.business_note %}
#### 商务信息

{% if r.commercial.pricing_note %}
- **报价说明**: {{ r.commercial.pricing_note }}
{% endif %}
{% if r.commercial.business_note %}
- **商务备注**: {{ r.commercial.business_note }}
{% endif %}
{% endif %}

#### 链接

{% if r.links.platform_url.value %}
- **平台链接**: [{{ r.links.platform_url.value }}]({{ r.links.platform_url.value }}) ({{ enums.link_status[r.links.platform_url.status] }})
{% else %}
- **平台链接**: 无
{% endif %}

{% if r.links.requirement_doc_url.value %}
- **需求文档**: [{{ r.links.requirement_doc_url.value }}]({{ r.links.requirement_doc_url.value }}) ({{ enums.link_status[r.links.requirement_doc_url.status] }})
{% else %}
- **需求文档**: 无
{% endif %}

{% if r.tags and r.tags | length > 0 %}
#### 标签

{% for tag in r.tags %}
<span class="tag">{{ tag }}</span>
{% endfor %}
{% endif %}

</div>
{% endfor %}

---

## 维护说明

- 所有数据修改应先更新主数据 YAML。
- Dashboard 与文档应优先消费 `analysis`、`progress.current_phase`、`progress.next_task`、`progress.log_entries`。
- Growatt 为主线品牌，其他品牌用于 competitor analysis。
