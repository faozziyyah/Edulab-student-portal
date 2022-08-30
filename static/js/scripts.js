$( window ).on("load", function() {
    $("#myModal").modal("show");
    $("#content").hide();
    $(".update-content").hide();
    $(".edit-word, .edit-meaning").hide();
    $(".submit, .cancel").hide();

    $('#modal').click(function() {
        $("#content").show();
    });

    $('#close').click(function() {
        $("#content").hide();
    });

    $('#update-close').click(function() {
        $(".update-content").hide();
    });

    // upload image operation

    $("#logo-form").submit(function() {
        let data = new FormData();
        data.append('file', $('#logo')[0].files[0]);

        $.ajax({
            url: '/addlogo',
            type: 'POST',
            data: data,
            enctype: 'multipart/form-data',
            processData: false,
            contentType: false,
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err);
            }
        })
    });


    //create operation
    $("#student-form").submit(function() {
        let firstname = $('#firstname').val();
        let phone = $('#phone').val();
        let jambscore = $('#score').val();
        let email = $('#email').val();
        let student_id = $('#student_id').val();

        $.ajax({
            url: '/insert',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                'firstname': firstname,
                'jambscore': jambscore,
                'phone': phone,
                'email': email,
                'student_id': student_id
            }),
            contentType: 'application/json, charset=utf-8',
            success: function(data) {
                location.reload();
            },

           error: function(err) {
                console.log(err);
            }
        })
    });

    // delete operation
    $(".delete").click(function() {
        let word_id = $(this).attr('id');

        $.ajax({
            url: '/word/' + word_id + '/delete',
            type: 'POST',
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err);
            }
        });
    });

        // update operation

        $(".edit").click(function() {
            let parent = $(this).parents('tr');
            parent.find(".edit-word, .edit-meaning").show();
            parent.find(".word-word, .word-meaning").hide();
            $(".submit, .cancel").show();
            parent.find(".edit, .delete").parent().hide();
        });

    $('.cancel').click(function() {
        location.reload();
    });

    $(".update-form").submit(function() {
        //let parent = $(this).parents('tr');
        let firstname = $('input').val();
        let lastname = $('input').val();
        let email = $('textarea').val();
        let word_id = $('.submit').attr('student_id');

        $.ajax({
            url: '/word/' + word_id + '/edit',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify({
                'firstname': firstname,
                'lastname': lastname,
                'email': email
            }),
            contentType: 'application/json, charset=utf-8',
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err);
            }
        })
    });

});