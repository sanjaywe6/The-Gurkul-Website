//  run function when all page loaded
$(document).ready(function(){

    //  function to make navigation bar stickey
    window.onscroll=function(){
        var scroll=window.scrollY
        if(scroll>309){
            $('.gurkulNav').addClass('gurkulNavSticky')
        }
        if(scroll<309){
            $('.gurkulNav').removeClass('gurkulNavSticky')
        }
    }

        // function for animated navigation
    $('.openBtn').click(function(){
        $('.sidenav').css('width','250px')
    })
    $('.closeBtn').click(function(){
        $('.sidenav').css('width','0')
    })
        
        
    })