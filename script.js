// Product data (you can replace this with your own data)
const products = [
  { id: 1, name: "Product 1", price: 10 },
  { id: 2, name: "Product 2", price: 20 },
  { id: 3, name: "Product 3", price: 30 },
];

// Cart object to store added items
const cart = {
  items: [],
  addItem: function (product) {
    this.items.push(product);
  },
  getTotalPrice: function () {
    let totalPrice = 0;
    for (let i = 0; i < this.items.length; i++) {
      totalPrice += this.items[i].price;
    }
    return totalPrice;
  },
};

// Function to render products on the page
function renderProducts() {
  const productContainer = document.getElementById("product-container");
  productContainer.innerHTML = "";

  for (let i = 0; i < products.length; i++) {
    const product = products[i];
    const productElement = document.createElement("div");
    productElement.innerHTML = `${product.name} - $${product.price}`;

    const addButton = document.createElement("button");
    addButton.textContent = "Add to Cart";
    addButton.addEventListener("click", function () {
      cart.addItem(product);
      updateCart();
    });

    productElement.appendChild(addButton);
    productContainer.appendChild(productElement);
  }
}

// Function to update the cart information on the page
function updateCart() {
  const cartItemsContainer = document.getElementById("cart-items-container");
  cartItemsContainer.innerHTML = "";

  for (let i = 0; i < cart.items.length; i++) {
    const cartItem = cart.items[i];
    const cartItemElement = document.createElement("div");
    cartItemElement.textContent = `${cartItem.name} - $${cartItem.price}`;

    cartItemsContainer.appendChild(cartItemElement);
  }

  const totalPriceElement = document.getElementById("total-price");
  totalPriceElement.textContent = "$" + cart.getTotalPrice();
}

// Call the renderProducts function to initially display the products
renderProducts();
