import PropTypes from 'prop-types';
import React from 'react';

import '../styles/Nav.css';
import home from '../static/home.svg';

class Nav extends React.Component {
  render() {
    return (
      <header className="Nav">
        <div className="nav-container">
          <img className="nav-home" src={home} alt="home image"></img>
          <h1>
            A Day in the Life of...
          </h1>
        </div>
      </header>

    )
  }
}

export default Nav;
