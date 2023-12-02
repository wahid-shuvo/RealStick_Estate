import {v4 as uuid} from 'uuid';
import {SET_ALERT, REMOVE_ALERT} from "./types";

export const setAlert = (msg, alertType, timeout = 5000) => dispatchEvent => {
    const id = uuid();
    dispatchEvent({
        type: SET_ALERT,
        payload: {msg, alertType, id}
    });
    setTimeout(() => dispatchEvent({type: REMOVE_ALERT, payload: id}), timeout)
}