var labelElements = document.querySelectorAll('label[for="id_question"]');
labelElements.forEach(function(labelElement) {
    labelElement.style.display = 'none';
});
document.getElementById('error_1_id_question').style.display = 'none'

var currentFaq = 1

var answerContainer = document.getElementById('answer-container')
// var generatedText = document.getElementById("generatedText")
var url = window.location.href

var question = document.getElementById("id_question")
question.classList.remove('is-invalid')
var submitForm = document.getElementById('form')

var csrf = document.getElementsByName("csrfmiddlewaretoken")[0]

submitForm.addEventListener('submit', function(e) {
    e.preventDefault()
    var fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf.value)
    fd.append('question', question.value)
    fd.append('type', "book")
    $.ajax({
        type:'POST', 
        url: url,
        data: fd,
        success: function(response){
            console.log("everything went well, here is the response status: ", response.status)
            answerContainer.classList.remove("not-visible")
            currentFaq = response.faqId
            // loadAnswer()
            document.getElementById("submit-form-button").classList.add("not-visible")
            document.getElementById("like-button").classList.remove("not-visible")
            document.getElementById("dislike-button").classList.remove("not-visible")
            document.getElementById("refresh-button").classList.remove("not-visible")
            document.getElementById("submit-form-button").classList.remove("btn", "btn-primary")
            document.getElementById("like-button").classList.add("btn", "btn-primary")
            document.getElementById("dislike-button").classList.add("btn", "btn-primary")
            document.getElementById("refresh-button").classList.add("btn", "btn-primary")

        },
        error:function(error){
            console.log(error)
        },
        cache:false,
        contentType:false,
        processData:false,
    })
})

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function rateAnswerPut(ratingType, selected, unselected, action) {

    var csrfToken = getCookie('csrftoken');

    // Make sure the token is retrieved successfully
    if (csrfToken === null) {
        console.error('CSRF token not found.');
        return;
    }

    $.ajax({
        url: url + action + currentFaq,
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(ratingType),
        headers: { 'X-CSRFToken': csrfToken }, 
        success: function(response) {
            document.getElementById(selected).classList.add("border", "border-warning", "text-warning")

            if (document.getElementById(unselected).classList.contains("border", "border-warning", "text-warning")){
                document.getElementById(unselected).classList.remove("border", "border-warning", "text-warning")
            }
        },
        error: function(error) {
            console.error('Error in update request:', error);
        }
    });
}

document.getElementById("like-button").addEventListener('click', () => {
    var ratingType = true
    rateAnswerPut(ratingType, 'like-button', 'dislike-button', 'like_it/')
})

document.getElementById("dislike-button").addEventListener('click', () => {
    var ratingType = false
    rateAnswerPut(ratingType, 'dislike-button', 'like-button', 'dislike_it/')
})