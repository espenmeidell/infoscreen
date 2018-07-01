import React, { Component } from "react"
import PropTypes from "prop-types"
import { titleStyle, matIcon } from "../globals"

class BikeInfo extends Component {
  render() {
    return (
      <div style={style}>
        <div style={titleStyle}>
          <i style={matIcon} className="material-icons">
            directions_bike
          </i>
          {this.props.title}
        </div>
        <div> {this.props.count} sykler igjen</div>
      </div>
    )
  }
}

BikeInfo.propTypes = {
  title: PropTypes.string.isRequired,
  count: PropTypes.number.isRequired,
}

const style = {
  display: "flex",
  flexDirection: "column",
}

export default BikeInfo
