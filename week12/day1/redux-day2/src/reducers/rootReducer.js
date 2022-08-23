const initialState = {
    weather:  {},
    location: "",
    changeMe: "",
    
};

const rootReducer = (state=initialState,action) => {
    switch (action.type) {
        case "GET_USER":
            return { ...state }
        case "SET_LOCATION":
            return { ...state, location: action.payload  }
        case "SET_WEATHER":
            return { ...state, weather: action.payload }
        case "SAVE_CHANGEME":
            return { ...state, changeMe: action.payload }
        default:
            return state;
    }
};

export default rootReducer