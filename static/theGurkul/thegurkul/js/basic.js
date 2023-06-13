$(document).ready(function(){

    // code for onloading animation
      $(document).ready(function () {
    $('#loading').css('display', 'none')
    })

    //  function to make navigation bar stickey
    function device_width_navigationbar_static(scroll, width) {
      if (scroll > 267 & device_width > 779) {
        $('#navigation_bar_statick').addClass('navigation_bar_statick')
        $('#navigation_bar_logo').css('display', 'unset')
      }
      else if (scroll < 268 & device_width > 779) {

        $('#navigation_bar_statick').removeClass('navigation_bar_statick')
        $('#navigation_bar_logo').css('display', 'none')
      }
      else if (device_width < 780 & scroll > 325) {
        $('#navigation_bar_statick').addClass('navigation_bar_statick')
        $('#navigation_bar_logo').css('display', 'unset')
      }
      else if (device_width < 780 & scroll < 325) {
        $('#navigation_bar_statick').removeClass('navigation_bar_statick')
        $('#navigation_bar_logo').css('display', 'none')
      }

    }
    $(window).scroll(function () {
      device_width = window.innerWidth
      scroll_val = window.scrollY
      device_width_navigationbar_static(scroll_val, device_width)
    })


    // code for dynamic navigation bar
    function big_device_width_navigationbar() {
      // all adding class
      // css to inline the all navigation link 
      $('.nav_link').addClass('first_nav_link ')
      // for justifying all navigation element space around
      $('#ul_div').addClass('first_ul')
      // to change the width of navigationbar
      $('#sanjay_web_nav').addClass('first_navigation_div')
      $('#offcanvas-div').addClass('first_offcanvas_body')
      // to remove padding in scroll close btn
      $('#close_button_off_canvas').addClass('close_button_off_canvas')

      // all removing class
      // to expand the navigation from scroll to linear
      $('#sanjay_web_nav').removeClass('offcanvas offcanvas-start')
      // to float login type outer button to right
      $('#scroll_out_list').removeClass('scroll_out_list')

      // all adding css
      // hiding scroll close button
      $('#btn_nav_close').css('display', 'none')
      // hiding scroll open button
      $('#nav_scroll_btn').css('display', 'none')
      $('#sanjay_web_nav').css('visibility', 'unset')
    }
    function small_device_width_navigationbar() {
      $('.nav_link').removeClass('first_nav_link ')
      $('#ul_div').removeClass('first_ul')
      $('#sanjay_web_nav').removeClass('first_navigation_div')
      $('#offcanvas-div').removeClass('first_offcanvas_body')
      $('#close_button_off_canvas').removeClass('close_button_off_canvas')

      $('#sanjay_web_nav').addClass('offcanvas offcanvas-start')
      $('#scroll_out_list').addClass('scroll_out_list')

      $('#btn_nav_close').css('display', 'unset')
      $('#nav_scroll_btn').css('display', 'unset')

    }
    var load_device_width = window.innerWidth
    if (load_device_width > 999) {
      big_device_width_navigationbar()
    }
    else if (load_device_width < 1000) {
      small_device_width_navigationbar()
    }
    $(window).resize(function () {

      var load_device_width = window.innerWidth
      if (load_device_width > 999) {
        big_device_width_navigationbar()
      }

      else if (load_device_width < 1000) {
        small_device_width_navigationbar()
      }

    })

   
    


})