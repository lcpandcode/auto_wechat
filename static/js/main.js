/**
 * Created by lcp on 18-6-21.
 */
$(document).ready(function () {
    $("#register").click(function () {
        $.get("../register_template",function (data,status) {
             $("#main_content").html(data);
        })
    })

    $("#login").click(function () {
        $.get("../login_template",function (data,status) {
             $("#main_content").html(data);
        })
    })

    $("#forget_password").click(function () {
        $.get("../forget_password_template",function (data,status) {
             $("#main_content").html(data);
        })
    })
    $("#auto_replay").click(function () {
        $.get("../init",function (data) {
             $("#main_content").html(data);
        })
    })

})
