import React, { Component } from "react"
import Card from "./components/Card"
import BikeInfo from "./components/BikeInfo"
import { colors } from "./globals"

class App extends Component {
  render() {
    return (
      <div style={style}>
        <Card color={colors.blue}>
          <BikeInfo stationId="264" />
        </Card>
      </div>
    )
  }
}

const style = {
  display: "flex",
  justifyContent: "space-around",
  margin: "2em",
}

export default App
