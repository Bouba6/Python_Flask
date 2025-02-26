
const button1 = document.getElementById("price");

button1.addEventListener("click", function () {
    try {
        let id = button1.value;
        fetch(`/addtocart/${id}`, {
            method: "POST",

        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
            });
    } catch (error) {
        console.error(error);
    }

});