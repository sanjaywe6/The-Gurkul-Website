$(document).ready(function () {
    
    // js for main page image slider
    imageCount_img_slide1 = $('#image_slide_container_img_slide1 .slider_images_img_slide1').length;
    currentImage_img_slide1 = 0;
    function slideToNextImage_img_slide1() {
        currentImage_img_slide1++;
        if (currentImage_img_slide1 > imageCount_img_slide1) {
            currentImage_img_slide1 = 1;
        }
        moveSlider_img_slide1(currentImage_img_slide1, imageCount_img_slide1);
    }
    function slideToPrevImage_img_slide1() {
        currentImage_img_slide1--;
        if (currentImage_img_slide1 < 1) {
            currentImage_img_slide1 = imageCount_img_slide1;
        }
        moveSlider_img_slide1(currentImage_img_slide1, imageCount_img_slide1)
    }
    function moveSlider_img_slide1(id, length) {
        for (let index = 1; index <= length; index++) {
            if (id == index) {
                $(`#slider_img_${index}_img_slide1`).addClass('decompress_slide_img_img_slide1')
                $(`#slider_img_${index}_img_slide1`).removeClass('compress_slide_img_img_slide1')
                $(`#slider_image_text_${index}_img_slide1`).css('display', 'unset')
                $(`#slider_image_indicator_${index}_img_slide1`).css('background-color', 'red')
            }
            else {
                $(`#slider_img_${index}_img_slide1`).removeClass('decompress_slide_img_img_slide1')
                $(`#slider_img_${index}_img_slide1`).addClass('compress_slide_img_img_slide1')
                $(`#slider_image_text_${index}_img_slide1`).css('display', 'none')
                $(`#slider_image_indicator_${index}_img_slide1`).css('background-color', 'white')

            }
        }
    }
    var imagSlideInterval_img_slide1 = setInterval(slideToNextImage_img_slide1, 4000);
    $('#img_slider_next_img_slide1').click(function () {
        clearInterval(imagSlideInterval_img_slide1)
        slideToNextImage_img_slide1()
    })
    $('#img_slider_prev_img_slide1').click(function () {
        clearInterval(imagSlideInterval_img_slide1)
        slideToPrevImage_img_slide1();
    });
    slideToNextImage_img_slide1()

    // js for showing animation gurkul quotes when scrolled but fixed device size
    var device_width = window.innerWidth
    if (device_width > 1351) {

      window.addEventListener("scroll", function () {
        home_scroll = scrollY;

        if (home_scroll > 1350) {
          $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
        }
        if (home_scroll > 1700) {
          $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
        }

      });

    }
    else if (device_width > 676 && device_width < 1350) {

      window.addEventListener("scroll", function () {
        home_scroll = scrollY;

        if (home_scroll > 1200) {
          $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
        }
        if (home_scroll > 1700) {
          $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
        }

      });

    }

    // when device with less than 676px
    else if (device_width < 677 && device_width > 550) {

      window.addEventListener("scroll", function () {
        home_scroll = scrollY;

        if (home_scroll > 911) {
          $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
        }
        if (home_scroll > 1500) {
          $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
        }

      });

    }


    // when device with less than 550px
    else if (device_width < 551 && device_width > 460) {

      window.addEventListener("scroll", function () {
        home_scroll = scrollY;

        if (home_scroll > 900) {
          $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
        }
        if (home_scroll > 1500) {
          $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
        }

      });

    }


    // when device with less than 500px
    else if (device_width < 461) {
      console.log(device_width)
      window.addEventListener("scroll", function () {

        home_scroll = scrollY;
        console.log(home_scroll)

        if (home_scroll > 700) {
          $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
        }
        if (home_scroll > 1350) {
          $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
        }

      });

    }

    $(window).resize(function () {

        // js for showing animation gurkul quotes when scrolled and changing the device width device size
        var device_width = window.innerWidth
  
  
        // when device with greater than 1350px
        if (device_width > 1351) {
  
          window.addEventListener("scroll", function () {
            var window_width = window.innerWidth
            home_scroll = scrollY;
  
            if (home_scroll > 1350) {
              $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
            }
            if (home_scroll > 1700) {
              $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
            }
  
          });
  
        }
  
        // when device with greater than 676px but less than 1350
        else if (device_width > 676 && device_width < 1350) {
  
          window.addEventListener("scroll", function () {
            var window_width = window.innerWidth
            home_scroll = scrollY;
  
            if (home_scroll > 1200) {
              $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
            }
            if (home_scroll > 1700) {
              $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
            }
  
          });
  
        }
  
        // when device with less than 676px
        else if (device_width < 677 && device_width > 550) {
  
          window.addEventListener("scroll", function () {
            var window_width = window.innerWidth
            home_scroll = scrollY;
  
            if (home_scroll > 911) {
              $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
            }
            if (home_scroll > 1500) {
              $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
            }
  
          });
  
        }
  
  
        // when device with less than 550px
        else if (device_width < 551 && device_width > 460) {
  
          window.addEventListener("scroll", function () {
            var window_width = window.innerWidth
            home_scroll = scrollY;
  
            if (home_scroll > 900) {
              $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
            }
            if (home_scroll > 1500) {
              $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
            }
  
          });
  
        }
  
  
        // when device with less than 500px
        else if (device_width < 461) {
  
          window.addEventListener("scroll", function () {
            var window_width = window.innerWidth
            home_scroll = scrollY;
  
            if (home_scroll > 700) {
              $('.quote_div_thegurkul1').addClass('quote_div_thegurkul_1_animate')
            }
            if (home_scroll > 1350) {
              $('.quote_div_thegurkul2').addClass('quote_div_thegurkul_2_animate')
            }
  
          });
  
        }
  
  
  
  
  
      })


      $(document).ready(function () {

        setInterval(function () {
    
          $.ajax({
            url: '/total_visitor/',
            type: 'get',
            data: {},
            success: function (data) {
              list = data.data
              $('#count_number_thegurkul0').text(list[0])
              $('#count_number_thegurkul1').text(list[1])
              $('#count_number_thegurkul2').text(list[2])
              $('#count_number_thegurkul3').text(list[3])
              $('#count_number_thegurkul4').text(list[4])
              $('#count_number_thegurkul5').text(list[5])
            }
    
    
          })
    
    
        },50000000)
    
      })





  })