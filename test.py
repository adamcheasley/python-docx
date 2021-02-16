from docx import Document
from pptx.chart.data import CategoryChartData
from pptx.util import Pt, Inches
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_DATA_LABEL_POSITION


print 'Generating document...'
document = Document()
document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

chart_data = CategoryChartData()
chart_data.categories = ['East', 'West', 'Midwest']
chart_data.add_series('Series 1', (19.2, 21.4, 16.7))
x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(4.5)
chart = document.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, x, y, cx, cy, chart_data)

chart.has_legend = True
chart.legend.position = XL_LEGEND_POSITION.BOTTOM
chart.legend.include_in_layout = False

plot = chart.plots[0]
plot.has_data_labels = True
data_labels = plot.data_labels
data_labels.font.size = Pt(13)
data_labels.position = XL_DATA_LABEL_POSITION.OUTSIDE_END

chart.has_title = True
chart_title = chart.chart_title
text_frame = chart_title.text_frame
text_frame.text = 'Title'
paragraphs = text_frame.paragraphs
paragraph = paragraphs[0]
paragraph.font.size = Pt(18)

category_axis = chart.category_axis
category_axis.tick_labels.font.size = Pt(14)

document.save('demo.docx')
print 'Done'
