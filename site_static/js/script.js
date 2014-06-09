$(function () {
    var i = 0;
    var slide = $(".slider").find("li");
    var item = $(".slider_in").find(".usl");
    var size = item.size();
    var map = $("#gruz").find("a.main_fon");
    var city = $(".city");

    $(".dot").find("li").eq(0).find('a').click(function () {
        if (!item.is(":animated")) {
            if (!$(this).hasClass("active")) {
                clearInterval(autoplay);
                rotate2();

            }
        }
        return false;
    });
    function rotate1() {
        $(".dot li a").removeClass("active");
        $(".dot").find("li").eq(1).find('a').addClass("active");
        $(".slider").find("li").eq(1).animate({
            left: 0
        });
        $(".slider").find("li").eq(0).fadeOut(function () {
            disappearance();
        });
    }

    function rotate2() {
        i = 0;
        $(".dot li a").removeClass("active");
        $(".dot").find("li").eq(0).find('a').addClass("active");
        $(".slider").find("li").eq(0).show().css('opacity', '1');
        $(".slider").find("li").eq(1).fadeOut(function () {
            $(".slider").find("li").eq(1).css("left", 915).fadeIn(1);
        });
        appearance();

    }


    $(".dot").find("li").eq(1).find('a').click(function () {
        if (!item.is(":animated")) {
            if (!$(this).hasClass("active")) {
                clearInterval(autoplay);
                rotate1();
            }
        }
        return false;
    });

    function appearance() {
        item.eq(i).animate({
            left: '-=915'
        }, 1000, function () {
        });
        i++;
        if (i < size) {
            setTimeout(appearance, 300)
        }
    }

    function disappearance() {
        for (i = 0; i < size; i++) {
            item.eq(i).animate({
                left: '+=915'
            });
        }
    }

    function auto() {
        setTimeout(rotate1, 1000);
        setTimeout(rotate2, 11000);


    }

    $(".slider").find("li").eq(0).show().css('left', 915);
    appearance();
    autoplay = setInterval(auto, 21000);

    //options

    $('.selected_select').find('select').on('change', way);

    function way() {
        clearInterval(autoplay);

        var op = $(".selected_select option:selected").val();
        switch (op) {
            case '0':
                map.css('background-image', 'url' + '(./images/map.png)');
                map.css('background-position', '110px 20px');
                city.show();
                break;
            case '1':
                map.css('background-image', 'url' + '(./images/way1.jpg)');
                map.css('background-position', '108px 19px');
                city.hide();
                break;
            case '2':
                map.css('background-image', 'url' + '(./images/way2.jpg)');
                map.css('background-position', '109px 19px');
                city.hide();
                break;
            case '3':
                map.css('background-image', 'url' + '(./images/way3.jpg)');
                map.css('background-position', '110px 19px');
                city.hide();
                break;
        }
    }


});

function getTime() {
        var d = new Date();
        var hours = d.getUTCHours();
        var minutes = d.getUTCMinutes();
        if (minutes <= 9) minutes = "0" + minutes;
        var setTime = [hours + 3, hours + 10, hours + 7];
        var countryLength = $(".h").size();
        for (var i = 0; i < countryLength; i++) {
            if (setTime[i] > 23) {
                setTime[i] -= 24
            }
            if (setTime[i] <= 9) setTime[i] = "0" + setTime[i];
            $(".h").eq(i).html(setTime[i])
        }
        $(".clock").find(".m").html(minutes);
    }
    setInterval(getTime, 2000)