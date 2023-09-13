document.addEventListener("DOMContentLoaded", function () {
    const calculateButton = document.getElementById("calculateButton");
    const string1Input = document.getElementById("string1");
    const string2Input = document.getElementById("string2");
    const resultSpan = document.getElementById("result");
    
    // Trigger Calculate button on "Enter" key press in input fields
    string1Input.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            calculateButton.click();
        }
    });

    string2Input.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            calculateButton.click();
        }
    });
    
    
    calculateButton.addEventListener("click", function () {
        const string1 = string1Input.value;
        const string2 = string2Input.value;
        
        // Send the strings to the server-side Python script for calculation
        fetch(`/calculate?string1=${string1}&string2=${string2}`)
            .then(response => response.json())
            .then(data => {
                resultSpan.textContent = data.distance;
            })
            .catch(error => {
                console.error("Error:", error);
            });
    });
});
