
$(document).ready(function(){
    console.log("loaded");
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();

        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                if(response == "success"){
                    alert("Congrats! Your account has been created.");
                    window.location.href = '/login'
                }else if(response == "fail"){
                    alert("Username is has been taken! Choose another.");
                }else{
                    alert("Something went wrong!")
                }
            }
        });
    });

    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var form = $("#login-form").serialize();
        $.ajax({
            url: '/checklogin',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == "error"){
                    alert("Could not log in.");
                }else{
                    console.log("Logged in as", res);
                    window.location.href = "/";
                }
            }
        });
    });

    $(document).on("click", "#logout-link", function(e){
        e.preventDefault();

        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == "success"){
                    window.location.href = "/login";
                }else{
                    alert("Something went wrong");
                }
            }
        });
    });

    $(document).on("submit", "#post-activity", function(e){
        e.preventDefault();

        var form = $('#post-activity').serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function(res){
                if(res == 'success'){
                    console.log("post sent successfully.");
                }else{
                    alert('something went wrong');
                }
            }
        });
    });

});
