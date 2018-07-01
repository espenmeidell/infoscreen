import React from "react"
import PropTypes from "prop-types"
import { colors } from "../globals"

const Card = ({ color, children }) => {
  return <div style={{ ...style, backgroundColor: color }}>{children}</div>
}

const style = {
  padding: "2em",
  width: "300px",
  color: colors.foreground,
}

Card.propTypes = {
  children: PropTypes.element.isRequired,
  color: PropTypes.string.isRequired,
}

export default Card
