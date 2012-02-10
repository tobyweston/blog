
function redirect(){
    // Fade the page, hide the 'Not found' message a little, there's still hope!
    jQuery('#entry-title').css('opacity', 0.3);

    // If the JSON is taking its time or fail then reset
    var timeout = setTimeout(function(){
        jQuery('#entry-title).css('opacity', 1);
    }, 2000);

    // Get the JSON. Using jQuery.
    jQuery.getJSON('/javascripts/url_migrations.json?r='+Math.random(), function(data){
        var found = false;
        alert("hello");
        jQuery.each(data['redirects'], function(idx, url){
            if(url[0] == window.location.pathname){
                window.location.replace(url[1]);  // redirect
                found = true;
                return false;
            }
        });

        // Cleanup...
        if(found)
            return;

        jQuery('#entry-title').css('opacity', 1);
        clearTimeout(timeout);
    });

};