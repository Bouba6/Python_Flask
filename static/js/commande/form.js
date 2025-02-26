let total = document.getElementById("total");
function incrementQuantity(productId) {
    console.log(productId);
    let quantityInput = document.getElementById(`quantity-${productId}`);
    let quantity = parseInt(quantityInput.value);
    quantity++;
    quantityInput.value = quantity;
    fetch(`/update/${productId}`, {  // Remplacer "id" par productId
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ quantity: quantity })

    })
        .then(response => response.json())
        .then(data => {
            // Extraire le total actuel (en supposant qu'il se trouve dans le texte de la div)
            let oldTotal = parseFloat(total.innerHTML.replace(/[^0-9.-]+/g, ""));
            let newTotal = oldTotal + parseFloat(data.total);
            total.innerHTML = `Sous Total : ${newTotal.toFixed(2)} $`;
            console.log(data);
        });
}

function decrementQuantity(productId) {
    let quantityInput = document.getElementById(`quantity-${productId}`);
    let quantity = parseInt(quantityInput.value);
    if (quantity > 1) {
        quantity--;
        quantityInput.value = quantity;
        fetch(`/update/${productId}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ quantity: quantity })
        })
            .then(response => response.json())
            .then(data => {

                total.innerHTML = `Sous Total : ${data.total} $`;
            });
    }
}
