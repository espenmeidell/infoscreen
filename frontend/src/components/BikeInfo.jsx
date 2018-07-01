import React, { Component } from "react"
import PropTypes from "prop-types"
import { titleStyle, matIcon, centered } from "../globals"

class BikeInfo extends Component {
  state = {
    isLoading: true,
    stationName: "",
    count: 0,
  }

  async loadData() {
    console.log("Loading data")
  }

  componentDidMount() {
    this.loadData()
  }

  getComponent = () => {
    switch (this.state.isLoading) {
      case true:
        return (
          <div style={centered}>
            <div className="lds-ripple">
              <div />
              <div />
            </div>
          </div>
        )

      default:
        return (
          <div style={style}>
            <div style={titleStyle}>
              <i style={matIcon} className="material-icons">
                directions_bike
              </i>
              {this.state.stationName}
            </div>
            <div> {this.state.count} sykler igjen</div>
          </div>
        )
    }
  }

  render() {
    return this.getComponent()
  }
}

BikeInfo.propTypes = {
  stationId: PropTypes.string.isRequired,
}

const style = {
  display: "flex",
  flexDirection: "column",
}

export default BikeInfo
