import { useAppSelector } from '../app/hooks';
import Cart from './Cart'
import Products from './Products'

function Homepage(): JSX.Element {
    const products = useAppSelector((state) => state.products);
  return (
    <div className='home'>
          {products?.map((product) => (
              <Products{...product} />
        ))}
        <Cart/>
    </div>
  )
}

export default Homepage