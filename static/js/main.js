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
//    $("#created").trigger("click");

    $(".postSaveBt").click(function(){

        var post_id = $(this).attr("id")
        console.log(post_id)
        data = {"post_id":post_id}
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url: '/content/post/save/',
          type: 'POST',
          headers: {
              'X-CSRFToken': csrftoken
          },
          data: JSON.stringify(data),
          success: function(response) {
            console.log(response.saved)
            $('#saved_num').text(response.saved);

          },
          error: function(xhr, status, error) {
            if (xhr.status === 400){

            }
          }
        });


    });

    $(".sadBt").click(function(){

        var post_id = $(this).attr("id")
        console.log(post_id)
        data = {"post_id":post_id}
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url: '/account/sad/',
          type: 'POST',
          headers: {
              'X-CSRFToken': csrftoken
          },
          data: JSON.stringify(data),
          success: function(response) {
            console.log(response.count)
            $("#"+post_id).text("슬퍼요 "+response.count);

          },
          error: function(xhr, status, error) {
            if (xhr.status === 400){

            }
          }
        });


    });

});
