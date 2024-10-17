from jinja2 import Environment, FileSystemLoader
import plotly.graph_objects as go
from plotly.io import to_html
import numpy as np
from pathlib import Path
import pyarrow as pa


base_constructs = ['Library', 'Language', 'Concepts']


class Plot:
    '''
    Plot class implements the generation of frequency distribution plots of the various components of the profiler report.
    Given a pyarrow table and a column name, it generates the corresponding plot.
    '''
    def __init__(self, table, column_name):
        self.table = table
        self.column_name = column_name
        self.column_data = self._get_column_data()

    def _get_column_data(self):
        column_data = self.table[self.column_name].to_numpy()
        split_data = []
        for value in column_data:
            if isinstance(value, str) and ',' in value:
                split_data.extend(value.split(','))
            else:
                split_data.append(value)
        return np.array([item.strip() if isinstance(item, str) else item for item in split_data])

    def generate_distribution_plot(self):
        data = self.column_data
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=data, nbinsx=len(np.unique(data)), opacity=0.7, marker=dict(color='blue', line=dict(width=1, color='black'))))
        fig.update_layout(
            width=500,  
            height=300,  
            title=dict(
                text=f'Distribution of {self.column_name}',
                font=dict(size=14)  
            ),
            xaxis=dict(
                title='Value',
                title_font=dict(size=12),  
                tickfont=dict(size=10)  
            ),
            yaxis=dict(
                title='Frequency',
                title_font=dict(size=12), 
                tickfont=dict(size=10) 
            ),
            bargap=0.1
        )
        return to_html(fig, full_html=False)


class Report:
    '''
    Generates the report containing the distribution of various syntactic and semantic components.
    '''
    def __init__(self, template_file: str):
        path = Path(template_file)
        directory = path.parent 
        file_name = path.name  
        self.env = Environment(loader=FileSystemLoader(directory))
        self.template = self.env.get_template(file_name)
        self.data = {}
        self.data['title'] = 'Profiler Report'
        self.data['heading'] = 'Syntactic and Semantic Profile'
        self.data['description'] = 'This report presents the detailed profiling report of the input dataset.'

    def add_metric(self, metric_id, name, graph_html=None):
        if 'metrics' not in self.data:
            self.data['metrics'] = []
        self.data['metrics'].append({
            'id': metric_id,
            'name': name,
            'graph_html': graph_html
        })

    def render(self):
        return self.template.render(self.data)

    def save(self, output_file):
        output = self.render()
        with open(output_file, 'w') as f:
            f.write(output)
        print(f"HTML file generated: {output_file}")



def generate_report(table: pa.Table, metrics_list):
    """
    Generates the profiler report given the table name and the metrics list given as input by the user.
    """
    columns = base_constructs + metrics_list
    script_dir = Path(__file__).parent.resolve()
    template_file = str(script_dir / 'template.html')
    output_file = str(script_dir / 'output.html')
    report = Report(template_file)
    count = 0
    for column in columns:
        plot = Plot(table, column)
        plot_html = plot.generate_distribution_plot()
        report.add_metric(count, column, plot_html)
        count+=1
    report.save(output_file)