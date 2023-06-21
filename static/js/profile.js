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

$(document).ready(function() {

    $(".followBt").click(function(){

        var user_nickname = $(this).attr("id")
        console.log(user_nickname)
        data = {"user_nickname":user_nickname}
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url: '/account/follow/',
          type: 'POST',
          headers: {
              'X-CSRFToken': csrftoken
          },
          data: JSON.stringify(data),
          success: function(response) {
            location.reload();
          },
          error: function(xhr, status, error) {
            if (xhr.status === 400){

            }
          }
        });


    });

    $(".unFollowBt").click(function(){

        var user_nickname = $(this).attr("id")
        console.log(user_nickname)
        data = {"user_nickname":user_nickname}
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url: '/account/unFollow/',
          type: 'POST',
          headers: {
              'X-CSRFToken': csrftoken
          },
          data: JSON.stringify(data),
          success: function(response) {
            location.reload();
          },
          error: function(xhr, status, error) {
            if (xhr.status === 400){

            }
          }
        });


    });
});
