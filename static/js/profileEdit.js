$(document).ready(function() {
        $("#imageContainer").click(function() {
            $("#profileInput").change(function () {
                var file = this.files[0];
                var reader = new FileReader();

                reader.onload = function (e) {
                    $('#imageContainer').html('<img src="' + e.target.result + '" class="thumbnail">');
                }

                reader.readAsDataURL(file);
            });

        })
    $("#updateUserBt").click(function(){
        $("#updateUserSb").trigger("click");
    })
});
