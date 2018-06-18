$(window).on('load resize orientationchange', function () {
    $('.serv-container').each(function () {
        var $carousel = $(this);
        // ativa o slick apenas em telas que width < height
        if ($(window).width() > $(window).height()) {
            if ($carousel.hasClass('slick-initialized')) {
                $carousel.slick('unslick');
            }
        } else {
            if (!$carousel.hasClass('slick-initialized')) {
                $carousel.slick({
                    dots: true, // ativa os pontos
                    arrows: false,  // remove as setas
                    slidesToShow: 1, // mostra 1 card por vez
                    slidesToScroll: 1, // passa 1 card por vez
                });
            }
        }
    });
});