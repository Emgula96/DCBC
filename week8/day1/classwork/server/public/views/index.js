const button = document.getElementById("button");
const searchBtn = document.getElementById("search");


const createRestaurant = async () => {
  const name = document.getElementById("name").value;
  const address = document.getElementById("address").value;
  const reviewScore = document.getElementById("review").value;
  const restaurantCreate = {
    name,
    address,
    reviewScore,
    createdAt: new Date(),
    updatedAt: new Date(),
  };
  const send = await fetch(
    "http://localhost:3008/restaurants/create_restaurant",
    {
      method: "POST",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify(restaurantCreate),
    }
  );
  const json = await send.json();
  console.log(json);
};

button.onclick = createRestaurant;

const getRestaurant = async () => {
  const userSearch = document.getElementById("userSearch").value;
  const send = await fetch(
    "http://localhost:3008/restaurants/by_name",
    {
      method: "GET",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: JSON.stringify(userSearch),
    }
  );
  const json = await send.json();
  console.log(json);
};


searchBtn.onclick = getRestaurant;