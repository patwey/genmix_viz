import 'bootstrap/dist/css/bootstrap.min.css'

var React = require('react')
var ReactDOM = require('react-dom')
var Recharts = require('recharts')
var moment = require('moment')

const { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } = Recharts;

class Chart extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  getGenerations() {
    fetch(this.props.url)
    .then((response) => response.json())
    .then((data) => {
      this.setState({ data: data['generation_mixes'] })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  componentDidMount() {
    this.getGenerations();
  }

  render() {
    if (this.state.data.length > 0) {
      var keys = Object.keys(this.state.data[0]).filter((k) => { return k != 'timestamp' })
    } else {
      var keys = []
    }

    if (this.state.data.length > 0) {
      var lastUpdated = 'Last updated: ' + this.props.moment(this.state.data[this.state.data.length - 1].timestamp * 1000).format('MMM Do, h:mm a')
    } else {
      var lastUpdated = null
    }

    var colors = [
      '#133C55',
      '#386FA4',
      '#59A5D8',
      '#84D2F6',
      '#91E5F6'
    ]
    var colorsLength = colors.length

    var ticks = this.state.data.map((d) => { return d.timestamp })
    var domain = [ticks[0], ticks[ticks.length - 1]]

    return (
      <div className="container" style={{paddingTop: '20px'}}>
        <h1>CAISO</h1>
        <p>{lastUpdated}</p>

        <LineChart width={1000} height={500} data={this.state.data} margin={{top: 5, right: 30, left: 20, bottom: 5}}>
         <XAxis dataKey="timestamp"
                tickFormatter={(tick) => { return this.props.moment(tick * 1000).format('h a') } }
                domain={domain}
                ticks={ticks}
                type="number" />
         <YAxis />
         <CartesianGrid strokeDasharray="3 3"/>
         <Tooltip labelFormatter={(text) => {
           return (
             <span className="recharts-tooltip-item-list">
               <span className="reacharts-tooltip-item" style={{display: 'block', paddingTop: '4px', paddingBottom: '4px'}}>
                 <strong className="recharts-tooltip-item-name">{this.props.moment(text * 1000).format('MMMM Do')}</strong>
               </span>
               <span className="reacharts-tooltip-item" style={{display: 'block', paddingTop: '4px', paddingBottom: '4px'}}>
                 <span className="recharts-tooltip-item-value">{this.props.moment(text * 1000).format('h:mm a')}</span>
               </span>
             </span>
           )
         } }
         />
         <Legend />
         {
           keys.map((k, idx) => {
              return (
                <Line type="monotone"
                      key={k}
                      dataKey={k}
                      stroke={colors[idx % colorsLength]}
                      connectNulls={true}
                      activeDot={{r: 6}} />
              )
           })
         }
        </LineChart>
      </div>
    );
  }
}

ReactDOM.render(<Chart url='/caiso/yesterdays_mixes' moment={moment}/>, document.getElementById('content'))
