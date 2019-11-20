from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts


def line_code_length_acc() -> Line:
    y = [1,2,2,3,5]

    c = (
        Line()
        .add_xaxis(["50", "100", "150", "200", "200+"])
        .add_yaxis("method1",
                   [2, 2, 3, 3, 5],
                   )
        .add_yaxis("method2",
                   [4, 6, 7, 2, 5],
                   )
        .add_yaxis("method3",
                   [4, 5, 2, 1, 4],
                   )
        .add_yaxis("method4",
                   [1, 6, 6, 3, 1],
                   )
        .add_yaxis("method5",
                   [1, 5, 4, 2, 6])

        .set_series_opts(
            label_opts = opts.LabelOpts(is_show=False),
            LabelOpts = opts.LabelOpts(is_show=False),
            LineStyleOpts = opts.LineStyleOpts(width=1)
        )

        .set_global_opts(title_opts=opts.TitleOpts(title="line_code_length_acc"),
                         legend_opts=opts.LegendOpts(pos_left='12%',
                                                     orient='vertical',
                                                     pos_top='11%'),
                         )

    )
    return c


def line_code_length_BLEU() -> Line:
    y = Faker.values()
    y[3], y[5] = None, None
    c = (
        Line()
            .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8", "9", "9", "9", "9", "9", "9", "9", "9",]  )
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))

    )
    return c




code_length_acc = line_code_length_acc()
# code_length_BLEU = line_code_length_BLEU()


code_length_acc.render('code_length_acc.html')
# code_length_BLEU.render('code_length_BLEU.html')
