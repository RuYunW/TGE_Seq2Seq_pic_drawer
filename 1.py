from pyecharts.charts import Line
from pyecharts.faker import Faker
from pyecharts import options as opts


def line_connect_null() -> Line:
    y = Faker.values()
    y[3], y[5] = None, None
    c = (
        Line()
        .add_xaxis(["1", "2", "3", "4", "5", "6", "7", "8", "9", "9", "9", "9", "9", "9", "9", "9", ]  )
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Line-基本示例"))

    )
    return c

c = line_connect_null()
c.render('1.html')