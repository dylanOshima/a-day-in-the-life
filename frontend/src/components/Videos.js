import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import * as videosActions from '../actions/videosActions';
import PropTypes from 'prop-types';
import React from 'react';

class Videos extends React.Component {

  renderVideos(){
    return <div>{this.props.videos}</div>
  }


  render() {
    return (
      <div className="Videos">
        { this.props.videos.length > 0?
          this.renderVideos()
          :
          <div className="error-message">
            Sorry, no data...
          </div>
        }
      </div>

    )
  }
}

Videos.propTypes = {
  videosActions: PropTypes.object,
  videos: PropTypes.array
};

function mapStateToProps(state) {
  return {
    videos: state.videos
  };
}

function mapDispatchToProps(dispatch) {
  return {
    videosActions: bindActionCreators(videosActions, dispatch)
  };
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Videos);
