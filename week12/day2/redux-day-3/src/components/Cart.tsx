import { useAppDispatch, useAppSelector } from '../app/hooks';
import { createClient } from "@supabase/supabase-js";



function Cart(): JSX.Element {
    // const sendToDatabase = async() = {};
    const cart = useAppSelector((state) => state.cart);
    const dispatch = useAppDispatch()
    const supabaseUrl =
    "https://mxakcphctxajogkuteth.supabase.co";
    const supabaseAnonKey =
    'enter your key here'
    const supabase = createClient(
    supabaseUrl,
    supabaseAnonKey,
    );

        const sendToDatabase = async () => {
            const { data, error } = await supabase
            .from('ProductsDatabase')
                .insert([{
                    name: 'Ethan', items: cart }]);
            console.log(data)
        };
    return (
        <div>
            <button onClick={sendToDatabase}>Complete Order</button>
            <div className='Cart-card'>
            {cart.map((item)=>{
                return(
            <>
                <h1>{item.price}</h1>
                <h1>{item.description}</h1>
                <button onClick={() => { dispatch({type:"REMOVE_FROM_CART", payload:item}) }}>Remove from Cart</button>
            </>
            );
            })}
            </div>
        </div>
    );
}

export default Cart