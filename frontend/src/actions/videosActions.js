import * as types from './actionTypes';

function url(str) {
  if(str === ""){
    return 'http://localhost:3004';
  } else {
    return 'http://localhost:3004' + str;
  }
}

export function receiveVideos(json) {
  console.log("******* receiveVideos: ", json)
  return {
    type: types.RECEIVE_VIDEOS
    ,videos: json
  };
}

export function fetchVideos() {
  return dispatch => {
    return fetch(url('/videos'), {
      method: 'GET',
      headers: {
        'x-api-key': "1000000",
        'Accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(json => dispatch(receiveVideos(json)));
  };
}
