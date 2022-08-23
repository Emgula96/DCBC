import { useAppDispatch } from "../app/hooks";

type ProductDetail = {
    description: string;
    price: string;
}

const Products = (props: ProductDetail): JSX.Element => {
    const dispatch = useAppDispatch()
    return (
        <>
            <div className="Card">
            <h4>{props.description}</h4>
            <h4>{props.price}</h4>
            <button onClick={() => dispatch({ type: "ADD_TO_CART", payload:props})}>Add to cart</button>
            </div>
        </>
    );
};

export default Products