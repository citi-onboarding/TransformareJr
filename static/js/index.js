$(window).on('load resize orientationchange', function () {
    $('.serv-container').each(function () {
        var $carousel = $(this);
        /* Initializes a slick carousel only on mobile screens */
        // slick on mobile
        if ($(window).width() > $(window).height()) {
            if ($carousel.hasClass('slick-initialized')) {
                $carousel.slick('unslick');
            }
        }
        else {
            if (!$carousel.hasClass('slick-initialized')) {
                $carousel.slick({
                    dots: true,
                    arrows: false,
                    centerMode: true,
                });
            }
        }
    });
});