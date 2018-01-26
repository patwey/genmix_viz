import 'bootstrap/dist/css/bootstrap.min.css'

var React = require('react')
var ReactDOM = require('react-dom')

import GenerationChart from './generation-chart'

ReactDOM.render(
  <GenerationChart chartName='California ISO Generations' url='/caiso/yesterdays_mixes' />,
  document.getElementById('content')
)
