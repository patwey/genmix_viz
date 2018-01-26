var React = require('react')
var Recharts = require('recharts')

const { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } = Recharts

import TimeHelpers from './time-helpers'

export default class GenerationChart extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      data: [],
    }
    this.colors = [
      '#133C55',
      '#386FA4',
      '#59A5D8',
      '#84D2F6',
      '#91E5F6'
    ]
    this.colorsLength = this.colors.length
  }

  getGenerations() {
    fetch(this.props.url)
    .then((response) => response.json())
    .then((data) => {
      var data = this.convertTimestampsToMilliseconds(data['generation_mixes'])
      this.setState({ data: data })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  componentDidMount() {
    this.getGenerations()
  }

  convertTimestampsToMilliseconds(data) {
    return (
      data.map((d) => {
        d.timestamp = TimeHelpers.toMilliseconds(d.timestamp)
        return d
      })
    )
  }

  domain() {
    return [this.ticks()[0], this.ticks[this.ticks().length - 1]]
  }

  ticks() {
    return this.state.data.map((d) => { return d.timestamp })
  }

  lineKeys() {
    if (this.state.data.length > 0) {
      var dataPoint = this.state.data[0]
      return Object.keys(dataPoint).filter((k) => { return k != 'timestamp' })
    } else {
      return []
    }
  }

  renderHeader() {
    return (
      <div>
        <h1>{this.props.chartName}</h1>
        <p>{this.renderLastUpdated()}</p>
      </div>
    )
  }

  renderLastUpdated() {
    if (this.state.data.length > 0) {
      var lastTs = this.state.data[this.state.data.length - 1].timestamp
      return (
        <em>
          Last updated: {TimeHelpers.monthAndDate(lastTs)} {TimeHelpers.hourAndMinutes(lastTs)}
        </em>
      )
    } else {
      return null
    }
  }

  renderLabel(timestamp) {
    return (
      <span className="recharts-tooltip-item-list">
        <span
          className="reacharts-tooltip-item"
          style={{display: 'block', paddingTop: '4px', paddingBottom: '4px'}}
        >
          <strong className="recharts-tooltip-item-name">
            {TimeHelpers.monthAndDate(timestamp)}
          </strong>
        </span>
        <span
          className="reacharts-tooltip-item"
          style={{display: 'block', paddingTop: '4px', paddingBottom: '4px'}}
        >
          <span className="recharts-tooltip-item-value">
            {TimeHelpers.hourAndMinutes(timestamp)}
          </span>
        </span>
      </span>
    )
  }

  renderLine(key, n) {
    var color = this.colors[n % this.colorsLength]
    return (
      <Line
        type="monotone"
        key={key}
        dataKey={key}
        stroke={color}
        connectNulls={true}
        activeDot={{r: 6}}
      />
    )
  }

  render() {
    return (
      <div className="container" style={{paddingTop: '20px'}}>
        {this.renderHeader()}

        <LineChart
          width={1000}
          height={500}
          data={this.state.data}
          margin={{top: 5, right: 30, left: 20, bottom: 5}}
        >
          <XAxis
            dataKey="timestamp"
            tickFormatter={TimeHelpers.hourAndPeriod}
            domain={this.domain()}
            ticks={this.ticks()}
            type="number"
          />
          <YAxis />
          <CartesianGrid strokeDasharray="3 3"/>
          <Tooltip labelFormatter={this.renderLabel.bind(this)} />
          <Legend />
          { this.lineKeys().map(this.renderLine.bind(this)) }
        </LineChart>
      </div>
    )
  }
}
