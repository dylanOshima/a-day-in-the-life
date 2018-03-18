import * as types from './actionTypes';

function url() {
  return 'www.url.com';
}

export function receiveStuff(json) {
  return {
    type: types.RECEIVE_VIDEOS
    , stuff: json.stuff
  };
}

export function fetchStuff() {
  return dispatch => {
    return fetch(url(), {
      method: 'GET',
      mode: 'cors',
      credentials: 'include',
      headers: {
        'x-api-key': "1000000",
        'Accept': 'application/json'
      }
    })
    .then(response => response.json())
    .then(json => dispatch(receiveStuff(json)));
  };
}
