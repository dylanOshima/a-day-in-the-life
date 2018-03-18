import initialState from './initialState';
import { FETCH_VIDEOS, RECEIVE_VIDEOS } from '../actions/actionTypes';

export default function stuff(state = initialState.videos, action) {
  let newState;

  switch (action.type) {
    case FETCH_VIDEOS:
      console.log('FETCH_VIDEOS Action');
      return action;

    case RECEIVE_VIDEOS:
      newState = action.videos
      console.log('RECEIVE_VIDEOS action');
      return newState;

    default:
      return state;
  }
}
