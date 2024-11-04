document.getElementById("quiz-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";

    let answers = [];
    const formData = new FormData(event.target);

    formData.forEach((value, key) => {
        answers.push({ question: key, answer_id: value });
    });

    console.log("Answers to submit:", answers);

    fetch("/check_answers", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ answers })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `You got ${data.correct_count} out of ${answers.length} correct!`;
        resultDiv.style.color = "green";
    })
    .catch(error => {
        console.error("Error:", error);
        resultDiv.innerHTML = "An error occurred while checking your answers.";
        resultDiv.style.color = "red";
    });
});
