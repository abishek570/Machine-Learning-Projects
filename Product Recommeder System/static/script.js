document.addEventListener('DOMContentLoaded', () => {
    const productGrid = document.getElementById('product-grid');

    // Fetch product data
    fetch('/api/products?limit=25')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(products => {
            renderProducts(products);
        })
        .catch(error => {
            console.error('Error fetching products:', error);
            productGrid.innerHTML = '<p class="error-msg">Failed to load products. Please try again later.</p>';
        });

    function renderProducts(products) {
        productGrid.innerHTML = ''; // Clear loading state

        products.forEach((product, index) => {
            const card = document.createElement('article');
            card.classList.add('product-card');

            // Stagger animation delay
            card.style.animation = `fadeInUp 0.5s ease-out ${index * 0.05}s forwards`;
            card.style.opacity = '0'; // Initial state for animation

            card.onclick = () => window.location.href = `/product/${product.id}`;
            card.style.cursor = 'pointer';

            card.innerHTML = `
                <div class="product-image">
                    <span class="product-tag">Fresh</span>
                    <img src="${product.image}?random=${product.id}" alt="${product.name}" loading="lazy">
                </div>
                <div class="product-details">

                    <h3 class="product-title">${product.name}</h3>
                    <p class="product-desc" title="${product.description}">${product.description}</p>
                    <div class="price-row">
                        <span class="price">₹${product.price}</span>
                        <button class="add-btn" aria-label="Add to cart" onclick="event.stopPropagation()">
                            <i class="fa-solid fa-plus"></i>
                        </button>
                    </div>
                </div>
            `;

            productGrid.appendChild(card);
        });
    }
});
