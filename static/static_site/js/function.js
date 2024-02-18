console.log("working fine")

$("#ReviewFrom").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(res){
            console.log("Comment Saved to DB...");

            if(res.bool == true)
                $("#review-res").html("Review added successfully.")
        }
    })

})