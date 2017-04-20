$(document).ready(function() {
    //responsive menu toggle
    $("#menutoggle").click(function() {
        $('.xs-menu').toggleClass('displaynone');

    });
    //add active class on menu
    
    //drop down menu    
    $('li.drop-down').hover(
        function() {
            $(this).children("div").addClass('display-on');
        },
        function() {
            $(this).children("div").removeClass('display-on');
        }
    );
    //collapse table
    $('.click_toggle').click(function(){
        $(this).next().toggle('fast');
        $(this).next().addClass('display-on');
    });

});

function myFunction() {
    var x = document.getElementById("myMenu");
        if (x.className === "menu") {
                x.className += " responsive";
        } else {
                x.className = "menu";
        }
    }