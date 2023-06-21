$(document).ready(function() {
    $("#imageDiv").click(function(){
        $("#imageBt").trigger("click");
    });


    $("#imageBt").change(function() {
        var file = this.files[0];
        var reader = new FileReader();

        reader.onload = function(e) {
          $('#imageContainer').html('<img src="' + e.target.result + '" class="thumbnail">');
        }

        reader.readAsDataURL(file);
    });

    $("#createPostBT").click(function(){
        $("createPostSb").trigger("click");
    })
});
