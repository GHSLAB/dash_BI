import dash
from dash import dcc, html

import feffery_antd_components as fac
import feffery_antd_charts as fact
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style

from datetime import datetime
import random

app = dash.Dash(__name__)


def tab_filter_style():
    """创建带边框的样式"""
    return style(
        height=80,
        # border="1px solid #000",
        borderRadius=5,
        boxShadow="0 0 5px rgba(0, 0, 0, 0.5)",
        padding=10,
        # margin=5,
        width="100%",
    )


def tab1():
    return [
        fac.AntdRow(  # 选择行
            [
                fac.AntdCol(
                    fac.AntdSpace(
                        [
                            fac.AntdText("仓库"),
                            fac.AntdSelect(
                                options=[f"选项{i}" for i in range(1, 6)],
                                mode="tags",
                                style={"width": "100%"},
                            ),
                        ],
                        direction="vertical",
                        style=tab_filter_style(),
                    ),
                    span=6,
                ),
                fac.AntdCol(
                    fac.AntdSpace(
                        [
                            fac.AntdText("订单签署日期"),
                            fac.AntdSelect(
                                options=[f"选项{i}" for i in range(1, 6)],
                                mode="tags",
                                style={"width": "100%"},
                            ),
                        ],
                        direction="vertical",
                        style=tab_filter_style(),
                    ),
                    span=6,
                ),
                fac.AntdCol(
                    fac.AntdSpace(
                        [
                            fac.AntdText("供应商"),
                            fac.AntdSelect(
                                options=[f"选项{i}" for i in range(1, 6)],
                                mode="tags",
                                style={"width": "100%"},
                            ),
                        ],
                        direction="vertical",
                        style=tab_filter_style(),
                    ),
                    span=6,
                ),
                fac.AntdCol(
                    fac.AntdSpace(
                        [
                            fac.AntdText("审批结果", style=style(fontWeight="bold")),
                            # fac.AntdSelect(
                            #     options=[f"选项{i}" for i in range(1, 6)],
                            #     mode="tags",
                            #     style={"width": "100%"},
                            # ),
                            fac.AntdFlex(
                                [
                                    fac.AntdButton(
                                        "通过",
                                        type="primary",
                                        style=style(width="calc((100% - 5px)/2)"),
                                    ),
                                    fac.AntdButton(
                                        "不通过",
                                        style=style(width="calc((100% - 5px)/2)"),
                                    ),
                                ],
                                justify="space-between",
                                style={"width": "100%"},
                            ),
                        ],
                        direction="vertical",
                        style=tab_filter_style(),
                    ),
                    span=6,
                ),
            ],
            gutter=10,
            style=style(padding=5),
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdRow(
                            fac.AntdCenter(
                                "采购总金额",
                                style={
                                    "height": "100%",
                                    "width": "100%",
                                },
                            ),
                            style=style(height=40),
                        ),
                        fac.AntdRow(
                            fac.AntdFlex(
                                fac.AntdStatistic(
                                    value=fuc.FefferyCountUp(
                                        end=11289300,
                                        duration=1,
                                        decimals=2,
                                        style=style(fontSize=52, color="#7F45EC"),
                                    )
                                ),
                                justify="center",
                                align="center",
                                style={
                                    "height": "100%",
                                    "width": "100%",
                                },
                            ),
                            style=style(height="calc(100% - 40px)"),
                        ),
                    ],
                    span=6,
                    style=style(backgroundColor="#FFFFFF"),
                ),
                fac.AntdCol(
                    [
                        # fac.AntdRow(
                        #     [],
                        #     style=style(
                        #         backgroundColor="#1677ffbf",
                        #         color="white",
                        #         height="calc((100% - 10px)/2)",
                        #     ),
                        # ),
                        # fac.AntdRow(
                        #     style=style(
                        #         backgroundColor="#1677ffbf",
                        #         color="white",
                        #         height="calc((100% - 10px)/2)",
                        #         marginTop="10px",
                        #     )
                        # ),
                        html.Div(
                            [
                                fac.AntdCenter(
                                    "供应商数量", style=style(height=40, width="100%")
                                ),
                                html.Div(
                                    fac.AntdFlex(
                                        fac.AntdStatistic(
                                            value=fuc.FefferyCountUp(
                                                end=3,
                                                duration=1,
                                                style=style(
                                                    fontSize=36, color="#7F45EC"
                                                ),
                                            )
                                        ),
                                        justify="center",
                                        align="center",
                                        style={
                                            "height": "100%",
                                            "width": "100%",
                                        },
                                    ),
                                    style=style(height="calc(100% - 40px)"),
                                ),
                            ],
                            style=style(
                                backgroundColor="white",
                                height="calc((100% - 10px)/2)",
                            ),
                        ),
                        html.Div(
                            [
                                fac.AntdCenter(
                                    "采购订单签订数量",
                                    style=style(height=40, width="100%"),
                                ),
                                html.Div(
                                    fac.AntdFlex(
                                        fac.AntdStatistic(
                                            value=fuc.FefferyCountUp(
                                                end=20,
                                                duration=1,
                                                style=style(
                                                    fontSize=36, color="#7F45EC"
                                                ),
                                            )
                                        ),
                                        justify="center",
                                        align="center",
                                        style={
                                            "height": "100%",
                                            "width": "100%",
                                        },
                                    ),
                                    style=style(height="calc(100% - 40px)"),
                                ),
                            ],
                            style=style(
                                backgroundColor="white",
                                height="calc((100% - 10px)/2)",
                                marginTop="10px",
                            ),
                        ),
                    ],
                    span=4,
                ),
                fac.AntdCol(
                    [
                        fac.AntdRow(
                            fac.AntdText(
                                "采购金额趋势",
                                style={
                                    "height": "100%",
                                    "width": "100%",
                                },
                            ),
                            style=style(height=40, padding=10),
                        ),
                        fac.AntdRow(
                            [
                                fact.AntdArea(
                                    data=[
                                        {
                                            "date": f"2020-0{i}",
                                            "y": random.randint(50, 40000),
                                        }
                                        for i in range(1, 10)
                                    ],
                                    xField="date",
                                    yField="y",
                                    smooth=True,
                                    areaStyle={
                                        "fill": "l(270) 0:#ffffff 0.5:#7ec2f3 1:#1890ff"
                                    },
                                    point={"shape": "circle", "style": {"r": 8}},
                                    # width="100%",
                                    style={"height": "100%", "width": "100%"},
                                )
                            ],
                            style=style(height="calc(100% - 40px)", padding=10),
                        ),
                    ],
                    span=14,
                    style=style(backgroundColor="#FFFFFF"),
                ),
            ],
            gutter=20,
            style=style(padding=5, height=320),
        ),
        fac.AntdSpace(  # 表格行
            [
                fac.AntdText("采购订单明细"),
                fac.AntdTable(
                    columns=[{"title": col, "dataIndex": col} for col in col_list]
                    + [
                        {"group": "采购产品明细", "title": good, "dataIndex": good}
                        for good in goods_list
                    ],
                    data=[
                        {
                            "供应商": f"供应商{i}",
                            "采购订单名称": f"采购订单名称{i}",
                            "仓库": f"仓库{i}",
                            "采购订单金额/元": f"采购订单金额/元{i}",
                            "采购负责人": f"采购负责人{i}",
                            "订单签订日期": f"订单签订日期{i}",
                            "订单交付日期": f"订单交付日期{i}",
                            "审批结果": f"审批结果{i}",
                            "产品名称": f"产品名称{i}",
                            "产品编码": f"产品编码{i}",
                            "采购数量": f"采购数量{i}",
                            "采购单价/元": f"采购单价/元{i}",
                            "产品采购总价/元": f"产品采购总价/元{i}",
                            "到货批次": f"到货批次{i}",
                        }
                        for i in range(1, 5)
                    ]
                    * 3,
                    conditionalStyleFuncs={  #
                        col: """
(record, index) => {
    if ( index % 2 === 1 ) {
        return { style: { backgroundColor: "#F1EEF9" } }
    }
}
"""
                        for col in col_list + goods_list
                    },
                    pagination={"pageSize": 10},
                ),
            ],
            direction="vertical",
            style=style(
                width="100%",
                background="#FFFFFF",
                padding=10,
                marginTop=10,
                boxShadow="0 2px 8px rgba(0, 0, 0, 0.15)"
            ),
        ),
    ]


col_list = [
    "供应商",
    "采购订单名称",
    "仓库",
    "采购订单金额/元",
    "采购负责人",
    "订单签订日期",
    "订单交付日期",
    "审批结果",
]

goods_list = [
    "产品名称",
    "产品编码",
    "采购数量",
    "采购单价/元",
    "产品采购总价/元",
    "到货批次",
]


def tab2():
    return fac.AntdCenter(
        "这是标签页2的内容示例",
        style={
            "fontSize": 18,
            "background": "rgba(28, 126, 214, calc(1 - 0.2))",
            "height": 200,
        },
    )


app.layout = fac.AntdLayout(
    [
        fac.AntdHeader(
            fac.AntdTitle(
                "WarehouseBI", level=2, style={"color": "white", "margin": "0"}
            ),
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                # "backgroundColor": "#1890ff",
            },
        ),
        fac.AntdLayout(
            [
                fac.AntdLayout(
                    [
                        fac.AntdContent(
                            [
                                fac.AntdTabs(
                                    items=[
                                        {
                                            "key": "tab1",
                                            "label": "采购订单统计",
                                            "children": tab1(),
                                        },
                                        {
                                            "key": "tab2",
                                            "label": "采购订单-入库-退货执行跟踪",
                                            "children": tab2(),
                                        },
                                    ]
                                )
                            ],
                            style=style(padding=10),
                        ),
                    ]
                ),
            ],
            style=style(height="100%", background="#F4F6F9"),
        ),
    ],
    style=style(width="100%", height="100vh"),
)


if __name__ == "__main__":
    app.run(debug=True)
