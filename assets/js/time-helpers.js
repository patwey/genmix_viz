var moment = require('moment')

export default class TimeHelpers {
  static toMilliseconds(seconds) {
    return seconds * 1000
  }

  static monthAndDate(milliseconds) {
    return moment(milliseconds).format('MMMM Do')
  }

  static hourAndMinutes(milliseconds) {
    return moment(milliseconds).format('h:mm a')
  }

  static hourAndPeriod(milliseconds) {
    return moment(milliseconds).format('h a')
  }
}
