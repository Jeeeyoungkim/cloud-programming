tailwind.config = {
  theme: {
    extend: {
      colors: {
        mySky: "#30A2FF",
        blackSky: "#37364A",
      },
    },
  },
};

$("#signupBT").click(function(){
    $("signupSB").trigger("click");
})

$("#signinBT").click(function(){
    $("signinSB").trigger("click");
})

$("#findPwBt").click(function(){
    $("findPwSb").trigger("click");
})

$("#resetPwBt").click(function(){
    $("resetPwSb").trigger("click");
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

$(document).ready(function() {
    $("#findIdBt").click(function(){
        var nickname = $("#username").val()
        data = {"nickname":nickname}
        var csrftoken = getCookie('csrftoken');
        $.ajax({
          url: '/account/findid/',
          type: 'POST',
          headers: {
              'X-CSRFToken': csrftoken
          },
          data: JSON.stringify(data),
          success: function(response) {
            console.log($("#findIdRs").text())
            $("#findIdRs").text(response.nickname+"님의 이메일 아이디는")
            var email = response.email;

            // <span> 요소 생성 및 속성 설정
            var spanElement = $('<span>').addClass('block text-lg text-blue-600 font-bold').text(email);
            $('#findIdRs').text(response.nickname+"님의 이메일 아이디는 ").append(spanElement).append(" 입니다");
            console.log($("#findIdRs").text())
          },
          error: function(xhr, status, error) {
            if (xhr.status === 400){
                alert("일치하는 닉네임이 없습니다.")
                location.reload()
            }
          }
        });
    })
})
