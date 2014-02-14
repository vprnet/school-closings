var closings_container = $('#closings_container'),
    sidebar_container = $('#sidebar_container');

$(window).resize(function() {
    if ( Modernizr.mq('(min-width: 768px)') ) {
        closings_container.after(sidebar_container);
    }
    else {
        sidebar_container.after(closings_container);
    }
}).resize();

