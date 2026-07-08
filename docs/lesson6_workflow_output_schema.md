# TACO 第6课：言论分类器输出格式

最终输出必须包含三个字段：

hardness：整数，范围 1-10
domain：字符串，只能是 tariff / tech / energy / fx / other
reasoning：中文评分理由

示例输出：

{
"hardness": 8,
"domain": "tariff",
"reasoning": "这句话包含明确关税威胁和具体时间，因此强硬度较高。"
}

说明：

* hardness 不是概率，而是强硬程度。
* domain 是政策领域，不是情绪。
* reasoning 必须简短清楚。
* 输出格式稳定，是后续 S07 概率引擎的输入基础。
