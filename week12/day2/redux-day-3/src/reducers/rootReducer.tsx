type ProductDetail = {
    description: string;
    price:string
}

const initialProducts = [
    {
        description: "Ethan's Gucci Hat",
        price: "$50000"
    },
    {
        description: "Joe's Prada Glasses",
        price: "$3000"
    },
    {
        description: "Rolex Submariner",
        price: "$A Cool 2 Mil$"
    },
    {
        description: "Cole Haan Crocskin Loafers",
        price: "$2000"
    },
    {
        description: "The BLK Cigar",
        price: "$500"
    },
    {
        description: "Uchi Omakase",
        price: "$200"
    },
]

type State = {
    products: ProductDetail[];
    cart: ProductDetail[];
    order: {}
}

const initialState: State = {
    products: initialProducts,
    cart: [],
    order: {
        name: "EthanG",
        items:[]
    }
};

// type Product = {
//     description: string,
//     price:string
// }

type Action = {
    type: string,
    payload?: any;
}

const rootReducer = (state = initialState, action: Action) => {
    switch (action?.type) {
        case "ADD_TO_CART":
            const newCart = state.cart;
            return {...state, cart: [...newCart, action?.payload] }
        case "REMOVE_FROM_CART":
            return {...state, cart: [...state.cart].filter(value => value !== action.payload) }
        // case "ADD":
        // return { ...state, counter: state.counter+1 };
        // case "SUB":
        // return { ...state, counter: state.counter-1 };
        default:
            return state;
    }
};

export default rootReducer;