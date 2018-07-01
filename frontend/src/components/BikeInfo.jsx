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
    const ctx = await fetch(
      "https://l6k9n76oz1.execute-api.eu-central-1.amazonaws.com/api/bikes/" +
        this.props.stationId,
    )
    const json = await ctx.json()
    this.setState({
      isLoading: false,
      stationName: json.name,
      count: json.availableBikes,
    })
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
