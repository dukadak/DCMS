var data = [{
    values: [16, 15, 12, 6, 5, 4, 42],
    labels: ['HP', 'Lenovo', 'DELL', 'Huawei', 'Inspur', 'ESLIM', 'DS&G' ],
    domain: {
      x: [0, .48]
    },
    hoverinfo: 'label+percent',
    hole: .4,
    type: 'pie'
  }];
  
  var layout = {
    annotations: [
      {
        font: {
          size: 20
        },
        showarrow: false,
        text: '',
        x: 0.17,
        y: 0.5
      }
    ],
    height: 400,
    width: 600
  };
  
  Plotly.newPlot('vendor-chart-div', data, layout);