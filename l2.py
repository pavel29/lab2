from spyre import server

import pandas as pd
import matplotlib.pyplot as plt

class StockExample(server.App):
  title = "Inputs"

  inputs = [{   "type":'dropdown',
                "label": 'Index  ',
                "options" : [ {"label": "VCI", "value":"VCI"},
                                {"label": "TCI", "value":"TCI"},
                                {"label": "VHI", "value":"VHI"},],
                "key": 'index',
                "action_id": "update_data"},

              { "type":'dropdown',
                "label": 'Region',
                "options" : [ {"label": "Vinnitsya", "value":"01"},
                                  {"label": "Volyn", "value":"02"},
                                  {"label": "Dnipropetrovsk", "value":"03"},
                                  {"label": "Donetsk", "value":"04"},
                                  {"label": "Zhytomyr", "value":"05"},
                                  {"label": "Transcarpathia", "value":"06"},
                                  {"label": "Zaporizhzhya", "value":"07"},
                                  {"label": "Ivano-Frankivsk", "value":"08"},
                                  {"label": "Kiev", "value":"09"},
                                  {"label": "Kirovohrad", "value":"10"},
                                  {"label": "Luhansk", "value":"11"},
                                  {"label": "Lviv", "value":"12"},
                                  {"label": "Mykolayiv", "value":"13"},
                                  {"label": "Odessa", "value":"14"},
                                  {"label": "Poltava", "value":"15"},
                                  {"label": "Rivne", "value":"16"},
                                  {"label": "Sumy", "value":"17"},
                                  {"label": "Ternopil", "value":"18"},
                                  {"label": "Kharkiv", "value":"19"},
                                  {"label": "Kherson", "value":"20"},
                                  {"label": "Khmelnytskyy", "value":"21"},
                                  {"label": "Cherkasy", "value":"22"},
                                  {"label": "Chernivtsi", "value":"23"},
                                  {"label": "Chernihiv", "value":"24"},
                                  {"label": "Crimea", "value":"25"},
                                  {"label": "Kiev City", "value":"26"},
                                  {"label": "Sevastopol", "value":"27"}],
                "key": 'region',
                "action_id": "update_data"},

              { "input_type":"text",
                "variable_name":"year",
                "label": "Year",
                "value":1981,
                "key": 'year',
                "action_id":"update_data"},

              { "type":'slider',
                "label": 'First week',
                "min" : 1,"max" : 52,"value" : 35,
                "key": 'first',
                "action_id": 'update_data'},

              { "type":'slider',
                "label": 'Last week',
                "min" : 1,"max" : 52,"value" : 35,
                "key": 'last',
                "action_id": 'update_data'}]

  controls = [{   "type" : "hidden",
                  "id" : "update_data"}]

  tabs = ["Plot", "Table"]

  outputs = [{  "type" : "plot",
                "id" : "plot",
                "control_id" : "update_data",
                "tab" : "Plot"},
              { "type" : "table",
                "id" : "table",
                "control_id" : "update_data",
                "tab" : "Table"}]

  def table(self, params):
    index = params['index']
    region = params['region']
    year = params['year']
    first = params['first']
    last = params['last']

    path = 'id_{}.csv'.format(region)

    df = pd.read_csv(path, index_col=False, header=9,
                     names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI', 'VHI<15', 'VHI<35'])
    df1 = df[(df['year'] == int(year)) & (df['week'] >= int(first)) & (df['week'] <= int(last))]
    df1 = df1[['week', index]]
    return df1

  def getPlot(self, params):
    index = params['index']
    year = params['year']
    first = params['first']
    last = params['last']
    df = self.table(params).set_index('week')
    plt_obj = df.plot()
    plt_obj.set_ylabel(index)
    plt_obj.set_title('Index {index} for {year} from {first} to {last} weeks'.format(index=index,
      year=int(year), first=int(first), last=int(last)))
    fig = plt_obj.get_figure()
    return fig

app = StockExample()
app.launch()