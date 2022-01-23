from itertools import count
import plotly.express as px
import numpy as np
df = px.data.iris()


fig1 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                  marginal_x="box", marginal_y="violin", trendline="ols")


df = df.sort_values(by="sepal_width")
fig2 = px.line(df, x="sepal_width", y="sepal_length", color="species")


fig3 = px.scatter_matrix(df, dimensions=[
                         'sepal_length',
                         'sepal_width',
                         'petal_length',
                         'petal_width'
                         ],
                         color="species")


df4 = px.data.iris()
fig4 = px.parallel_coordinates(df4, color="species_id", labels={
    "sepal_length": "Sepal Length",
    "sepal_width": "Sepal Width",
    "petal_length": "Petal Length",
    "petal_width": "Petal Width",
},
    color_continuous_scale=px.colors.diverging.Fall,
    color_continuous_midpoint=2
)

df5 = px.data.tips()
fig5 = px.parallel_categories(df5, color="size")

df6 = px.data.gapminder()
fig6 = px.scatter(df6, x="gdpPercap", y="lifeExp",
                  animation_frame="year", animation_group="country",
                  range_x=[100, 80000], range_y=[25, 90],
                  color="continent", size="pop", hover_name="country",
                  log_x=True, size_max=100)


df7 = px.data.gapminder()
fig7 = px.line(df7, x="year", y="lifeExp",
               color="continent",
               line_group="country",
               hover_name="country",
               line_shape="spline",
               render_mode="svg")

fig7_2 = px.area(df7, x="year", y="pop",
                 color="continent",
                 line_group="country",
                 hover_name="country",
                 line_shape="spline",
                 )
df8 = px.data.gapminder().query("year==2007").query("continent=='Europe'")
df8.loc[df8["pop"] < 4_000_000, 'country'] = "Other"
fig8 = px.pie(df8,
              values='pop',
              names='country',
              title="Population in Europa",
              )

df9 = px.data.gapminder().query("year==2007")
print(df9.query("country=='Germany'").query("year==2007"))
double_row = {'country': 'Germany',
              'continent': 'Europe',
              'year': 2007,
              'lifeExp': 40.,
              'pop': 80000000,
              'gdpPercap': 32170.37442,
              'iso_alpha': 'DEU',
              'iso_num': 276}

# print(df9.columns, df9.dtypes)
# df9 = df9.append(double_row, ignore_index=True)
# print("")
# print(df9.query("country=='Germany'").query("year==2007"))

fig9 = px.sunburst(df9,
                   path=['continent', 'country'],
                   values='pop',
                   title="Population in the World",
                   color="lifeExp",
                   )

df10 = px.data.tips()
fig10 = px.histogram(df10, x='total_bill', nbins=10, y="tip", color="sex")
# space between every "Balken"
fig10.update_layout(bargap=0.1)

# wenn counts verwendet werden will, wird numpy as histogramm verwendet
counts, bins = np.histogram(df10.total_bill, bins=range(0, 60, 5))
bins = bins[:-1] + bins[1:]
fig11 = px.bar(x=bins, y=counts)

# oder normalisiertes histogramm: histnorm='percent',
# histnorm='probability density' -> zusammenaddiert = 1 -> kein nbins angeben
df12 = px.data.tips()
fig12 = px.histogram(df12, x='total_bill', nbins=10,
                     y="tip", color="sex", histnorm='percent')
# histfunc bildet average, pattern_shape für zweite color
fig12 = px.histogram(df12, x='total_bill', y="tip",
                     color="sex", pattern_shape="smoker", histfunc="avg")
# space between every "Balken"
fig12.update_layout(bargap=0.1)

# visualize all different templates
for t in ['plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn', 'simple_white', 'none']:
    fig12.update_layout(template=t)
    fig12.show()

# fig7.write_html("country_lifeExp.html")
fig12.show()
